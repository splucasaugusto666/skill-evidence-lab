"""Offline validator, integrity catalog and conservative local installer."""
import argparse, hashlib, json, re, shutil, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
NAME=re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
PLATFORMS={'codex':'.agents/skills','claude-code':'.claude/skills','gemini-cli':'.gemini/skills','cursor':'.cursor/skills','copilot':'.github/skills','manual':'skills'}

def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d: raise ValueError(f'duplicate key: {k}')
        d[k]=v
    return d

def read_json(p):
    return json.loads(p.read_text(encoding='utf-8'),object_pairs_hook=unique)

def safe_dir(p):
    for q in (p,*p.parents):
        if q.is_symlink(): raise ValueError(f'symlink: {q}')
    if p.exists() and not p.is_dir(): raise ValueError(f'not a directory: {p}')

def validate(p):
    safe_dir(p)
    if not p.is_dir(): raise ValueError(f'missing skill: {p}')
    if not NAME.fullmatch(p.name) or len(p.name)>64: raise ValueError('invalid name')
    if {x.name for x in p.iterdir()}!={'SKILL.md','manifest.json'}: raise ValueError('unsupported package contents')
    for f in p.iterdir():
        if f.is_symlink() or not f.is_file() or f.stat().st_nlink!=1 or f.stat().st_size>128_000: raise ValueError(f'unsafe file: {f}')
    raw=(p/'SKILL.md').read_bytes(); content=raw.decode('utf-8'); lines=content.splitlines()
    if not lines or lines[0]!='---' or '---' not in lines[1:]: raise ValueError('missing frontmatter')
    end=lines.index('---',1); fields={}
    # Intentionally supports only this project's flat YAML subset, not arbitrary YAML.
    for line in lines[1:end]:
        k,sep,v=line.partition(': ')
        if not sep or k not in {'name','description','license'} or k in fields: raise ValueError('unsupported frontmatter')
        fields[k]=json.loads(v) if v.startswith('"') else v
    if fields.get('name')!=p.name or not isinstance(fields.get('description'),str) or not 0<len(fields['description'])<=1024 or fields.get('license')!='MIT': raise ValueError('invalid metadata')
    if not '\n'.join(lines[end+1:]).strip() or len(lines)>500: raise ValueError('empty or oversized instructions')
    m=read_json(p/'manifest.json')
    if not isinstance(m,dict) or m.get('schema_version')!=1 or m.get('name')!=p.name or m.get('version')!='0.1.0' or m.get('maturity')!='STATICALLY_VALIDATED' or m.get('permissions')!={'execution':'none','network':'host-authorized-only','writes':'host-authorized-only'} or not isinstance(m.get('category'),str): raise ValueError('invalid manifest')
    if m.get('sha256')!=hashlib.sha256(raw).hexdigest(): raise ValueError('checksum mismatch')
    return {**m,'description':fields['description']}

def catalog(root):
    safe_dir(root)
    if not root.is_dir(): raise ValueError('missing library')
    entries=[validate(p) for p in sorted(root.iterdir())]
    if not entries: raise ValueError('empty library')
    return entries

def install(source, name, workspace, platform, dry_run=False):
    if not NAME.fullmatch(name) or len(name)>64: raise ValueError('invalid name')
    src=source/name; validate(src)
    safe_dir(workspace)
    if not workspace.is_dir(): raise ValueError('workspace must exist')
    base=workspace/PLATFORMS[platform]; safe_dir(base)
    dest=base/name; safe_dir(dest)
    if dest.exists(): raise ValueError('destination exists; no overwrite')
    if dry_run: return dest
    base.mkdir(parents=True,exist_ok=True); dest.mkdir(exist_ok=False)
    try:
        for filename in ('SKILL.md','manifest.json'):
            with (dest/filename).open('xb') as f: f.write((src/filename).read_bytes())
        validate(dest)
    except Exception:
        shutil.rmtree(dest)
        raise
    return dest

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--library',type=Path,default=ROOT/'skills'); sub=ap.add_subparsers(dest='cmd',required=True)
    for cmd in ('validate','list','catalog'): sub.add_parser(cmd)
    s=sub.add_parser('search');s.add_argument('query')
    i=sub.add_parser('info');i.add_argument('name')
    ins=sub.add_parser('install');ins.add_argument('name');ins.add_argument('--workspace',type=Path,required=True);ins.add_argument('--platform',choices=PLATFORMS,required=True);ins.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(argv)
    try:
        if a.cmd=='install': print(('Would install: ' if a.dry_run else 'Installed: ')+str(install(a.library,a.name,a.workspace,a.platform,a.dry_run)));return 0
        entries=catalog(a.library)
        if a.cmd=='validate': print(f'{len(entries)} skills statically validated')
        elif a.cmd=='catalog': print(json.dumps(entries,indent=2))
        elif a.cmd=='info':
            match=next((x for x in entries if x['name']==a.name),None)
            if match is None: raise ValueError('unknown skill')
            print(json.dumps(match,indent=2))
        else:
            for e in entries:
                if a.cmd=='list' or a.query.casefold() in (e['name']+' '+e['category']+' '+e['description']).casefold(): print(f"{e['name']}\t{e['category']}\t{e['description']}")
        return 0
    except (ValueError,OSError,TypeError) as e: print(f'Error: {e}',file=sys.stderr);return 1
if __name__=='__main__': raise SystemExit(main())
