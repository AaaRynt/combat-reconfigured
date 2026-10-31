#!/usr/bin/env python3
"""Dependency-free integration checks using an installed Factorio 2.1.24 executable.

All game files, test mods, configuration, logs and saves live in a temporary folder.
The runner never uses the player's mod directory or saves and runs no build commands.
"""

import argparse
import configparser
import json
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]


def lua(value):
    if isinstance(value, dict):
        return "{" + ",".join("[" + json.dumps(k) + "]=" + lua(v) for k, v in value.items()) + "}"
    if isinstance(value, bool):
        return "true" if value else "false"
    return json.dumps(value)


def execute(command, folder, stop_on_save=None):
    log = folder / "process.log"
    with log.open("w") as output:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=output, stderr=subprocess.STDOUT)
        start = time.monotonic()
        stopped = False
        try:
            while process.poll() is None:
                if stop_on_save and stop_on_save.exists():
                    process.send_signal(signal.SIGINT)
                    process.wait(timeout=10)
                    stopped = True
                    break
                if time.monotonic() - start > 60:
                    raise RuntimeError("Factorio check exceeded 60 seconds")
                # Guard against the excessive memory use reported for huge ranges.
                rss = subprocess.run(["ps", "-o", "rss=", "-p", str(process.pid)],
                                     capture_output=True, text=True).stdout.strip()
                if rss and int(rss) > 2 * 1024 * 1024:
                    raise RuntimeError("Factorio check exceeded the 2 GiB memory guard")
                time.sleep(0.1)
            if process.returncode and not stopped:
                raise RuntimeError(log.read_text()[-9000:])
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
    return log.read_text()


def setup(folder, enabled=True, expansion=False, overrides=None):
    mods = folder / "mods"
    mods.mkdir(parents=True)
    if enabled:
        target = mods / ("combat-reconfigured_" + json.loads((ROOT / "info.json").read_text())["version"])
        target.mkdir()
        for name in ["info.json", "settings.lua", "data-final-fixes.lua", "prototypes", "locale"]:
            source = ROOT / name
            if source.is_dir():
                shutil.copytree(source, target / name)
            else:
                shutil.copy2(source, target / name)
    entries = [{"name": "base", "enabled": True}]
    entries += [{"name": name, "enabled": expansion}
                for name in ["quality", "space-age", "elevated-rails"]]
    if enabled:
        entries.append({"name": "combat-reconfigured", "enabled": True})
    if overrides:
        fixture = mods / "cr-check_0.0.1"
        fixture.mkdir()
        (fixture / "info.json").write_text(json.dumps({
            "name": "cr-check", "version": "0.0.1", "title": "Test fixture", "author": "Astro704",
            "factorio_version": "2.1", "dependencies": ["combat-reconfigured"]}))
        (fixture / "settings-updates.lua").write_text(
            "local overrides = " + lua(overrides) + "\n"
            "for key, value in pairs(overrides) do\n  local found = false\n"
            "  for _, kind in ipairs({'double-setting', 'int-setting', 'bool-setting', 'string-setting'}) do\n"
            "    local setting = data.raw[kind] and data.raw[kind][key]\n"
            "    if setting then setting.default_value = value; found = true end\n"
            "  end\n  assert(found, 'Unknown test setting: ' .. key)\nend\n")
        entries.append({"name": "cr-check", "enabled": True})
    (mods / "mod-list.json").write_text(json.dumps({"mods": entries}))
    return mods
