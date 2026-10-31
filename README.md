# Combat Reconfigured

Combat Reconfigured customizes the native player weapons and turrets in **Factorio 2.1**, with optional **Space Age** support. The repository contains two independent editions: a focused public mod and an unpublished research edition. Both keep native behavior at their default settings and provide English and Simplified Chinese in-game text.

| Edition | Status | Purpose |
| --- | --- | --- |
| [Public mod](https://github.com/AaaRynt/combat-reconfigured/blob/master/mod/README.md) | **1.0.0 — Initial public release** | 63 base / 87 Space Age startup settings for range, firing intervals, damage, resource costs and selected special weapon controls. |
| [Experimental edition](https://github.com/AaaRynt/combat-reconfigured/blob/master/experiments/README.md) | **Unpublished research** | 1,777 base / 2,348 Space Age settings, with the full parameter inventory, generator and research tests. Not a supported public release. |

## Repository layout

```text
mod/          Public mod, documentation, tests and packaging script
experiments/  Independent research edition, documentation, generator and tests
README.md     Project overview
LICENSE       Project MIT license
```

Each edition has its own metadata, README, license, prototypes, locale files and development resources. Neither loads code or files from the other. Follow the [public documentation](https://github.com/AaaRynt/combat-reconfigured/blob/master/mod/README.md) or [research documentation](https://github.com/AaaRynt/combat-reconfigured/blob/master/experiments/README.md) for its scope, settings and validation limits.

## Installation

For normal play, use **`combat-reconfigured_1.0.0.zip`**. Copy it without extracting into Factorio's user-data `mods` directory, enable Combat Reconfigured, and configure **Settings → Mod settings → Startup**. On macOS the usual location is `~/Library/Application Support/factorio/mods`.

**Install only one edition.** Both intentionally use the internal mod name `combat-reconfigured`, so they cannot be installed together or used as add-ons to each other. Remove the other edition and any duplicate copies from the selected mods directory before switching. Separate Factorio user-data/mod directories can be used for research. Review startup settings when switching editions; research settings are not automatically migrated to the public interface.

The public ZIP excludes experiments, tests, development scripts, local reference exports and Git metadata. Its license is included. Cross-edition documentation links use GitHub URLs so they remain usable when only one edition is downloaded.

## Development

From the repository root, with a matching installed Factorio 2.1.24:

```sh
python3 mod/tests/run.py
python3 mod/scripts/package.py --output /path/to/combat-reconfigured_1.0.0.zip
```

No build framework or additional dependencies are needed. The [public validation notes](https://github.com/AaaRynt/combat-reconfigured/blob/master/mod/TESTING.md) describe source checks and actual loading/combat tests from the installation ZIP. The [experimental validation notes](https://github.com/AaaRynt/combat-reconfigured/blob/master/experiments/TESTING.md) cover the separate research tools.

The project and both editions use the MIT license. See [LICENSE](LICENSE).
