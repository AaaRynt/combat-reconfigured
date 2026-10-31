# Combat Reconfigured

**v0.3.0** provides focused startup settings for the existing guns and turrets in **Factorio 2.1**, with optional **Space Age** support. Validated with Factorio **2.1.24**. English and Simplified Chinese setting names and explanations are included.

The public interface has **63 settings in base game / 87 with Space Age** across 15 / 20 weapon configuration groups. Most weapons have four controls: maximum range, shot interval, damage coefficient and the appropriate resource cost. The gun turret has **exactly these four**. Space Age-only controls are absent without the expansion.

Compared with v0.2.0, the public interface is reduced from 1,777 / 2,348 experimental settings to the focused controls above. Spidertron uses one shared launcher group, and artillery turret/wagon settings are shared. Broad entity and combat-effect controls remain available only in the [experimental edition](experiments/README.md). See [upgrade guidance](#upgrade-from-v020) for setting-ID changes.

## Install and configure

Copy `combat-reconfigured_0.3.0.zip` into Factorio's user-data `mods` directory. On macOS this is normally `~/Library/Application Support/factorio/mods`. Keep one installed copy of Combat Reconfigured. Enable it, then use **Settings → Mod settings → Startup** and restart when prompted. The game may offer to synchronize startup settings with a save; check the resulting values after synchronization.

Defaults leave **every vanilla prototype unchanged**. Changed values are base values, applied through the native prototypes. Research, quality and ammunition effects continue to work. There is no runtime script, per-tick scan, new entity, recipe or technology.

## Supported weapons and defaults

Range is in tiles; interval is in ticks (60 ticks = 1 second). Damage is the weapon's native coefficient. Resource costs are per shot; ammo values are coefficients, fluid values are units, and energy values below are shown in MJ for readability. The settings screen takes energy in **J**, where 1 MJ = 1,000,000 J.

| Weapon                                      | Range | Interval | Damage | Resource cost    |
| ------------------------------------------- | ----: | -------: | -----: | ---------------- |
| Gun turret                                  |    18 |        6 |      1 | Ammo 1           |
| Laser turret                                |    24 |       40 |      2 | 0.8 MJ           |
| Flamethrower turret                         |    30 |        4 |      1 | Fluid 0.2        |
| Rocket turret (Space Age)                   |    36 |      120 |      1 | Ammo 1           |
| Tesla turret (Space Age)                    |    30 |      120 |      1 | 12 MJ            |
| Railgun turret (Space Age)                  |    40 |      170 |      1 | Ammo 1 and 10 MJ |
| Pistol                                      |    15 |       15 |      1 | Ammo 1           |
| Submachine gun                              |    18 |        6 |      1 | Ammo 1           |
| Shotgun                                     |    15 |       40 |      1 | Ammo 1           |
| Combat shotgun                              |    15 |       30 |    1.5 | Ammo 1           |
| Rocket launcher                             |    36 |       60 |      1 | Ammo 1           |
| Handheld flamethrower                       |    15 |        1 |      1 | Ammo 1           |
| Handheld railgun (Space Age)                |    40 |      120 |      1 | Ammo 1           |
| Tesla gun (Space Age)                       |    24 |       60 |      1 | Ammo 1           |
| Car machine gun                             |    20 |        4 |      1 | Ammo 1           |
| Tank machine gun                            |    20 |        4 |      1 | Ammo 1           |
| Tank cannon                                 |    30 |       90 |      1 | Ammo 1           |
| Tank flamethrower                           |     9 |        1 |      1 | Ammo 1           |
| Artillery turret and wagon (shared gun)     |   224 |      200 |      1 | Ammo 1           |
| Spidertron launchers 1–4 (one shared group) |    36 |       60 |      1 | Ammo 1           |

Special controls include shared artillery turret/wagon rotation speed, a shared artillery shell damage radius, artillery manual range (default **560**), Tesla chain jumps (turret **10**, handheld **12**) and the shared railgun ammunition line length (**50**). Railgun turrets expose both ammunition and electrical cost. All artillery controls affect turret and wagon together, including one shared cannon rotation setting. Shared shell damage radius defaults to 4 tiles. The shared cannon rotation input defaults to 21.6 degrees/second (0.001 turns/tick).

Grenades, capsules, land mines, combat robots, equipment, armor, walls and general vehicle properties have no public controls. Health, regeneration, resistances, repair, general rotation controls (except artillery), preparation timing, alerts, targeting scores, effect physics and visual controls have been removed. Their original behavior remains enabled.

## Input limits

The settings screen enforces inclusive bounds and shows them in each description. Limits apply to **base inputs**, before native bonuses.

| Parameter                                   |                  Minimum |                Maximum |
| ------------------------------------------- | -----------------------: | ---------------------: |
| Ordinary targeting range                    | Native minimum range + 1 |              256 tiles |
| Artillery automatic range                   |                       33 |            1,024 tiles |
| Artillery manual range                      |                       33 |            4,096 tiles |
| Shared railgun line length                  |                        1 |              256 tiles |
| Shot interval                               |                   1 tick |            3,600 ticks |
| Damage coefficient                          |                        0 |                     10 |
| Ammo coefficient, single-round magazines    |                        0 |                      1 |
| Ammo coefficient, other supported magazines |                        0 |                     10 |
| Flamethrower turret fluid/shot              |                        0 |               10 units |
| Electrical energy/shot                      |                        0 | 100,000,000 J (100 MJ) |
| Tesla chain jumps                           |                        1 |                     16 |
| Artillery cannon rotation speed (shared)    |               1 degree/s |          360 degrees/s |
| Shared artillery shell damage radius        |                0.5 tiles |               32 tiles |

Unchanged blind spots give these ordinary range floors: flamethrower turret **7**, rocket turret **16**, railgun turret **4.5**, handheld/tank flamethrower **4**, tank cannon **6**, all remaining ordinary weapons **1** tile. Single-round consumers are rockets, cannon shells, artillery shells and railgun ammunition. Native per-shot debits are capped at magazine size; an ammo coefficient above 1 would not reliably spend multiple single-round items per shot, so it is not offered.

Range, firing frequency and chain effects can increase CPU/memory use. These bounds reduce extreme inputs; they are not a measured large-factory performance guarantee. A 256-tile circle is about 202 times the area of an 18-tile circle. Native quality/research/ammo bonuses can take effective range above an input ceiling and can reduce effective intervals below one tick. Numerous fast-firing turrets can still be expensive. Increase range, rate and jumps gradually when testing an existing factory.

## Meaning and interaction of settings

1. **Startup values replace the corresponding base values.** They are not multipliers on every vanilla number. A damage coefficient of 1 is not neutral for the laser turret (default 2) or combat shotgun (default 1.5). A smaller interval means faster fire; 6 ticks gives a base 10 shots/s, while 60 ticks gives 1 shot/s. Actual rates also depend on power, ammo, turning, preparation and native reloading.
2. **Native bonuses apply afterward.** Weapon damage coefficients combine with native ammo/actions, research and relevant quality effects; target resistances still apply. No fixed final damage or global override is imposed. A zero damage coefficient does not disable firing or native non-damage effects. Native ammo range/cooldown modifiers remain; ammo range modifiers do not extend artillery in this engine.
3. **Local settings stay local.** Gun/turret settings do not rewrite shared projectile, beam, stream or ammo damage. A turret range increase extends an insufficient embedded beam limit and explicit preparation radius only on that turret. Increasing an electrical shot cost expands only that turret's energy buffer when necessary, preserving vanilla headroom. Input power, idle drain and flow limits stay unchanged; sustained fire can become power-limited.
4. **Artillery is explicitly shared.** Both turret and wagon use the configured automatic range, interval, damage and ammo cost. Manual range is an independent absolute base input; changing automatic range alone keeps the base manual input at 560. The mod derives both entities' native manual-range ratio. Manual range may be below automatic range. Native research/quality continue to modify the resulting behavior. The turret and wagon share one cannon rotation control in degrees/second (1-360, default 21.6); it does not change shot intervals, post-shot turning delay, parking or wagon travel. The shared shell radius (0.5-32, default 4 tiles) changes both physical and explosion damage coverage for both entities. It is a radius, not diameter. Visual effects, map reveal and damage per target remain unchanged. Radius 32 covers 64 times the area of vanilla radius 4, potentially affecting more entities and increasing CPU work and native collateral damage.
5. **Railguns have two distance limits.** Each railgun has its own targeting range; the explicit shared ammunition line-length setting affects both handheld and turret railguns. To engage at 70 tiles, set the relevant targeting range and shared line length to at least 70. Quality range alone does not rewrite that line length. The line can also hit entities along its path according to native rules.
6. **Resources use native accounting.** Ammo 1 generally means one round, not an entire magazine; 0.5 means reduced expenditure, including one single-round item per two shots. Ammo 0 still needs compatible ammunition loaded. Fluid cost is per shot, not per second; native fuel checks and oil damage bonuses remain. Energy cost is J/shot, not idle watts; zero shot cost does not remove idle drain. Shot costs do not create supplies or change loading requirements.
7. **Spidertron uses one shared group.** Range, interval, damage coefficient and ammo coefficient each apply to all four native launchers. Interval is per launcher and ammo cost is per shot, not a combined total for the vehicle. Other rocket weapons remain independent.
8. **Tesla chains remain separate.** Each Tesla setting edits only its own chain's maximum jumps. Native jump reach, branching and quality-dependent forking remain, so this value is not a guaranteed total number of unique targets.

There are no global enable switches, category overrides or hidden experimental fallbacks. Unchanged settings do not write optional native fields. Third-party mod compatibility is outside the supported scope.

## Upgrade from v0.2.0

Only the four core `cr-gun-turret-*` identifiers are retained from its gun turret interface. Other public identifiers use `cr-<weapon>-<parameter>`; experimental long-path IDs have been removed. Old experimental settings are not migrated to new fields. Review startup settings after upgrading; removed fields return to native behavior and changed IDs start at public defaults unless configured.

The [experimental edition](experiments/README.md) retains the full research parameter set, generator and tests in one editable directory. One catalog file defines all experimental parameters, with one locale file per language. See its [parameter inventory](experiments/PARAMETERS.md) and [validation notes](experiments/TESTING.md). Public entry points never import it, and the release ZIP excludes experiments, tests, scripts and local references.

## Validation and packaging

See [TESTING.md](TESTING.md) for checks and their limits. No build commands or additional dependencies are required.

```sh
python3 tests/run.py
python3 scripts/package.py --output /path/to/combat-reconfigured_0.3.0.zip
```

The test runner accepts `--factorio`, `--data` and `--keep /new/directory`. Packaging uses an explicit allowlist. `prototypes/weapons.lua` defines public inputs; `settings.lua` registers them; `data-final-fixes.lua` applies changed values only. Only `changelog.txt` is maintained.

## Official references

Validated against the installed official data and matching 2.1.24 API: [attack parameters](https://lua-api.factorio.com/latest/types/BaseAttackParameters.html), [ammo types](https://lua-api.factorio.com/latest/types/AmmoType.html), [artillery turrets](https://lua-api.factorio.com/latest/prototypes/ArtilleryTurretPrototype.html), and [Tesla chains](https://lua-api.factorio.com/latest/prototypes/ChainActiveTriggerPrototype.html), [artillery wagons](https://lua-api.factorio.com/latest/prototypes/ArtilleryWagonPrototype.html), and [area triggers](https://lua-api.factorio.com/latest/types/AreaTriggerItem.html).
