# v0.1.0 validation

Checked on 2026-10-30 with the installed **Factorio 2.1.24 (build 87808, mac-arm64)** and the matching official offline prototype/runtime API. No build commands were run. The tests use Python's standard library and isolated game configurations, mod directories, scenarios and saves. They do not modify player saves or installed mods.

## Passed

| Check | Evidence |
| --- | --- |
| Base defaults | Every exported prototype exactly equals an unmodified base-game run. |
| Space Age defaults | Every exported prototype exactly equals an unmodified run with the official expansion mods. |
| Settings and localization | All 51 settings have matching English and Simplified Chinese names and descriptions; every nondefault setting is mapped to its intended field. |
| Scope | With all settings changed, every prototype except the existing `gun-turret` still exactly matches the official data. No replacement entities are created. |
| Feature gating | Heating changes load correctly with freezing enabled and are ignored without it. The setting is hidden without the freezing feature. |
| Large-range data loading | 10,000-tile range loads and exports successfully with base and Space Age. |
| Long-range combat | A 1,000-tile turret acquires and hits a target 990 tiles away in an actual headless scenario. |
| Range conflict | Minimum range 20 with maximum range 10 is clamped to 10 and logged. |
| Representative boundaries | Engine loading accepts range 0, cooldown 0.001, 65,535 ammo slots, uint32 maximum insertion count and warmup, zero rotation, 1-tick preparation/folding, zero consumption, 100% physical resistance and zero heating. |
| Default and modified combat | Normal and customized turrets fire; base bullet damage is multiplied by the configured coefficient, ammo damage research, and turret damage research. Measured firing intervals follow shooting-speed research. |
| Quality | Normal, rare and legendary turrets engage targets inside their native quality-adjusted ranges and leave targets beyond their ranges untouched. Health scales with native quality. |
| Ammunition | Configured inventory slot counts are present on created entities. Zero-consumption turrets fire without consuming loaded rounds. |
| Existing save | A vanilla turret saved without the mod is reloaded with range 60, health 1,000 and four ammo slots. The same entity/unit number remains, seven magazines are retained, the new parameters apply, and native health-ratio preservation is confirmed. |
| Unused fields | Factorio's unused-prototype-data check reports no unused gun-turret fields in the exercised configurations. |
| Repository hygiene | Git whitespace checks pass; `temp/`, reference mods, ZIPs and Python caches are excluded from the commit and release package. |
| Release archive | The ZIP contains only 10 allowlisted release files, passes its CRC check, loads in Factorio, and exports data exactly equal to the vanilla base defaults. |

## Resource limit encountered

An additional **10,000-tile actual-combat attempt** exceeded the runner's **2 GiB resident-memory guard during map initialization** and was stopped before combat assertions ran. Successful prototype loading does not establish that this range is practical in a playable save. The default suite therefore uses 1,000 tiles for actual long-range combat and keeps the 10,000-tile combat attempt behind `--extreme-combat`.

The setting still accepts ranges up to the documented configuration guard of 1,000,000 tiles, as requested for broad configurability. Values above 10,000 were not run in an actual map. The guard is not the engine's formal maximum and does not make large spatial queries safe. Quality can increase the effective range further. There is no custom scanning or runtime workaround that hides these engine costs.

## Not verified

- Manual visual inspection of the settings screen or range overlays, and multiplayer client synchronization.
- Long-running performance in a large player factory, all possible setting combinations, or the full floating-point range.
- Dedicated behavioral assertions for every native state toggle, fractional ammo accounting, regeneration, inserter supply limits, freezing, circuit connections, mining, repair and each resistance formula. Their settings, field mappings and prototype loading were checked; the corresponding native game mechanisms are retained.
- Compatibility with third-party mods or Factorio versions other than the installed 2.1.24. These are outside this release's validation scope.

## Reproduce

```sh
python3 tests/run.py --factorio /Applications/factorio.app/Contents/MacOS/factorio
```

For another installation, add `--data /path/to/factorio/data`. To retain logs and temporary files, use `--keep /path/to/a/new-directory`. The save test starts a private server bound to loopback on an automatically assigned port and stops it after the isolated save is written.

Each process has a 60-second timeout and a 2 GiB resident-memory guard. The standard suite must finish with `All integration checks passed.`. The optional `--extreme-combat` run is expected to encounter the reported resource limitation on some systems and is not a release pass criterion.
