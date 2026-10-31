# Combat Reconfigured 1.0.0 validation

Validated on **2026-10-31** with **Factorio 2.1.24, build 87808, mac-arm64**, official base/Space Age data and the matching offline API. The runner uses isolated mod, configuration and scenario directories. It does not read or modify player saves or installed mods. No build commands or extra dependencies are required.

## Prototype and settings checks

`python3 tests/run.py` checks both base game and official Space Age configurations:

- Every exported prototype is exactly equal to vanilla at default public settings, including absent optional fields.
- Base registers 63 public numeric startup settings; Space Age registers 87. The gun turret has exactly four. No hidden experimental settings are registered.
- Defaults, minimum/maximum bounds and native target paths are independently checked against vanilla exports. Every control is changed to a distinct test value (with integer/fractional exceptions where appropriate), and the full prototype export must match vanilla plus only the expected edits.
- All settings are loaded together at their minimum inputs, then at their maximum inputs. Shared Spidertron mutations must update all four launchers, and shared rotation mutations must update both artillery entities. Full export comparisons also cover the dependency edits needed for native beams, preparation, artillery ratios and energy buffers. This proves valid prototype loading, not high-load performance at all maxima.
- Additional isolated gun, laser, fluid, artillery, shared Spidertron, Tesla and railgun/shared-ammo edits verify their exact intended scope. English and Simplified Chinese locale sections/keys must match.
- Public entry points must not reference experiments. The editable [experimental edition](https://github.com/AaaRynt/combat-reconfigured/blob/master/experiments/README.md) has its own locale/completeness checks; public regression tests do not freeze its contents.
- Factorio's unused-prototype-data diagnostic is enabled during runs.

## Actual native combat

| Scenario | Observed behavior required |
| --- | --- |
| Gun turret, default and configured | Ammo and turret damage research multiply the configured coefficient; measured shot intervals retain shooting-speed research. Normal/rare/legendary inside/outside range tests retain quality bonuses. Inventory and normal/legendary health remain native. Ammo coefficient 0 preserves loaded ammunition. |
| Expanded weapon ranges | Laser, flamethrower and Tesla turrets hit targets at 45 tiles with range 50; both railguns hit at 60 with targeting 70 and shared line 80; pistol hits at 25 with range 30; handheld flamethrower hits at 20 with range 25; Tesla gun hits at 35 with range 40. Rocket turret, shotgun, rocket launcher and both artillery forms also deal actual damage. Thirteen cases total. |
| Ordinary input range ceiling | With normal quality and no research, a gun turret configured to range 256 hits at 250 tiles and does not hit at 270. |
| Artillery automatic/manual split | Turret and wagon configured to automatic 100/manual 300 hit automatically at 90. Separate targets at 200 receive no damage before native manual artillery flares are created, and are then hit. Targets at 320 remain unhit even after manual flares. |
| Artillery rotation | Measure native barrel orientation increments: one shared 90 degrees/s setting must apply to both turret and wagon. |
| Artillery damage radius | Both native turret and wagon shells hit targets offset 7 tiles from impact with radius 8, but not with default radius 4. Offset 12 remains outside both. Target collision boxes remain native. |
| Resource costs and weapon damage | Eleven cases measure native costs at positive and zero inputs; doubling each weapon coefficient must double its first damage event against a test target with resistances removed. |

Resource cases cover gun turret, pistol, laser turret, Tesla turret, railgun turret, flamethrower turret, handheld flamethrower, artillery turret, artillery wagon, Tesla gun and handheld railgun. The fixture appends a test-only instantaneous launch marker without replacing native attack actions. Single-round weapons fire twice; the others fire once. It then compares native inventory round counts, electric buffer debits (less idle drain) or fluid reservoir debits with the configured cost multiplied by measured launches.

Positive checks include doubled firearm/Tesla/flamethrower ammo cost, fractional **0.5** railgun/artillery ammo costs, laser **1.6 MJ**, Tesla turret **24 MJ**, railgun turret **20 MJ** and flamethrower turret **2 fluid units** per shot. Zero-cost checks retain loaded ammo/fluid and supplied energy, and double weapon damage coefficients. Native stream/fire behavior remains; the comparison uses the first damage event, not a claim of equal long-term damage against every target type.

The test supplies energy/fluid directly to isolate attacks and cost accounting. It does not validate an entire power or pipe network. Test markers, target resistance changes and scenario code are excluded from the public ZIP.

## Installation artifact

`scripts/package.py` creates a deterministic ZIP from exactly nine public files. It verifies every ZIP member and its bytes against source. The runner installs that ZIP into isolated mod directories and compares its default prototypes with vanilla in both base game and Space Age. Actual combat from the installed ZIP verifies base-game artillery automatic/manual targeting and Space Age gun research/quality behavior. The ZIP includes LICENSE, README and changelog alongside the game files. Experiments, tests, TESTING.md, scripts, temporary data, caches and Git metadata must not be shipped.

## Limits

These tests distinguish prototype mapping from actual combat evidence. Vehicle driving/aiming, all four Spidertron launchers in action, every supported weapon at every input limit, Tesla branching distributions, every quality/research combination, live UI presentation, multiplayer and large-factory UPS are not separately tested. No third-party mod compatibility is claimed.

Input ceilings are conservative product limits, not a guaranteed frame-rate or total-entity budget. Native research, quality and ammo modifiers are preserved and can exceed the effective range/rate implied by a base input limit. High firing rates and many chain effects can still be costly. The [experimental edition](https://github.com/AaaRynt/combat-reconfigured/blob/master/experiments/README.md)'s extreme-range experiments are not v1.0.0 performance evidence.

Switching from the research edition does not migrate its setting IDs. Review startup settings when switching editions; migration from every research configuration is not tested.

## Reproduce

Run these commands from the `mod/` source directory. From the repository root, prefix both script paths with `mod/`.

```sh
python3 tests/run.py --keep /new/test/directory
python3 scripts/package.py --output /path/to/combat-reconfigured_1.0.0.zip
```

The default executable is `/Applications/factorio.app/Contents/MacOS/factorio`; use `--factorio` and optional `--data` for other installations. Each process has a 60-second timeout and a 2 GiB resident-memory guard. Paths must point to matching official content.
