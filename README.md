# Combat Reconfigured

**0.2.0 is an internal experimental version for Factorio 2.1.24.** It exposes native startup settings for the player weapons and combat facilities in the base game and Space Age. The MIT license, project identity and author are unchanged.

With Space Age enabled there are **2,348 settings across 128 configurable prototype records**. Base game registers **1,777 settings**, including feature-hidden controls. The original 51 gun turret setting identifiers are retained. This deliberately large catalog is intended for individual experiments and later selection, not a finalized public interface.

## Coverage

- All 17 native gun prototypes: eight handheld weapons, car/tank guns, four independent Spidertron launchers, and the shared artillery gun.
- All seven turrets: gun, laser, flamethrower, artillery, rocket, tesla and railgun.
- Car, tank, Spidertron and artillery wagon combat properties; land mines, walls and gates.
- Throwing capsules, grenades, combat robots, capture robots, personal laser/discharge equipment, shields and armor. Healing/buff consumables and cliff explosives are included; the two remotes have no separate numeric attack controls.
- All 17 ammunition prototypes and the player-combat resource graph: projectiles, beams, streams, fire, poison cloud, stickers and tesla chains.

The independent English [parameter inventory](PARAMETERS.md) lists every setting, exact native property path, default, units, meaning, resource consumers and exclusions. A record is a prototype, not necessarily a distinct weapon: for example, a grenade capsule and its projectile are separate records.

## Use

Copy `combat-reconfigured_0.2.0.zip` into the user data `mods` directory, enable the mod, and open **Settings → Mod settings → Startup**. Apply changes and restart when prompted. On macOS the usual location is `~/Library/Application Support/factorio/mods`. Keep only one installed copy of this mod active. Loading a save with its saved startup settings can restore older values.

Settings are organized by family and prototype. Their names use native translated item/entity names where available, followed by the property and nested path. English and Simplified Chinese labels/descriptions are supplied. Search by weapon name, property or resource identifier. Shared resources are marked **[shared]** / **[共享]**.

Defaults are exact no-ops: the mod does not write unchanged values or materialize optional fields. Native research, ammunition categories, entity identities and quality prototypes are retained. Settings modify existing and newly created entities through their original prototypes. There is no custom GUI, control script, per-tick scan, or new dependency.

## Mechanisms and dependencies

- Weapon-local damage and consumption coefficients stay local. Ammo item, projectile, beam, fire and sticker controls affect **all consumers** of that shared resource. These are separate, explicit settings; there are no silent copies or global ammo rewrites from a weapon setting. The inventory identifies direct consumers, including enemy/environmental users of shared effects when present.
- Laser/tesla/robot/equipment beam delivery limits live inside their attacks. Increasing an attack range raises an insufficient embedded beam length unless that length is explicitly configured. For a turret with an explicit preparation radius, a range increase also raises an insufficient preparation radius unless explicitly configured.
- Railgun targeting range and the shared ammunition's **line attack range** are independent. Change both when researching longer actual line attacks. Artillery turret and wagon share `artillery-wagon-cannon`; their manual range coefficients belong to each entity. Ammo range modifiers do not extend artillery range in the native engine.
- Flamethrower fluid supply, buffer size, activation threshold and consumption are separate controls. Crude/heavy/light oil damage coefficients are separate. Stream flight physics and shared ground-fire/sticker damage are distinct from turret attack coefficients.
- Tesla gun and turret have separate chain prototypes. Jump count, reach, delay and branching are configurable, including the native quality-dependent fork increment. No quality or research bonus is replaced by scripts.
- Reversed minimum/maximum attack ranges are clamped and logged. Initial fire lifetime is clamped to its maximum. Exponential projectile turning is kept disabled if acceleration remains zero. Negative sentinel values preserve native unlimited/disabled defaults. Explicit research choices such as a short beam limit or preparation radius take precedence over automatic extension.
- Freezing settings require the freezing feature; armor flight settings require space travel. Mech armor's flight flag is coupled to its native collision/drawing boxes and is not independently exposed. The fluid turret's engine-forced fuel check is omitted. Capsule warmup is omitted because nonzero capsule warmup is invalid.

## Experimental limits

Back up saves before changing inventory sizes; shrinking an inventory can discard items. Current health and ammunition in saved entities remain engine-managed. Native health-ratio preservation was tested on a saved gun turret.

Inputs use absolute values where possible: ticks, tiles, joules, watts, HP and inventory slots. Native coefficients are retained when the underlying mechanism needs them. Numeric guards follow documented widths/constraints, with positive floors for intervals and a million-tile spatial guard. These are not balance limits or performance guarantees. Huge ranges, radii, repeat counts and branches can exhaust memory/CPU. A prior 10,000-tile actual-map attempt exceeded the test runner's 2 GiB memory guard; successful prototype loading at that range does not prove playable operation.

The catalog deliberately does not alter prototype identifiers, visual/audio resources, masks, recipe/technology definitions, general production, transport movement engines, or enemy-only combat prototypes. Optional fields without a reliable independent scalar interpretation are documented rather than fabricated. Several native options have conditional effects depending on target type/state; a registered setting is not a promise that the condition always occurs.

## Validation

See [TESTING.md](TESTING.md) for the distinction between prototype checks and actual combat tests.

```sh
python3 tests/run.py
python3 tests/experimental.py
python3 tests/mechanisms.py
```

All tests use isolated mod/config/save directories and the installed Factorio 2.1.24 executable. Player saves and installed mods are not modified. No build commands or extra libraries are needed. `tests/run.py` accepts `--factorio` and `--data`; the additional catalog/mechanism checks currently target the macOS installation at `/Applications/factorio.app/Contents/MacOS/factorio`. Use `--keep /new/directory` on the regression/catalog runner to retain logs. The runners enforce a 60-second process timeout and 2 GiB resident-memory guard.

## Files and maintenance

- `prototypes/gun-turret-settings.lua`: retained original gun turret controls.
- `prototypes/catalog.lua`: explicit catalog entries, safe to prune individually.
- `settings.lua`: native startup registration and feature gating.
- `data-final-fixes.lua`, `prototypes/apply-catalog.lua`: changed-value-only application and dependency handling.
- `locale/en/`, `locale/zh-CN/`: names and descriptions.
- `PARAMETERS.md`: independent English inventory for later selection.
- `tests/`: regression scenarios and catalog mappings; `tests/catalog.json` is the readable test manifest.
- `scripts/catalog.py`: development-only catalog refresher using official dumps and matching API, not third-party mods. No build step is required to use or edit the committed catalog.

The refresher takes `--base`, `--space-age` and `--api` paths to official JSON exports. `temp/` is local reference material, ignored by Git and excluded from installation ZIPs. Only `changelog.txt` is maintained. This internal iteration is not automatically committed, pushed or published.

## Official references

- [Factorio API](https://lua-api.factorio.com/latest/index.html), matched to the local 2.1.24 offline API and installed official data.
- [Attack parameters](https://lua-api.factorio.com/latest/types/BaseAttackParameters.html), [ammo type](https://lua-api.factorio.com/latest/types/AmmoType.html), [fluid turrets](https://lua-api.factorio.com/latest/prototypes/FluidTurretPrototype.html), [artillery turrets](https://lua-api.factorio.com/latest/prototypes/ArtilleryTurretPrototype.html), and [tesla chains](https://lua-api.factorio.com/latest/prototypes/ChainActiveTriggerPrototype.html).
