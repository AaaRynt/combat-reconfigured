# Combat Reconfigured

Version **0.1.0** customizes the **existing vanilla gun turret** through Factorio's native startup settings. It targets **Factorio 2.1**, with **2.1.24** as the minimum tested version. The [MIT license](./LICENSE) and project author, Astro704, are preserved.

There are 51 settings, with English and Simplified Chinese names and descriptions. The freezing setting is hidden when the freezing feature is unavailable. No new turret, item, recipe, technology, custom UI, runtime script, or external dependency is added.

## Installation and use

1. Put `combat-reconfigured_0.1.0.zip`, or the source files in a folder named `combat-reconfigured_0.1.0`, in your Factorio `mods` directory. Do not put the whole repository, `temp/`, or the test files there.
2. Enable Combat Reconfigured, then open **Settings → Mod settings → Startup**.
3. Change the **Gun turret** settings, apply them, and restart when prompted. Load your save with the new startup settings; syncing settings from an older save can restore its previous values.

Defaults preserve vanilla behavior exactly: 18-tile range, 6-tick shot interval (10 shots/s before research), 400 HP, one ammunition slot, and an inserter supply target of 10 magazines. Values are absolute unless the engine property itself is a coefficient. One second is 60 game ticks.

Startup changes apply to the existing `gun-turret` prototype, including turrets already placed in saves. Existing health, ammunition and circuit settings are handled by the engine. Back up saves before reducing ammunition inventory slots: removed slots can lose their contents. Increasing maximum health does not explicitly heal existing turrets.

## Settings

All keys below have the prefix `cr-gun-turret-`. Numbers are base values before native quality and research effects.

| Key | Default | Meaning and accepted range |
| --- | --- | --- |
| `range` | 18 | Maximum attack range in tiles; 0–1,000,000. |
| `min-range` | 0 | Minimum targeting distance in tiles; 0–1,000,000. Clamped to maximum range if larger, with a log message. |
| `prepare-range` | -1 | Preparation radius in tiles; negative values preserve automatic native behavior, nonnegative values set an explicit radius up to 1,000,000. |
| `cooldown` | 6 | Ticks between shots; 0.001–4,294,967,295. Base shots/s = 60 / cooldown. Values below 1 permit multiple shots per tick. |
| `warmup` | 0 | Native delay between a shooting order and firing; integer ticks, 0–4,294,967,295. |
| `cooldown-deviation` | 0 | Native random shot-interval deviation; 0–1. |
| `damage-modifier` | 1 | Native damage coefficient applied to the loaded ammunition; nonnegative. |
| `ammo-consumption-modifier` | 1 | Native ammunition consumption coefficient per shot; nonnegative. 1 means one round, not one magazine. 0 still requires loaded ammunition. |
| `rotation-speed` | 0.015 | Turns per tick; 0–1. 0 prevents turning. Both native rotation variants change together. |
| `preparing-time` | 12.5 | Preparation duration in ticks; 1–4,294,967,295. Converted to `preparing_speed = 1 / time`, for both speed variants. |
| `folding-time` | 12.5 | Folding duration in ticks; same limits and conversion as preparation. |
| `inventory-size` | 1 | Ammunition slots; integer, 1–65,535. Capacity also depends on ammo item stack sizes. |
| `automated-ammo-count` | 10 | Inserter ammunition supply target in items; integer, 0–4,294,967,295, subject to inventory capacity. |
| `prepare-with-no-ammo` | true | Permit preparation without ammunition. |
| `shoot-in-prepare-state` | false | Permit native firing in the preparation state. |
| `start-attacking-only-when-can-shoot` | false | Require ammunition before entering the starting-attack state. |
| `leave-attacking-if-shoot-fails` | true | Leave attacking state when a shot fails. |
| `can-retarget-while-starting-attack` | false | Permit retargeting while starting an attack. |
| `allow-turning-when-starting-attack` | false | Permit turning while starting an attack. |
| `range-mode` | center-to-center | Native range calculation: `center-to-center`, `bounding-box-to-bounding-box`, or `center-to-bounding-box`. |
| `health-penalty` | 10 | Signed target scoring coefficient; positive prefers lower health ratios, negative prefers higher ratios. |
| `rotate-penalty` | 0 | Signed target scoring coefficient; higher values discourage targets requiring more rotation. |
| `fire-penalty` | 0 | Signed target scoring coefficient; positive prefers targets without fire-spreading stickers. |
| `threatening-asteroid-penalty` | -20 | Signed target scoring coefficient; negative prefers threatening asteroids. |
| `call-for-help-radius` | 40 | Native help radius in tiles; 0–1,000,000. Does not extend another turret's attack range. |
| `max-health` | 400 | Base maximum HP; at least 1. |
| `healing-per-second` | 0 | Signed HP/s; divided by 60 for `healing_per_tick`. Negative values cause passive health loss. Slow healing is applied once per second by the engine. |
| `repair-speed-modifier` | 1 | Native repair tool speed coefficient; nonnegative. |
| `is-military-target` | true | Make the turret a high-priority military target for enemies. |
| `alert-when-attacking` | true | Enable native attack alerts. |
| `alert-when-damaged` | true | Enable native damage alerts. |
| `create-ghost-on-death` | true | Permit native ghost creation, subject to the force's normal rules. |
| `circuit-wire-max-distance` | 9 | Circuit wire reach in tiles; 0–1,000,000. The other endpoint also limits the connection. |
| `mining-time` | 0.5 | Base mining time in seconds; nonnegative. |
| `heating-energy` | -1 | Heating requirement in kW. Negative values preserve official defaults: 0 in base, 50 with Space Age. 0 disables freezing. Visible and applied only with the freezing feature enabled. |
| `resistance-TYPE-decrease` | 0 | Flat incoming damage reduction; nonnegative. One setting for each of the eight damage types below. |
| `resistance-TYPE-percent` | 0 | Incoming damage resistance, 0–100%; 100 grants immunity. One setting for each damage type below. |

Resistance types: `physical`, `impact`, `poison`, `explosion`, `fire`, `laser`, `acid`, and `electric`. Their flat and percentage components use the native resistance formula; they do not alter outgoing bullet damage.

Unspecified floating-point upper bounds in the table are bounded by the prototype float representation (`3.402823466e38`). Time and count limits use the documented native integer widths where applicable; cooldown uses a uint32-sized time guard, with a positive 0.001-tick floor to exclude zero and effectively unbounded firing loops. Duration floors avoid zero division and preserve at least one simulation tick. Numeric acceptance does not guarantee useful gameplay or adequate performance at every extreme.

## Native mechanics and limits

- At default settings the mod does not write any turret properties, preserving explicit values, implicit engine defaults, and official expansion changes.
- The original entity name and `bullet` ammunition category are retained. Ammo damage research, gun turret damage research, and bullet shooting speed research continue to work. Quality continues to affect the attributes that vanilla actually supports, including turret range and health. This mod does not invent additional research or quality bonuses. Vanilla has no gun turret range research.
- Damage remains ammunition-dependent, so damage and ammo consumption use the engine's coefficients rather than a misleading fixed HP-per-shot value. Magazine size, ammo stack size and ammo actions are shared with other weapons and are not changed.
- The preparation and folding duration inputs use the documented reciprocal speed relationship. Actual transitions occur on whole simulation ticks. The firing animation speed is visual and is not a separate rate-of-fire control. The vanilla gun turret has no separate starting/ending attack animations, so their animation timing fields are not exposed.
- Target masks, ammo categories, projectile creation geometry, collision boxes, graphics, sounds, electrical energy sources and moving-unit properties are not exposed. They are resource choices, shared behavior, visual fields, or unsuitable independent controls for this turret. Full-circle turning is retained; arbitrary attack arcs are not exposed because the engine clamps arcs between half and full circles and a directional base would change placement behavior.
- Startup settings are global for the loaded game, not per turret. A data-stage mod cannot directly change the current ammunition or health of individual saved entities. No per-tick script or entity replacement is used.
- The spatial setting ceiling of 1,000,000 tiles is a configuration guard, not a documented engine maximum or a safe operating promise. It allows 10,000 and much larger values without a balance cap. Huge ranges can make native target searches and loading expensive; quality can increase the effective range further. See the [user report of memory exhaustion at very large turret ranges](https://mods.factorio.com/mod/Turret_Range_Buff_Updated/discussion/68d9211df31a27afb6fa89b7). To recover from a bad startup configuration, disable this mod or back up and remove `mod-settings.dat` from your mods directory, then restore reasonable settings.
- Only the vanilla gun turret and official game data are supported. Other weapons and third-party mod compatibility are outside v0.1.0.

## Validation and development

No build step or added dependency is required. Run the isolated integration checks with Python 3 and your installed Factorio executable:

```sh
python3 tests/run.py --factorio /Applications/factorio.app/Contents/MacOS/factorio
```

For other installations, pass `--data /path/to/factorio/data`. `--keep /path/to/new-test-directory` retains the temporary configurations and logs for inspection. The runner creates its own mod directory and test saves; it does not use player saves or installed mods. Each game process has a 60-second timeout and a 2 GiB resident-memory guard.

The integration suite compares every prototype against unmodified base and Space Age data, exercises all settings, checks range clamping and representative boundaries, loads a 10,000-tile range with and without Space Age, and tests combat, research, quality range/health and ammunition inventory in actual headless scenarios. A 1,000-tile combat scenario hits a target 990 tiles away. A separate save/reload check enables the mod on a previously saved vanilla turret, preserving its identity, ammunition and native health ratio while applying the new parameters. See [TESTING.md](TESTING.md) for results and limits.

The optional `--extreme-combat` check attempts actual 10,000-tile combat. In the release investigation, this attempt exceeded the 2 GiB memory guard during map initialization and was terminated. Prototype loading at 10,000 tiles passed; playable operation at that range has **not** been validated. The default suite excludes this known resource-intensive attempt.

Source layout: `settings.lua` registers settings; `prototypes/gun-turret-settings.lua` defines the gun turret options; `data-final-fixes.lua` applies changes; `locale/` contains translations; `tests/` contains development checks. `temp/` is ignored local reference material and must never be committed or included in a release archive. The original code of reference mods is not distributed.

## References

- [Factorio 2.1.24 prototype API](https://lua-api.factorio.com/latest/index.html), matched against the offline 2.1.24 API and locally installed official data.
- [AmmoTurretPrototype](https://lua-api.factorio.com/latest/prototypes/AmmoTurretPrototype.html), [TurretPrototype](https://lua-api.factorio.com/latest/prototypes/TurretPrototype.html), and [BaseAttackParameters](https://lua-api.factorio.com/latest/types/BaseAttackParameters.html).
- [QualityPrototype](https://lua-api.factorio.com/latest/prototypes/QualityPrototype.html) and [native mod settings](https://wiki.factorio.com/Tutorial:Mod_settings).
- Reference designs reviewed: [Long Range Turret 2.0](https://mods.factorio.com/mod/LR_Turret_2) and [Turret Range Buff 2.0](https://mods.factorio.com/mod/Turret_Range_Buff_Updated). Their source files and archives remain local references only.
