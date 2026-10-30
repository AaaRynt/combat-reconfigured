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
        target = mods / "combat-reconfigured_0.1.0"
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
            "for key, value in pairs(overrides) do\n"
            "  for _, kind in ipairs({'double-setting', 'int-setting', 'bool-setting', 'string-setting'}) do\n"
            "    local setting = data.raw[kind] and data.raw[kind]['cr-gun-turret-' .. key]\n"
            "    if setting then setting.default_value = value end\n"
            "  end\nend\n")
        entries.append({"name": "cr-check", "enabled": True})
    (mods / "mod-list.json").write_text(json.dumps({"mods": entries}))
    return mods


def check_locale():
    locales = []
    for language in ["en", "zh-CN"]:
        parser = configparser.ConfigParser(interpolation=None, strict=True, delimiters=("=",))
        parser.read(ROOT / "locale" / language / "settings.cfg")
        names = set(parser["mod-setting-name"])
        assert names == set(parser["mod-setting-description"])
        assert len(names) == 51
        locales.append(names)
    assert locales[0] == locales[1]
    assert json.loads((ROOT / "info.json").read_text())["version"] == "0.1.0"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factorio", type=Path,
                        default=Path("/Applications/factorio.app/Contents/MacOS/factorio"))
    parser.add_argument("--data", type=Path, help="Factorio data directory; inferred for macOS")
    parser.add_argument("--keep", type=Path, help="Keep isolated test files at this new directory")
    parser.add_argument("--extreme-combat", action="store_true",
                        help="Also attempt 10000-tile combat; may fail the memory guard")
    args = parser.parse_args()
    executable = args.factorio.resolve()
    data = args.data or executable.parents[1] / "data"
    check_locale()
    if args.keep:
        args.keep.mkdir(parents=True, exist_ok=False)
        workspace = args.keep.resolve()
    else:
        temporary = tempfile.TemporaryDirectory(prefix="combat-reconfigured-")
        workspace = Path(temporary.name)

    def run(name, enabled=True, expansion=False, overrides=None, scenario=None, save=None, server=False):
        folder = workspace / name
        mods = setup(folder, enabled, expansion, overrides)
        config = folder / "config.ini"
        config.write_text("[path]\nread-data=" + str(data) + "\nwrite-data=" + str(folder / "user")
                          + "\n[general]\ncheck-updates=false\n")
        command = [str(executable), "--config", str(config), "--mod-directory", str(mods),
                   "--check-unused-prototype-data"]
        if save is not None:
            command += ["--test-save", str(save), "--test-arg", "reload"]
        elif scenario is None:
            command.append("--dump-data")
        else:
            destination = folder / "user" / "scenarios" / "cr-check"
            destination.mkdir(parents=True)
            (destination / "control.lua").write_text(scenario)
            if server:
                (folder / "user/saves").mkdir(parents=True, exist_ok=True)
                server_settings = folder / "server-settings.json"
                server_settings.write_text(json.dumps({
                    "name": "Isolated Combat Reconfigured test", "description": "Local integration test",
                    "visibility": {"public": False, "lan": False}, "require_user_verification": False,
                    "auto_pause": False, "autosave_interval": 0}))
                command += ["--start-server-load-scenario", "cr-check", "--server-settings", str(server_settings),
                            "--bind", "127.0.0.1", "--port", "0"]
            else:
                command += ["--test-scenario", "cr-check"]
        output = execute(command, folder, folder / "user/saves/cr-existing.zip" if server else None)
        assert "Error while loading" not in output
        assert "Value ROOT.ammo-turret.gun-turret" not in output, output
        print("PASS", name, flush=True)
        if scenario is None and save is None:
            path = folder / "user" / "script-output" / "data-raw-dump.json"
            return json.loads(path.read_text())
        return output

    for expansion in [False, True]:
        suffix = "space-age" if expansion else "base"
        baseline = run("vanilla-" + suffix, False, expansion)
        defaults = run("defaults-" + suffix, True, expansion)
        assert defaults == baseline, "Default data must exactly match the official data"
    print("PASS exact default equality for every prototype (base and Space Age)", flush=True)

    overrides = {
        "range": 60, "min-range": 5, "prepare-range": 80, "cooldown": 0.5, "warmup": 3,
        "cooldown-deviation": 0.2, "damage-modifier": 2, "ammo-consumption-modifier": 0.5,
        "rotation-speed": 0.1, "preparing-time": 20, "folding-time": 25, "inventory-size": 4,
        "automated-ammo-count": 100, "prepare-with-no-ammo": False, "shoot-in-prepare-state": True,
        "start-attacking-only-when-can-shoot": True, "leave-attacking-if-shoot-fails": False,
        "can-retarget-while-starting-attack": True, "allow-turning-when-starting-attack": True,
        "range-mode": "center-to-bounding-box", "health-penalty": -10, "rotate-penalty": 2,
        "fire-penalty": 3, "threatening-asteroid-penalty": -30, "call-for-help-radius": 100,
        "max-health": 1000, "healing-per-second": 6, "repair-speed-modifier": 2,
        "is-military-target": False, "alert-when-attacking": False, "alert-when-damaged": False,
        "create-ghost-on-death": False, "circuit-wire-max-distance": 100, "mining-time": 0.2,
        "heating-energy": 25}
    for damage in ["physical", "impact", "poison", "explosion", "fire", "laser", "acid", "electric"]:
        overrides["resistance-" + damage + "-decrease"] = 3
        overrides["resistance-" + damage + "-percent"] = 25
    changed = run("all-settings", expansion=True, overrides=overrides)
    gun = changed["ammo-turret"]["gun-turret"]
    assert gun["attack_parameters"]["range"] == 60 and gun["attack_parameters"]["min_range"] == 5
    assert gun["preparing_speed"] == gun["preparing_speed_secondary"] == 0.05
    assert gun["folding_speed"] == gun["folding_speed_secondary"] == 0.04
    assert gun["healing_per_tick"] == 0.1 and gun["heating_energy"] == "25kW"
    assert gun["inventory_size"] == 4 and len(gun["resistances"]) == 8
    # Every setting must map to the intended field, without touching other prototypes.
    special = {"range", "min-range", "prepare-range", "preparing-time", "folding-time",
               "healing-per-second", "mining-time", "heating-energy"}
    for key, value in overrides.items():
        if key.startswith("resistance-"):
            _, damage, component = key.split("-")
            assert next(r for r in gun["resistances"] if r["type"] == damage)[component] == value
        elif key not in special:
            field = key.replace("-", "_")
            target = gun["attack_parameters"] if field in {
                "cooldown", "warmup", "cooldown_deviation", "damage_modifier", "ammo_consumption_modifier",
                "range_mode", "health_penalty", "rotate_penalty", "fire_penalty", "threatening_asteroid_penalty"
            } else gun
            assert target[field] == value, key
    assert gun["minable"]["mining_time"] == 0.2 and gun["prepare_range"] == 80
    changed["ammo-turret"]["gun-turret"] = baseline["ammo-turret"]["gun-turret"]
    assert changed == baseline
    base_heating = run("base-freezing-disabled", overrides={"heating-energy": 25})
    assert "heating_energy" not in base_heating["ammo-turret"]["gun-turret"]

    for expansion in [False, True]:
        extreme = run("range-10000-" + str(expansion), expansion=expansion,
                      overrides={"range": 10000})
        assert extreme["ammo-turret"]["gun-turret"]["attack_parameters"]["range"] == 10000
    clamped = run("reversed-range", overrides={"range": 10, "min-range": 20})
    assert clamped["ammo-turret"]["gun-turret"]["attack_parameters"]["min_range"] == 10
    edges = run("boundary-values", overrides={"range": 0, "cooldown": 0.001, "inventory-size": 65535,
        "automated-ammo-count": 4294967295, "warmup": 4294967295, "rotation-speed": 0,
        "preparing-time": 1, "folding-time": 1, "ammo-consumption-modifier": 0,
        "resistance-physical-percent": 100, "heating-energy": 0})
    assert edges["ammo-turret"]["gun-turret"]["inventory_size"] == 65535
    run("combat-and-quality", expansion=True, scenario=(ROOT / "tests" / "combat.lua").read_text())
    run("custom-combat", expansion=True, overrides={"range": 60, "damage-modifier": 2,
        "cooldown": 3, "inventory-size": 4, "max-health": 1000},
        scenario=(ROOT / "tests" / "combat.lua").read_text())
    run("zero-ammo-consumption", expansion=True, overrides={"ammo-consumption-modifier": 0},
        scenario=(ROOT / "tests" / "combat.lua").read_text())
    run("long-range-combat", overrides={"range": 1000},
        scenario=(ROOT / "tests" / "long-range.lua").read_text())
    if args.extreme_combat:
        run("extreme-range-combat", overrides={"range": 10000},
            scenario=(ROOT / "tests" / "long-range.lua").read_text())
    run("save-vanilla-turret", enabled=False,
        scenario=(ROOT / "tests" / "existing.lua").read_text(), server=True)
    saves = list((workspace / "save-vanilla-turret/user/saves").glob("*cr-existing*.zip"))
    assert len(saves) == 1, "Expected an isolated vanilla save"
    run("reload-existing-turret", overrides={"range": 60, "max-health": 1000, "inventory-size": 4},
        save=saves[0])
    print("All integration checks passed.", flush=True)
    if args.keep:
        print("Isolated test files:", workspace)


if __name__ == "__main__":
    main()
