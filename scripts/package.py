#!/usr/bin/env python3
"""Create a deterministic install ZIP from an explicit public-file allowlist."""
import argparse
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    'info.json', 'settings.lua', 'data-final-fixes.lua', 'prototypes/weapons.lua',
    'locale/en/settings.cfg', 'locale/zh-CN/settings.cfg',
    'README.md', 'TESTING.md', 'changelog.txt', 'LICENSE',
)


def create(output):
    info = json.loads((ROOT / 'info.json').read_text())
    prefix = info['name'] + '_' + info['version'] + '/'
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in FILES:
            entry = zipfile.ZipInfo(prefix + name, (2026, 10, 31, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (ROOT / name).read_bytes(), compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        assert set(archive.namelist()) == {prefix + name for name in FILES}
        assert archive.testzip() is None
        for name in FILES:
            assert archive.read(prefix + name) == (ROOT / name).read_bytes(), name
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    print(create(parser.parse_args().output))
