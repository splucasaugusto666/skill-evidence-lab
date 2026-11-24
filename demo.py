"""Reproduce a skill integrity check in an isolated temporary workspace."""
import tempfile
from pathlib import Path
import skilllab


def run():
    library = skilllab.ROOT / 'skills'
    entries = skilllab.catalog(library)
    with tempfile.TemporaryDirectory(prefix='skilllab-demo-') as directory:
        workspace = Path(directory).resolve(strict=True)
        dest = skilllab.install(library, 'code-review', workspace, 'manual', True)
        if dest.exists() or list(workspace.iterdir()):
            raise RuntimeError('Dry run changed the workspace')
        dest = skilllab.install(library, 'code-review', workspace, 'manual')
        if skilllab.validate(dest) != skilllab.validate(library / 'code-review'):
            raise RuntimeError('Installed package differs from source')
        with (dest / 'SKILL.md').open('ab') as stream:
            stream.write(b'\nDemo-only modification\n')
        try:
            skilllab.validate(dest)
        except ValueError as error:
            if str(error) != 'checksum mismatch':
                raise
        else:
            raise RuntimeError('Modification was not detected')
    return [f'{len(entries)} skills statically validated',
            'Dry run: no files created', 'Installation: verified copy',
            'Modified copy: checksum mismatch detected',
            'Temporary workspace removed; no agent executed']


if __name__ == '__main__':
    print('\n'.join(run()))
