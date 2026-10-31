# Experimental edition validation

Validated on **2026-10-30 and 2026-10-31** with **Factorio 2.1.24, build 87808, mac-arm64**, official content and the matching offline API. Checks cover exact base/Space Age defaults, all 51 original gun turret controls, bounds/clamping, research/quality, zero ammo, long-range combat, existing-save reload and 15 native combat mechanisms. The refresher reproduces the catalog definitions and test manifest in an isolated copy, retaining all 2,348 entries in each language's locale file.

All runs use isolated config/mod/scenario/save directories. Player saves, installed mods and account credentials are not used. No build command or additional dependency is required. See the [experimental README](README.md), [parameter inventory](PARAMETERS.md) and [public validation notes](../TESTING.md).

## Exact defaults and registration

- All exported prototypes are exactly equal to vanilla with default settings, both in base and official Space Age configurations. This checks the entire exported prototype data, not just selected weapon numbers.
- Base game registers 1,777 settings; Space Age registers 2,348. Counts include feature-hidden freezing controls. All registered IDs, types and declared defaults are checked against the catalog.
- Every catalog setting has English and Simplified Chinese labels and descriptions. Native translated item/entity/equipment names are used where available, with a resource identifier fallback.
- The original 51 gun turret IDs and regression tests remain. Feature-only prototypes are not registered without their content. Armor flight requires space travel, and heating is gated by freezing.

## Modification and isolation checks

`tests/experimental.py` changes every additional catalog control, one prototype family per isolated game process, in both supported official content configurations. Each changed field is read back from the real engine export. The entire result is compared against vanilla plus the exact intended paths; unrelated fields and prototypes must be unchanged. Energy strings are compared as absolute J/W values. Resistance edits are checked by damage type.

The manifest records 28 base-versus-Space-Age structural path differences. These include action arrays whose indices or singleton/list representation differ. Mapping tests exercise the correct path for each mode rather than assuming the expansion data is identical to base data.

Dedicated checks also verify that:

- Increased laser range extends the embedded beam delivery limit without changing the shared beam prototype.
- Increased flamethrower range extends an insufficient preparation radius.
- Explicit beam length overrides take precedence over automatic extension.
- Reversed minimum range is clamped to maximum range, with a log.
- Fire initial lifetime is clamped to maximum lifetime.
- Factorio's unused-prototype-data diagnostics do not report unused catalog paths in the exercised configurations.

## Actual combat, separate from prototype checks

`tests/mechanisms.py` runs a 900-tick headless scenario and requires positive damage events from each of these 15 cases:

| Mechanism | Actual observation required |
| --- | --- |
| Laser turret | Hits a target 45 tiles away with configured range 50, beyond its vanilla range. |
| Flamethrower turret | Hits a target 45 tiles away with configured range 50, supplied with light oil. This also exercises preparation-range extension and stream travel. |
| Rocket turret | Fires loaded rocket items and damages its target. |
| Tesla turret | Hits a target 45 tiles away with configured range 50 using its native chain attack. |
| Railgun turret | Hits a target 60 tiles away with targeting range 70 and shared ammo line range 80. |
| Artillery turret | Automatically fires at and damages an enemy spawner. |
| Artillery wagon | Placed on rails, automatically fires at and damages an enemy spawner. |
| Defender robot | Acquires and damages an enemy target. |
| Pistol | A character fires loaded magazines at a target 25 tiles away with configured range 30. |
| Handheld railgun | A character fires the native line attack at a target 60 tiles away, using the configured gun and ammo ranges. |
| Shotgun | A character fires pellets and damages its target. |
| Rocket launcher | A character launches loaded rockets and damages its target. |
| Handheld flamethrower | A character consumes loaded flamethrower ammo and damages its target through streams/fire. |
| Land mine | Arms and damages a nearby enemy unit. |
| Personal laser equipment | Installed in a character's armor grid and supplied with energy, damages its target. |

Energy/fluid supply is maintained by the test scenario to isolate attack behavior. These tests prove actual target engagement and damage, not detailed power-network balance or measured fluid throughput.

The retained `tests/run.py` suite additionally verifies gun turret ammo/turret damage research multiplication, measured shooting-speed research, normal/rare/legendary range boundaries and health, inventory slots, and zero ammunition consumption. It saves a vanilla gun turret and reloads it with the mod enabled: unit identity, ammo and native health ratio are retained while new settings apply. It also checks 1,000-tile real combat and 10,000-tile prototype loading in base and Space Age.

## Limits and unverified behavior

- Not every catalog field has a dedicated behavioral combat assertion. The all-catalog suite proves registration, data-stage mapping and isolation; it must not be described as actual-combat verification of all 2,348 controls.
- Direct vehicle driving/aiming, every Spidertron launcher in combat, capsule throwing through the player UI, capture completion, poison-cloud balance, shield regeneration, discharge remote behavior, each resistance formula, and every state/quality/research combination are not separately validated in combat. Their applicable catalog mappings and engine loading are covered.
- The tests do not measure exact energy/flow consumption against a live power/pipe network, long-run performance, or behavior at every numeric extreme. Some settings intentionally affect a native conditional state which may not occur in a given scenario.
- Shared ammo/beam/fire/sticker changes can affect multiple weapon types, and sometimes enemies or environmental fire. Consumers and exact paths are listed in [the parameter inventory](PARAMETERS.md). This is explicit scope, not per-weapon isolation of a shared resource.
- A prior 10,000-tile actual-map attempt exceeded the runner's 2 GiB resident-memory guard during map initialization. Prototype loading at that range passed; playable operation at 10,000 or up to the million-tile input guard is not established. High repeat/branch counts can similarly exhaust resources.
- The settings screen has not been manually reviewed for scrolling/search performance with thousands of controls. Multiplayer clients and third-party mods are not tested. Only the local 2.1.24 engine is validated.
- Mech armor flight cannot be disabled independently of its collision/drawing boxes. Fluid turret fuel checks are forced by the engine. Nonzero capsule warmup is invalid. These options are omitted rather than presented as independent working controls.

## Reproduce

```sh
python3 tests/run.py
python3 tests/experimental.py
python3 tests/mechanisms.py
```

The macOS default executable is `/Applications/factorio.app/Contents/MacOS/factorio`. `tests/run.py` accepts `--factorio` and `--data`; the two additional test runners currently use that macOS installation. The regression/catalog runners accept `--keep /new/test/directory`. Each process has a 60-second timeout and 2 GiB resident-memory guard. The vanilla-save check uses a private loopback-only server on an assigned port.
