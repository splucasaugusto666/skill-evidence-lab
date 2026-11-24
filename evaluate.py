"""Offline paired outcome aggregation. Does not execute or judge models."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from skilllab import read_json

DIGEST = re.compile(r'[0-9a-f]{64}\Z')
CONDITIONS = ('A', 'B', 'C', 'D')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=True, allow_nan=False).encode()).hexdigest()


def hex_digest(value):
    return isinstance(value, str) and DIGEST.fullmatch(value) is not None


def validate_plan(plan):
    require(isinstance(plan, dict), 'plan must be an object')
    require(set(plan) == {'schema_version', 'data_origin', 'model', 'config_sha256',
                          'scorer', 'conditions', 'tasks', 'repetitions'}, 'unexpected plan fields')
    require(type(plan['schema_version']) is int and plan['schema_version'] == 1, 'schema version')
    require(plan['data_origin'] in ('synthetic', 'external_unverified'), 'data origin')
    for key in ('model', 'scorer'):
        require(isinstance(plan[key], str) and bool(plan[key].strip()), f'missing {key}')
    require(hex_digest(plan['config_sha256']), 'configuration digest')
    conditions = plan['conditions']
    require(isinstance(conditions, dict) and {'A', 'C'} <= set(conditions) <= set(CONDITIONS), 'conditions')
    require(all(hex_digest(v) for v in conditions.values()), 'condition digests')
    tasks = plan['tasks']
    require(isinstance(tasks, dict) and 0 < len(tasks) <= 10000, 'tasks')
    require(all(k.strip() and hex_digest(v) for k, v in tasks.items()), 'task IDs or digests')
    n = plan['repetitions']
    require(type(n) is int and 1 <= n <= 100 and n * len(tasks) * len(conditions) <= 100000,
            'repetition or grid limit')
    return plan


def evaluate(plan, records):
    validate_plan(plan)
    require(isinstance(records, list), 'records must be an array')
    plan_hash = digest(plan)
    observations = {}
    for row in records:
        require(isinstance(row, dict) and set(row) == {'plan_sha256', 'task', 'repeat', 'condition',
                'status', 'success', 'output_sha256'}, 'unexpected record fields')
        require(row['plan_sha256'] == plan_hash, 'plan hash mismatch')
        task, repeat, condition = row['task'], row['repeat'], row['condition']
        require(isinstance(task, str) and task in plan['tasks'], 'unknown task')
        require(type(repeat) is int and 1 <= repeat <= plan['repetitions'], 'invalid repeat')
        require(isinstance(condition, str) and condition in plan['conditions'], 'unknown condition')
        key = (task, repeat, condition)
        require(key not in observations, 'duplicate observation')
        status = row['status']
        require(status in ('completed', 'error'), 'invalid status')
        if status == 'completed':
            require(type(row['success']) is bool and hex_digest(row['output_sha256']), 'invalid completed record')
        else:
            require(row['success'] is None and row['output_sha256'] is None, 'error must not contain a score')
        observations[key] = row['success']
    slots = [(task, i) for task in sorted(plan['tasks']) for i in range(1, plan['repetitions'] + 1)]
    comparisons = {}
    for left, right in (('A', 'C'), ('B', 'C'), ('C', 'D')):
        if not {left, right} <= set(plan['conditions']):
            continue
        diffs, low, high = [], 0, 0
        wins = losses = ties = 0
        for task, i in slots:
            a, b = observations.get((task, i, left)), observations.get((task, i, right))
            low += (int(b) if b is not None else 0) - (int(a) if a is not None else 1)
            high += (int(b) if b is not None else 1) - (int(a) if a is not None else 0)
            if a is not None and b is not None:
                d = int(b) - int(a)
                diffs.append(d)
                wins += d == 1
                losses += d == -1
                ties += d == 0
        comparisons[f'{right}-{left}'] = {
            'planned_pairs': len(slots), 'complete_pairs': len(diffs),
            'incomplete_pairs': len(slots) - len(diffs), 'wins': wins, 'losses': losses, 'ties': ties,
            'complete_pair_delta': sum(diffs)/len(diffs) if diffs else None,
            'all_planned_delta_bounds': [low/len(slots), high/len(slots)],
        }
    return {'schema_version': 1, 'data_origin': plan['data_origin'], 'plan_sha256': plan_hash,
            'records_sha256': digest(sorted(records, key=lambda r: (r['task'], r['repeat'], r['condition']))),
            'planned_records': len(slots)*len(plan['conditions']), 'received_records': len(records),
            'error_records': sum(r['status'] == 'error' for r in records), 'comparisons': comparisons,
            'limitations': ['Scores supplied by caller; model execution, provenance and scoring not verified.',
                            'Bounds are worst-case missing-data bounds, not confidence intervals.',
                            'Descriptive paired deltas; repeated tasks are not independent samples.']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    parser.add_argument('records', type=Path, nargs='?')
    args = parser.parse_args(argv)
    try:
        plan = validate_plan(read_json(args.plan))
        if args.records is None:
            print(digest(plan))
        else:
            print(json.dumps(evaluate(plan, read_json(args.records)), indent=2, sort_keys=True))
        return 0
    except (ValueError, TypeError, OSError) as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
