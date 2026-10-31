# Combat Reconfigured experimental edition

This editable research edition exposes **2,348 Space Age / 1,777 base startup settings** for Factorio 2.1.24, including the original 51 gun turret controls. Experimental metadata uses version **0.0.0** and an explicit experimental title. Its changes are tracked in `changelog.txt` as a single experimental edition.

Read the [parameter inventory](PARAMETERS.md) for setting IDs, native paths, defaults, units, shared consumers and exclusions, and the [validation notes](TESTING.md) for evidence and limitations. See the [public mod README](../README.md) for the supported release and the [public validation notes](../TESTING.md) for its separate checks.

## Files

- `prototypes/catalog.lua` holds all parameter definitions in one file. Its first section covers the original gun turret controls with their conversions; its generated section contains all additional catalog entries. They remain separate arrays inside the same module because the original controls include derived durations, regeneration units and sentinel conversions. No setting IDs are duplicated or removed.
- `locale/en/settings.cfg` and `locale/zh-CN/settings.cfg` each contain every name, description and string choice for that language.
- `settings.lua` registers these definitions; `data-final-fixes.lua` and `prototypes/apply-catalog.lua` apply changed values and native dependency repairs. Factorio's native entry points remain separate from the single parameter-definition file.
- `scripts/catalog.py` refreshes the generated section, test manifest and parameter inventory from matching official data/API exports. It preserves the handwritten gun turret section and merges generated locale text into the same per-language file. Supply `--base`, `--space-age` and `--api` paths; local reference exports are not included.
- `tests/` retains regression, mapping and real-combat scenarios. Definitions, documentation and tests are maintained together.

## Research use

Copy the contents of this directory to a separate development mod folder, then follow the [validation instructions](TESTING.md). Do not enable this experimental edition alongside the public mod: both intentionally use the same mod name. There is no public switch to load experimental code. Public entry points never import this directory, and the release ZIP excludes it, its tests and its generator. The project [MIT license](../LICENSE) applies.

## Scope and limits

The experiment includes guns, turrets, vehicle combat, ammunition, capsules, robots, equipment, armor, defenses and shared projectile/beam/stream/fire/sticker/chain effects. Weapon-local settings stay local; shared resource edits can affect multiple weapons and sometimes enemies or environmental effects. Inspect the [consumer inventory](PARAMETERS.md) before editing shared effects.

Exact vanilla defaults, prototype mappings and selected native combat mechanisms were checked in the original research. These do not prove every state/quality/research combination, multiplayer or large-factory performance. Extreme ranges and branching can exhaust CPU/memory; the million-tile experimental input ceiling is not a safety guarantee. A prior 10,000-tile map attempt exceeded the runner's 2 GiB memory guard. Public bounds and supported features are described separately in the [public README](../README.md).
