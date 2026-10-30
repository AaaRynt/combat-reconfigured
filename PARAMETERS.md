# Combat Reconfigured experimental parameter inventory

Official source: Factorio 2.1.24 base + Space Age prototype dumps and matching API. All defaults are no-ops. Native research/quality remain active. Paths with numeric components use Lua one-based array indices. Energy settings use absolute joules or watts; 60 ticks = one second.

## Retained gun turret controls

The original 51 `cr-gun-turret-*` settings remain unchanged. The additional catalog avoids overlapping their paths.

| Setting | Default | Meaning |
| --- | --- | --- |
| `cr-gun-turret-range` | 18 | Base maximum attack range before quality bonuses. Default: 18. Very large ranges can consume substantial memory and CPU; the setting limit is not a safety guarantee. |
| `cr-gun-turret-min-range` | 0 | Base minimum targeting distance. Default: 0. Values above the maximum range are clamped to the maximum and logged. |
| `cr-gun-turret-prepare-range` | -1 | Negative values preserve the native automatic preparation range, which follows attack range. Nonnegative values set an explicit preparation radius. Default: -1. |
| `cr-gun-turret-cooldown` | 6 (10 shots/s) | Base ticks between shots. 60 ticks = 1 second; shots per second = 60 / interval before research. Default: 6 (10 shots/s). Values below 1 permit multiple shots per tick. Minimum: 0.001 to exclude zero and unbounded firing loops. |
| `cr-gun-turret-warmup` | 0 | Native attack warmup: ticks between a shooting order and the shot. Separate from raising the turret. Default: 0. |
| `cr-gun-turret-cooldown-deviation` | 0 (no random deviation) | Native random cooldown deviation, from 0 to 1. Default: 0 (no random deviation). |
| `cr-gun-turret-damage-modifier` | 1 | Native turret damage coefficient applied to the loaded ammunition. Default: 1. Ammo damage and turret damage research still apply. This is a coefficient because damage depends on the ammunition. |
| `cr-gun-turret-ammo-consumption-modifier` | 1 (one round, not one magazine) | Native ammunition consumption coefficient. Default: 1 (one round, not one magazine). 0 permits firing without consuming loaded ammunition; ammunition must still be present. Fractional values use engine accounting. |
| `cr-gun-turret-rotation-speed` | 0.015 | Absolute turns per tick. Default: 0.015. 0 prevents rotation; 1 is one full turn per tick. A changed value applies to both native rotation variants. |
| `cr-gun-turret-preparing-time` | 12.5 | Native preparation duration = 1 / preparing_speed. Default: 12.5 ticks (speed 0.08). Minimum: 1 tick. Both speed variants change together. Actual transitions occur on whole game ticks. |
| `cr-gun-turret-folding-time` | 12.5 | Native folding duration = 1 / folding_speed. Default: 12.5 ticks (speed 0.08). Minimum: 1 tick. Both speed variants change together. |
| `cr-gun-turret-inventory-size` | 1 | Number of ammunition inventory slots, not rounds or magazine size. Default: 1. Capacity also depends on ammunition stack sizes. Reducing slots can discard stored ammunition; back up saves first. |
| `cr-gun-turret-automated-ammo-count` | 10 magazines | Native number of ammunition items inserters try to supply. Default: 10 magazines. Limited by inventory capacity; does not change magazine size or item stack size. |
| `cr-gun-turret-prepare-with-no-ammo` | enabled | Allow the native turret preparation state without loaded ammunition. Default: enabled. |
| `cr-gun-turret-shoot-in-prepare-state` | disabled | Allow native firing in the preparation state. Default: disabled. |
| `cr-gun-turret-start-attacking-only-when-can-shoot` | disabled | Check ammunition availability before entering the starting-attack state. Default: disabled. This does not remove ammunition requirements for firing. |
| `cr-gun-turret-leave-attacking-if-shoot-fails` | enabled | Native behavior when a shot fails, such as running out of ammunition. Default: enabled. |
| `cr-gun-turret-can-retarget-while-starting-attack` | disabled | Allow native retargeting while starting an attack. Default: disabled. Effect depends on the native state transitions; no extra animation is added. |
| `cr-gun-turret-allow-turning-when-starting-attack` | disabled | Allow native rotation while starting an attack. Default: disabled. |
| `cr-gun-turret-range-mode` | center-to-center | Native range distance calculation. Default: center-to-center. Other modes account for source and/or target bounding boxes. |
| `cr-gun-turret-health-penalty` | 10 | Target scoring penalty for health ratio. Higher values prefer damaged targets; negative values prefer healthier targets. Default: 10. |
| `cr-gun-turret-rotate-penalty` | 0 | Higher values discourage targets requiring more rotation. Default: 0. |
| `cr-gun-turret-fire-penalty` | 0 | Positive values prefer targets without a fire-spreading sticker. Default: 0. |
| `cr-gun-turret-threatening-asteroid-penalty` | -20 | Positive values discourage threatening asteroids; negative values prefer them. Default: -20. Relevant when asteroids are present. |
| `cr-gun-turret-call-for-help-radius` | 40 | Native call-for-help radius. Default: 40. Does not extend another turret's firing range. |
| `cr-gun-turret-max-health` | 400 | Base maximum health before quality bonuses. Default: 400. Existing entities retain engine-managed health when saves are loaded; this does not explicitly heal them. |
| `cr-gun-turret-healing-per-second` | 0 | Absolute health regenerated per second, divided by 60 to obtain healing_per_tick. Default: 0. Negative values cause passive health loss. Slow regeneration is applied once per second by the engine. |
| `cr-gun-turret-repair-speed-modifier` | 1 | Native multiplier for repair tool speed on this turret. Default: 1. |
| `cr-gun-turret-is-military-target` | enabled | Make the turret a high-priority military target for enemies. Default: enabled. |
| `cr-gun-turret-alert-when-attacking` | enabled | Native attack alerts. Default: enabled. |
| `cr-gun-turret-alert-when-damaged` | enabled | Native damage alerts. Default: enabled. |
| `cr-gun-turret-create-ghost-on-death` | enabled | Native ghost creation on destruction, subject to the force's normal ghost rules. Default: enabled. |
| `cr-gun-turret-circuit-wire-max-distance` | 9 | Maximum circuit wire distance from this turret. Default: 9. The other endpoint's wire reach also limits connections. |
| `cr-gun-turret-mining-time` | 0.5 | Base mining time before character/tool modifiers. Default: 0.5 seconds. |
| `cr-gun-turret-heating-energy` | -1 | Negative values preserve official data: 0 kW in base, 50 kW with Space Age. 0 disables freezing; positive values set the heating requirement. This is not an electrical firing cost. Default: -1. |
| `cr-gun-turret-resistance-physical-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-physical-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-impact-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-impact-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-poison-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-poison-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-explosion-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-explosion-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-fire-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-fire-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-laser-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-laser-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-acid-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-acid-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |
| `cr-gun-turret-resistance-electric-decrease` | 0 | Flat damage reduction using the native resistance formula. Default: 0. Applies only to incoming damage of this type. |
| `cr-gun-turret-resistance-electric-percent` | 0 | Native percentage damage resistance, from 0 to 100. Default: 0. 100 grants immunity to this damage type. |

## Catalog summary

2297 additional settings across 128 prototype records; 2348 settings total with Space Age. Only available official content is registered.

| Prototype family | Records | Settings |
| --- | ---: | ---: |
| ammo-turret | 3 | 135 |
| electric-turret | 2 | 130 |
| fluid-turret | 1 | 67 |
| artillery-turret | 1 | 35 |
| gun | 17 | 350 |
| car | 2 | 60 |
| spider-vehicle | 1 | 27 |
| artillery-wagon | 1 | 31 |
| capsule | 14 | 363 |
| land-mine | 1 | 34 |
| combat-robot | 3 | 170 |
| active-defense-equipment | 2 | 59 |
| energy-shield-equipment | 2 | 8 |
| wall | 1 | 24 |
| gate | 1 | 27 |
| armor | 6 | 105 |
| ammo | 17 | 165 |
| projectile | 24 | 233 |
| artillery-projectile | 1 | 5 |
| beam | 7 | 25 |
| stream | 3 | 28 |
| fire | 2 | 26 |
| smoke-with-trigger | 1 | 6 |
| sticker | 12 | 137 |
| chain-active-trigger | 2 | 20 |
| capture-robot | 1 | 27 |

## ammo-turret / gun-turret

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-turret-gun-turret-attack-from-start-frame` | `attack_from_start_frame` | False |  | Attack from start frame. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1.39375 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |
| `cr-ammo-turret-gun-turret-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/gun-turret. |

Not exposed on this record: `alert_when_attacking`, `attacking_animation`, `attacking_speed`, `automated_ammo_count`, `call_for_help_radius`, `circuit_connector`, `circuit_wire_max_distance`, `close_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `drawing_box_vertical_extension`, `dying_explosion`, `fast_replaceable_group`, `flags`, `folded_animation`, `folding_animation`, `folding_sound`, `folding_speed`, `graphics_set`, `heating_energy`, `icon`, `icon_draw_specification`, `icons_positioning`, `inventory_size`, `max_health`, `minable`, `name`, `open_sound`, `prepared_animation`, `preparing_animation`, `preparing_sound`, `preparing_speed`, `rotation_speed`, `selection_box`, `type`, `water_reflection`. See exclusion policy below.

## ammo-turret / railgun-turret

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-turret-railgun-turret-alert-when-attacking` | `alert_when_attacking` | True |  | Alert when attacking. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-allow-turning-when-starting-attack` | `allow_turning_when_starting_attack` | True |  | Allow turning when starting attack. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-from-start-frame` | `attack_from_start_frame` | False |  | Attack from start frame. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-automated-ammo-count` | `automated_ammo_count` | 10 |  | Automated ammo count. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-call-for-help-radius` | `call_for_help_radius` | 40 | tiles | Call for help radius. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-can-retarget-while-starting-attack` | `can_retarget_while_starting_attack` | True |  | Can retarget while starting attack. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-energy-per-shot` | `energy_per_shot` | 10000000.0 | J | Energy per shot. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-inventory-size` | `inventory_size` | 1 |  | Inventory slots. Shrinking inventories may discard stored items. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-leave-attacking-if-shoot-fails` | `leave_attacking_if_shoot_fails` | False |  | Leave attacking if shoot fails. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-max-health` | `max_health` | 4000 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-prepare-with-no-ammo` | `prepare_with_no_ammo` | False |  | Prepare with no ammo. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-rotation-speed` | `rotation_speed` | 0.005 | turns/tick | Rotation speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-shoot-in-prepare-state` | `shoot_in_prepare_state` | False |  | Shoot in prepare state. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-start-attacking-only-when-can-shoot` | `start_attacking_only_when_can_shoot` | False |  | Start attacking only when can shoot. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-preparing-speed` | `preparing_speed` | 0.04 |  | Preparing speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-folding-speed` | `folding_speed` | 0.04 |  | Folding speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-starting-attack-speed` | `starting_attack_speed` | 0.02 |  | Starting attack speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-ending-attack-speed` | `ending_attack_speed` | 0.05 |  | Ending attack speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-cooldown` | `attack_parameters.cooldown` | 170 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | -10 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-min-range` | `attack_parameters.min_range` | 3.5 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-range` | `attack_parameters.range` | 40 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | -20 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | True |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-turn-range` | `attack_parameters.turn_range` | 0.2 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | False |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 3.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-fire-percent` | `resistances.fire.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-acid-percent` | `resistances.acid.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 11000000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-energy-source-input-flow-limit` | `energy_source.input_flow_limit` | 10000000.0 | W | Input flow limit. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |
| `cr-ammo-turret-railgun-turret-heating-energy` | `heating_energy` | 50000.0 | W | Heating energy. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/railgun-turret. |

Not exposed on this record: `attacking_animation`, `attacking_speed`, `circuit_connector`, `close_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `dying_explosion`, `ending_attack_animation`, `flags`, `folded_animation`, `folding_animation`, `folding_sound`, `graphics_set`, `icon`, `name`, `open_sound`, `prepared_animation`, `preparing_animation`, `preparing_sound`, `resource_indicator_animation`, `rotating_sound`, `selection_box`, `special_effect`, `starting_attack_animation`, `tile_height`, `turret_base_has_direction`, `type`, `water_reflection`. See exclusion policy below.

## ammo-turret / rocket-turret

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-turret-rocket-turret-alert-when-attacking` | `alert_when_attacking` | True |  | Alert when attacking. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-allow-turning-when-starting-attack` | `allow_turning_when_starting_attack` | False |  | Allow turning when starting attack. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-from-start-frame` | `attack_from_start_frame` | False |  | Attack from start frame. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-automated-ammo-count` | `automated_ammo_count` | 10 |  | Automated ammo count. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-call-for-help-radius` | `call_for_help_radius` | 40 | tiles | Call for help radius. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-can-retarget-while-starting-attack` | `can_retarget_while_starting_attack` | False |  | Can retarget while starting attack. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-inventory-size` | `inventory_size` | 1 |  | Inventory slots. Shrinking inventories may discard stored items. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-leave-attacking-if-shoot-fails` | `leave_attacking_if_shoot_fails` | True |  | Leave attacking if shoot fails. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-max-health` | `max_health` | 1500 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-prepare-with-no-ammo` | `prepare_with_no_ammo` | True |  | Prepare with no ammo. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-rotation-speed` | `rotation_speed` | 0.005 | turns/tick | Rotation speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-shoot-in-prepare-state` | `shoot_in_prepare_state` | False |  | Shoot in prepare state. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-start-attacking-only-when-can-shoot` | `start_attacking_only_when_can_shoot` | False |  | Start attacking only when can shoot. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-preparing-speed` | `preparing_speed` | 0.08 |  | Preparing speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-folding-speed` | `folding_speed` | 0.08 |  | Folding speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-cooldown` | `attack_parameters.cooldown` | 120 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-min-range` | `attack_parameters.min_range` | 15 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-range` | `attack_parameters.range` | 36 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | -20 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-fire-percent` | `resistances.fire.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-acid-percent` | `resistances.acid.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |
| `cr-ammo-turret-rocket-turret-heating-energy` | `heating_energy` | 50000.0 | W | Heating energy. Uses the native engine property; only this listed path is changed. Scope: ammo-turret/rocket-turret. |

Not exposed on this record: `attacking_animation`, `attacking_speed`, `circuit_connector`, `close_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `dying_explosion`, `flags`, `folded_animation`, `folding_animation`, `folding_sound`, `graphics_set`, `icon`, `name`, `open_sound`, `prepared_animation`, `preparing_animation`, `preparing_sound`, `rotating_sound`, `selection_box`, `type`. See exclusion policy below.

## electric-turret / laser-turret

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-electric-turret-laser-turret-alert-when-attacking` | `alert_when_attacking` | True |  | Alert when attacking. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-allow-turning-when-starting-attack` | `allow_turning_when_starting_attack` | False |  | Allow turning when starting attack. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-from-start-frame` | `attack_from_start_frame` | False |  | Attack from start frame. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-call-for-help-radius` | `call_for_help_radius` | 40 | tiles | Call for help radius. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-can-retarget-while-starting-attack` | `can_retarget_while_starting_attack` | False |  | Can retarget while starting attack. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-leave-attacking-if-shoot-fails` | `leave_attacking_if_shoot_fails` | True |  | Leave attacking if shoot fails. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-max-health` | `max_health` | 1000 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-rotation-speed` | `rotation_speed` | 0.01 | turns/tick | Rotation speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-shoot-in-prepare-state` | `shoot_in_prepare_state` | False |  | Shoot in prepare state. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-start-attacking-only-when-can-shoot` | `start_attacking_only_when_can_shoot` | False |  | Start attacking only when can shoot. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-preparing-speed` | `preparing_speed` | 0.05 |  | Preparing speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-folding-speed` | `folding_speed` | 0.05 |  | Folding speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-cooldown` | `attack_parameters.cooldown` | 40 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 2 |  | Native damage coefficient; ammunition and technology still contribute. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-range` | `attack_parameters.range` | 24 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | -20 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-bounding-box |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-energy-consumption` | `attack_parameters.ammo_type.energy_consumption` | 800000.0 | J | Energy consumption. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-fire-percent` | `resistances.fire.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-acid-percent` | `resistances.acid.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 801000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-energy-source-drain` | `energy_source.drain` | 24000.0 | W | Drain. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-energy-source-input-flow-limit` | `energy_source.input_flow_limit` | 9600000.0 | W | Input flow limit. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-heating-energy` | `heating_energy` | 50000.0 | W | Heating energy. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-action-action-delivery-max-length` | `attack_parameters.ammo_type.action.action_delivery.max_length` | 24 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: electric-turret/laser-turret. |
| `cr-electric-turret-laser-turret-attack-parameters-ammo-type-action-action-delivery-duration` | `attack_parameters.ammo_type.action.action_delivery.duration` | 40 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: electric-turret/laser-turret. |

Not exposed on this record: `circuit_connector`, `close_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `drawing_box_vertical_extension`, `dying_explosion`, `energy_glow_animation`, `fast_replaceable_group`, `flags`, `folded_animation`, `folding_animation`, `folding_sound`, `glow_light_intensity`, `graphics_set`, `icon`, `name`, `open_sound`, `prepared_animation`, `preparing_animation`, `preparing_sound`, `selection_box`, `type`, `water_reflection`. See exclusion policy below.

## electric-turret / tesla-turret

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-electric-turret-tesla-turret-alert-when-attacking` | `alert_when_attacking` | True |  | Alert when attacking. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-allow-turning-when-starting-attack` | `allow_turning_when_starting_attack` | False |  | Allow turning when starting attack. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-from-start-frame` | `attack_from_start_frame` | False |  | Attack from start frame. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-call-for-help-radius` | `call_for_help_radius` | 40 | tiles | Call for help radius. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-can-retarget-while-starting-attack` | `can_retarget_while_starting_attack` | False |  | Can retarget while starting attack. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-leave-attacking-if-shoot-fails` | `leave_attacking_if_shoot_fails` | True |  | Leave attacking if shoot fails. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-max-health` | `max_health` | 2000 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-rotation-speed` | `rotation_speed` | 0.005 | turns/tick | Rotation speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-shoot-in-prepare-state` | `shoot_in_prepare_state` | False |  | Shoot in prepare state. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-start-attacking-only-when-can-shoot` | `start_attacking_only_when_can_shoot` | True |  | Start attacking only when can shoot. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-preparing-speed` | `preparing_speed` | 0.1 |  | Preparing speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-folding-speed` | `folding_speed` | 0.1 |  | Folding speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-ending-attack-speed` | `ending_attack_speed` | 0.03225806451612903 |  | Ending attack speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-cooldown` | `attack_parameters.cooldown` | 120 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0.9 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-range` | `attack_parameters.range` | 30 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-bounding-box |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-energy-consumption` | `attack_parameters.ammo_type.energy_consumption` | 12000000.0 | J | Energy consumption. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-fire-percent` | `resistances.fire.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-acid-percent` | `resistances.acid.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 15000000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-energy-source-drain` | `energy_source.drain` | 1000000.0 | W | Drain. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-energy-source-input-flow-limit` | `energy_source.input_flow_limit` | 7000000.0 | W | Input flow limit. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-action-action-delivery-target-effects-2-action-action-delivery-max-length` | `attack_parameters.ammo_type.action.action_delivery.target_effects.2.action.action_delivery.max_length` | 40 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: electric-turret/tesla-turret. |
| `cr-electric-turret-tesla-turret-attack-parameters-ammo-type-action-action-delivery-target-effects-2-action-action-delivery-duration` | `attack_parameters.ammo_type.action.action_delivery.target_effects.2.action.action_delivery.duration` | 30 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: electric-turret/tesla-turret. |

Not exposed on this record: `circuit_connector`, `close_sound`, `collision_box`, `collision_mask`, `corpse`, `damaged_trigger_effect`, `drawing_box_vertical_extension`, `dying_explosion`, `ending_attack_animation`, `energy_glow_animation`, `fast_replaceable_group`, `flags`, `folded_animation`, `folding_animation`, `folding_sound`, `glow_light_intensity`, `graphics_set`, `icon`, `name`, `open_sound`, `prepared_animation`, `preparing_animation`, `preparing_sound`, `resource_indicator_animation`, `rotating_sound`, `selection_box`, `type`, `working_sound`. See exclusion policy below.

## fluid-turret / flamethrower-turret

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-fluid-turret-flamethrower-turret-activation-buffer-ratio` | `activation_buffer_ratio` | 0.25 |  | Activation buffer ratio. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-alert-when-attacking` | `alert_when_attacking` | True |  | Alert when attacking. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-allow-turning-when-starting-attack` | `allow_turning_when_starting_attack` | False |  | Allow turning when starting attack. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-from-start-frame` | `attack_from_start_frame` | False |  | Attack from start frame. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-call-for-help-radius` | `call_for_help_radius` | 40 | tiles | Call for help radius. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-can-retarget-while-starting-attack` | `can_retarget_while_starting_attack` | False |  | Can retarget while starting attack. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-fluid-buffer-input-flow` | `fluid_buffer_input_flow` | 0.8333333333333334 | fluid/tick | Fluid buffer input flow. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-fluid-buffer-size` | `fluid_buffer_size` | 100 |  | Fluid buffer size. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-leave-attacking-if-shoot-fails` | `leave_attacking_if_shoot_fails` | True |  | Leave attacking if shoot fails. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-max-health` | `max_health` | 1400 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-prepare-range` | `prepare_range` | 35 | tiles | Native preparation search radius, separate from firing range. -1 preserves automatic behavior. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-rotation-speed` | `rotation_speed` | 0.015 | turns/tick | Rotation speed. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-shoot-in-prepare-state` | `shoot_in_prepare_state` | False |  | Shoot in prepare state. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-preparing-speed` | `preparing_speed` | 0.08 |  | Preparing speed. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-folding-speed` | `folding_speed` | 0.08 |  | Folding speed. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-ending-attack-speed` | `ending_attack_speed` | 0.2 |  | Ending attack speed. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-cooldown` | `attack_parameters.cooldown` | 4 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 15 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 1 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-min-range` | `attack_parameters.min_range` | 6 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-range` | `attack_parameters.range` | 30 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-turn-range` | `attack_parameters.turn_range` | 0.3333333333333333 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-fluid-consumption` | `attack_parameters.fluid_consumption` | 0.2 | fluid/shot | Fluid consumption. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-fluids-1-damage-modifier` | `attack_parameters.fluids.1.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-fluids-2-damage-modifier` | `attack_parameters.fluids.2.damage_modifier` | 1.05 |  | Native damage coefficient; ammunition and technology still contribute. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-attack-parameters-fluids-3-damage-modifier` | `attack_parameters.fluids.3.damage_modifier` | 1.1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-fire-percent` | `resistances.fire.percent` | 100 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-acid-percent` | `resistances.acid.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |
| `cr-fluid-turret-flamethrower-turret-fluid-box-volume` | `fluid_box.volume` | 100 |  | Volume. Uses the native engine property; only this listed path is changed. Scope: fluid-turret/flamethrower-turret. |

Not exposed on this record: `attacking_animation`, `attacking_muzzle_animation_shift`, `attacking_speed`, `circuit_connector`, `close_sound`, `collision_box`, `corpse`, `dying_explosion`, `ending_attack_animation`, `ending_attack_muzzle_animation_shift`, `enough_fuel_indicator_light`, `enough_fuel_indicator_picture`, `fast_replaceable_group`, `flags`, `folded_animation`, `folded_muzzle_animation_shift`, `folding_animation`, `folding_muzzle_animation_shift`, `folding_sound`, `graphics_set`, `gun_animation_render_layer`, `gun_animation_secondary_draw_order`, `icon`, `muzzle_animation`, `muzzle_light`, `name`, `not_enough_fuel_indicator_light`, `not_enough_fuel_indicator_picture`, `open_sound`, `out_of_ammo_alert_icon`, `prepared_animation`, `prepared_muzzle_animation_shift`, `preparing_animation`, `preparing_muzzle_animation_shift`, `preparing_sound`, `selection_box`, `surface_conditions`, `turret_base_has_direction`, `type`. See exclusion policy below.

## artillery-turret / artillery-turret

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-artillery-turret-artillery-turret-alert-when-attacking` | `alert_when_attacking` | False |  | Alert when attacking. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-ammo-stack-limit` | `ammo_stack_limit` | 15 |  | Ammo stack limit. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-automated-ammo-count` | `automated_ammo_count` | 5 |  | Automated ammo count. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-cannon-parking-speed` | `cannon_parking_speed` | 0.25 |  | Cannon parking speed. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-disable-automatic-firing` | `disable_automatic_firing` | False |  | Disable automatic firing. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-inventory-size` | `inventory_size` | 1 |  | Inventory slots. Shrinking inventories may discard stored items. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-manual-range-modifier` | `manual_range_modifier` | 2.5 |  | Artillery manual targeting range coefficient. Automatic range is in the shared artillery gun. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-max-health` | `max_health` | 2000 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-turn-after-shooting-cooldown` | `turn_after_shooting_cooldown` | 60 | ticks | Turn after shooting cooldown. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-turret-rotation-speed` | `turret_rotation_speed` | 0.001 | turns/tick | Turret rotation speed. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-physical-decrease` | `resistances.physical.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-physical-percent` | `resistances.physical.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-impact-decrease` | `resistances.impact.decrease` | 50 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-impact-percent` | `resistances.impact.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-explosion-decrease` | `resistances.explosion.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-explosion-percent` | `resistances.explosion.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-fire-decrease` | `resistances.fire.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-fire-percent` | `resistances.fire.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-acid-decrease` | `resistances.acid.decrease` | 3 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-acid-percent` | `resistances.acid.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |
| `cr-artillery-turret-artillery-turret-heating-energy` | `heating_energy` | 200000.0 | W | Heating energy. Uses the native engine property; only this listed path is changed. Scope: artillery-turret/artillery-turret. |

Not exposed on this record: `base_picture`, `base_picture_render_layer`, `cannon_barrel_light_direction`, `cannon_barrel_pictures`, `cannon_barrel_recoil_shiftings`, `cannon_base_pictures`, `cannon_base_shift`, `cannon_parking_frame_count`, `circuit_connector`, `close_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `drawing_box_vertical_extension`, `dying_explosion`, `fast_replaceable_group`, `flags`, `gun`, `icon`, `mined_sound`, `name`, `open_sound`, `rotating_sound`, `selection_box`, `type`, `water_reflection`. See exclusion policy below.

## gun / artillery-wagon-cannon

Base game. Changes target this prototype. 
Shared by the artillery turret and artillery wagon.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-artillery-wagon-cannon-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-cooldown` | `attack_parameters.cooldown` | 200 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-min-range` | `attack_parameters.min_range` | 32 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-range` | `attack_parameters.range` | 224 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-gun-artillery-wagon-cannon-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `random_tint_color`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / combat-shotgun

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-combat-shotgun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1.5 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 0.125 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |
| `cr-gun-combat-shotgun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/combat-shotgun. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / flamethrower

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-flamethrower-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-cooldown` | `attack_parameters.cooldown` | 1 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-min-range` | `attack_parameters.min_range` | 3 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.4 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-fluid-consumption` | `attack_parameters.fluid_consumption` | 0.0 | fluid/shot | Fluid consumption. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |
| `cr-gun-flamethrower-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/flamethrower. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / pistol

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-pistol-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-cooldown` | `attack_parameters.cooldown` | 15 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.2 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1.125 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |
| `cr-gun-pistol-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/pistol. |

Not exposed on this record: `drop_sound`, `flags`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / railgun

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-railgun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 120 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.5 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-range` | `attack_parameters.range` | 40 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1.125 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |
| `cr-gun-railgun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/railgun. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / rocket-launcher

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-rocket-launcher-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-cooldown` | `attack_parameters.cooldown` | 60 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.8 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-range` | `attack_parameters.range` | 36 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |
| `cr-gun-rocket-launcher-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/rocket-launcher. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / shotgun

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-shotgun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 40 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 0.125 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |
| `cr-gun-shotgun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/shotgun. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / spidertron-rocket-launcher-1

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-cooldown` | `attack_parameters.cooldown` | 60 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-range` | `attack_parameters.range` | 36 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | -0.5 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | -0.0625 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |
| `cr-gun-spidertron-rocket-launcher-1-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-1. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `localised_name`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / spidertron-rocket-launcher-2

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-cooldown` | `attack_parameters.cooldown` | 60 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-range` | `attack_parameters.range` | 36 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | -0.5 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | -0.03125 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |
| `cr-gun-spidertron-rocket-launcher-2-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-2. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `localised_name`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / spidertron-rocket-launcher-3

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-cooldown` | `attack_parameters.cooldown` | 60 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-range` | `attack_parameters.range` | 36 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | -0.5 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0.03125 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |
| `cr-gun-spidertron-rocket-launcher-3-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-3. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `localised_name`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / spidertron-rocket-launcher-4

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-cooldown` | `attack_parameters.cooldown` | 60 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-range` | `attack_parameters.range` | 36 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | -0.5 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0.0625 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |
| `cr-gun-spidertron-rocket-launcher-4-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/spidertron-rocket-launcher-4. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `localised_name`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / submachine-gun

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-submachine-gun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 6 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.7 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-range` | `attack_parameters.range` | 18 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1.125 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |
| `cr-gun-submachine-gun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/submachine-gun. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / tank-cannon

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-tank-cannon-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-cooldown` | `attack_parameters.cooldown` | 90 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-min-range` | `attack_parameters.min_range` | 5 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-range` | `attack_parameters.range` | 30 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |
| `cr-gun-tank-cannon-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/tank-cannon. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / tank-flamethrower

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-tank-flamethrower-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-cooldown` | `attack_parameters.cooldown` | 1 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-min-range` | `attack_parameters.min_range` | 3 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-range` | `attack_parameters.range` | 9 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-fluid-consumption` | `attack_parameters.fluid_consumption` | 0.0 | fluid/shot | Fluid consumption. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |
| `cr-gun-tank-flamethrower-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/tank-flamethrower. |

Not exposed on this record: `auto_recycle`, `hidden`, `icon`, `name`, `order`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / tank-machine-gun

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-tank-machine-gun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 4 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.7 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-range` | `attack_parameters.range` | 20 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 1 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |
| `cr-gun-tank-machine-gun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/tank-machine-gun. |

Not exposed on this record: `auto_recycle`, `hidden`, `icon`, `name`, `order`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / teslagun

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-teslagun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 60 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.25 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-range` | `attack_parameters.range` | 24 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/teslagun. |
| `cr-gun-teslagun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/teslagun. |

Not exposed on this record: `default_import_location`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## gun / vehicle-machine-gun

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gun-vehicle-machine-gun-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-cooldown` | `attack_parameters.cooldown` | 4 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-movement-slow-down-factor` | `attack_parameters.movement_slow_down_factor` | 0.7 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-range` | `attack_parameters.range` | 20 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 0.65 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |
| `cr-gun-vehicle-machine-gun-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: gun/vehicle-machine-gun. |

Not exposed on this record: `auto_recycle`, `drop_sound`, `hidden`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## car / car

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-car-car-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: car/car. |
| `cr-car-car-immune-to-all-impacts` | `immune_to_all_impacts` | False |  | Immune to all impacts. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-immune-to-cliff-impacts` | `immune_to_cliff_impacts` | True |  | Immune to cliff impacts. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-immune-to-rock-impacts` | `immune_to_rock_impacts` | False |  | Immune to rock impacts. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-immune-to-tree-impacts` | `immune_to_tree_impacts` | False |  | Immune to tree impacts. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-max-health` | `max_health` | 450 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-turret-return-timeout` | `turret_return_timeout` | 60 | ticks | Turret return timeout. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-turret-rotation-speed` | `turret_rotation_speed` | 0.005833333333333332 | turns/tick | Turret rotation speed. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-impact-decrease` | `resistances.impact.decrease` | 50 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-impact-percent` | `resistances.impact.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-fire-percent` | `resistances.fire.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-acid-percent` | `resistances.acid.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/car. |
| `cr-car-car-minable-mining-time` | `minable.mining_time` | 0.4 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: car/car. |

Not exposed on this record: `alert_icon_shift`, `animation`, `braking_force`, `close_sound`, `collision_box`, `consumption`, `corpse`, `damaged_trigger_effect`, `deliver_category`, `dying_explosion`, `effectivity`, `energy_per_hit_point`, `energy_source`, `flags`, `friction_force`, `guns`, `icon`, `impact_category`, `impact_speed_to_volume_ratio`, `inventory_size`, `light`, `light_animation`, `mined_sound`, `name`, `open_sound`, `render_layer`, `rotation_snap_angle`, `rotation_speed`, `selection_box`, `sound_no_fuel`, `stop_trigger`, `stop_trigger_speed`, `surface_conditions`, `track_particle_triggers`, `turret_animation`, `type`, `water_reflection`, `weight`, `working_sound`. See exclusion policy below.

## car / tank

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-car-tank-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: car/tank. |
| `cr-car-tank-immune-to-all-impacts` | `immune_to_all_impacts` | True |  | Immune to all impacts. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-immune-to-cliff-impacts` | `immune_to_cliff_impacts` | True |  | Immune to cliff impacts. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-immune-to-rock-impacts` | `immune_to_rock_impacts` | True |  | Immune to rock impacts. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-immune-to-tree-impacts` | `immune_to_tree_impacts` | True |  | Immune to tree impacts. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-max-health` | `max_health` | 2000 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-turret-return-timeout` | `turret_return_timeout` | 300 | ticks | Turret return timeout. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-turret-rotation-speed` | `turret_rotation_speed` | 0.005833333333333332 | turns/tick | Turret rotation speed. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-physical-decrease` | `resistances.physical.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-physical-percent` | `resistances.physical.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-impact-decrease` | `resistances.impact.decrease` | 50 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-impact-percent` | `resistances.impact.percent` | 80 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-explosion-decrease` | `resistances.explosion.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-explosion-percent` | `resistances.explosion.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-fire-decrease` | `resistances.fire.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-fire-percent` | `resistances.fire.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-acid-percent` | `resistances.acid.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: car/tank. |
| `cr-car-tank-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: car/tank. |

Not exposed on this record: `alert_icon_shift`, `allow_remote_driving`, `animation`, `braking_force`, `close_sound`, `collision_box`, `consumption`, `corpse`, `damaged_trigger_effect`, `deliver_category`, `drawing_box_vertical_extension`, `dying_explosion`, `effectivity`, `energy_per_hit_point`, `energy_source`, `equipment_grid`, `flags`, `friction_force`, `guns`, `icon`, `impact_category`, `impact_speed_to_volume_ratio`, `inventory_size`, `light`, `light_animation`, `mined_sound`, `name`, `open_sound`, `rotation_snap_angle`, `rotation_speed`, `selection_box`, `sound_no_fuel`, `stop_trigger`, `stop_trigger_speed`, `surface_conditions`, `tank_driving`, `terrain_friction_modifier`, `track_particle_triggers`, `trash_inventory_size`, `turret_animation`, `type`, `water_reflection`, `weight`, `working_sound`. See exclusion policy below.

## spider-vehicle / spidertron

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-spider-vehicle-spidertron-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-automatic-weapon-cycling` | `automatic_weapon_cycling` | True |  | Automatic weapon cycling. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-chain-shooting-cooldown-modifier` | `chain_shooting_cooldown_modifier` | 0.5 |  | Chain shooting cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-max-health` | `max_health` | 3000 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-torso-rotation-speed` | `torso_rotation_speed` | 0.005 | turns/tick | Torso rotation speed. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-physical-decrease` | `resistances.physical.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-physical-percent` | `resistances.physical.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-impact-decrease` | `resistances.impact.decrease` | 50 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-impact-percent` | `resistances.impact.percent` | 80 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-explosion-decrease` | `resistances.explosion.decrease` | 20 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-explosion-percent` | `resistances.explosion.percent` | 75 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-fire-decrease` | `resistances.fire.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-fire-percent` | `resistances.fire.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-laser-percent` | `resistances.laser.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-acid-percent` | `resistances.acid.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-resistances-electric-percent` | `resistances.electric.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |
| `cr-spider-vehicle-spidertron-minable-mining-time` | `minable.mining_time` | 1 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: spider-vehicle/spidertron. |

Not exposed on this record: `alert_icon_shift`, `allow_remote_driving`, `braking_force`, `chunk_exploration_radius`, `close_sound`, `collision_box`, `corpse`, `drawing_box_vertical_extension`, `dying_explosion`, `energy_per_hit_point`, `energy_source`, `equipment_grid`, `factoriopedia_simulation`, `flags`, `friction_force`, `graphics_set`, `guns`, `height`, `icon`, `inventory_size`, `mined_sound`, `minimap_representation`, `movement_energy_consumption`, `name`, `open_sound`, `selected_minimap_representation`, `selection_box`, `selection_priority`, `spider_engine`, `sticker_box`, `surface_conditions`, `trash_inventory_size`, `type`, `weight`, `working_sound`. See exclusion policy below.

## artillery-wagon / artillery-wagon

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-artillery-wagon-artillery-wagon-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-ammo-stack-limit` | `ammo_stack_limit` | 100 |  | Ammo stack limit. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-cannon-parking-speed` | `cannon_parking_speed` | 0.25 |  | Cannon parking speed. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-disable-automatic-firing` | `disable_automatic_firing` | False |  | Disable automatic firing. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-inventory-size` | `inventory_size` | 1 |  | Inventory slots. Shrinking inventories may discard stored items. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-is-military-target` | `is_military_target` | False |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-manual-range-modifier` | `manual_range_modifier` | 2.5 |  | Artillery manual targeting range coefficient. Automatic range is in the shared artillery gun. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-max-health` | `max_health` | 600 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-turn-after-shooting-cooldown` | `turn_after_shooting_cooldown` | 60 | ticks | Turn after shooting cooldown. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-turret-rotation-speed` | `turret_rotation_speed` | 0.001 | turns/tick | Turret rotation speed. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-physical-decrease` | `resistances.physical.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-physical-percent` | `resistances.physical.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-impact-decrease` | `resistances.impact.decrease` | 50 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-impact-percent` | `resistances.impact.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-explosion-decrease` | `resistances.explosion.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-explosion-percent` | `resistances.explosion.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-fire-decrease` | `resistances.fire.decrease` | 15 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-fire-percent` | `resistances.fire.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-acid-decrease` | `resistances.acid.decrease` | 3 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-acid-percent` | `resistances.acid.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |
| `cr-artillery-wagon-artillery-wagon-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: artillery-wagon/artillery-wagon. |

Not exposed on this record: `air_resistance`, `back_light`, `braking_force`, `cannon_barrel_light_direction`, `cannon_barrel_pictures`, `cannon_barrel_recoil_shiftings`, `cannon_base_height`, `cannon_base_pictures`, `cannon_base_shift_when_horizontal`, `cannon_base_shift_when_vertical`, `cannon_parking_frame_count`, `close_sound`, `collision_box`, `color`, `connection_distance`, `corpse`, `damaged_trigger_effect`, `deliver_category`, `drive_over_tie_trigger`, `drive_over_tie_trigger_minimal_speed`, `dying_explosion`, `energy_per_hit_point`, `factoriopedia_simulation`, `flags`, `friction_force`, `gun`, `icon`, `icon_draw_specification`, `joint_distance`, `mined_sound`, `minimap_representation`, `name`, `open_sound`, `pictures`, `rotating_sound`, `selected_minimap_representation`, `selection_box`, `stand_by_light`, `surface_conditions`, `tie_distance`, `type`, `vertical_selection_shift`, `water_reflection`, `weight`, `wheels`, `working_sound`. See exclusion policy below.

## capsule / bioflux

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 960 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 0 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/bioflux. |
| `cr-capsule-bioflux-capsule-action-attack-parameters-ammo-type-action-action-delivery-target-effects-1-damage-amount` | `capsule_action.attack_parameters.ammo_type.action.action_delivery.target_effects.1.damage.amount` | -80 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: capsule/bioflux. |

Not exposed on this record: `default_import_location`, `drop_sound`, `fuel_categories`, `fuel_value`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `spoil_result`, `spoil_ticks`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / cliff-explosives

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 10 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-radius` | `capsule_action.radius` | 1.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: capsule/cliff-explosives. |
| `cr-capsule-cliff-explosives-capsule-action-attack-parameters-ammo-type-action-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/cliff-explosives. |

Not exposed on this record: `default_import_location`, `drop_sound`, `flags`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## capsule / cluster-grenade

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 20 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |
| `cr-capsule-cluster-grenade-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/cluster-grenade. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / defender-capsule

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 15 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 20 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |
| `cr-capsule-defender-capsule-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/defender-capsule. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / destroyer-capsule

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 25 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |
| `cr-capsule-destroyer-capsule-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/destroyer-capsule. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / distractor-capsule

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 25 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |
| `cr-capsule-distractor-capsule-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/distractor-capsule. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / grenade

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |
| `cr-capsule-grenade-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/grenade. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / jelly

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-jelly-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 960 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 0 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |
| `cr-capsule-jelly-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/jelly. |

Not exposed on this record: `default_import_location`, `drop_sound`, `fuel_categories`, `fuel_value`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `spoil_result`, `spoil_ticks`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / jellynut

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-jellynut-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 960 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 0 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |
| `cr-capsule-jellynut-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/jellynut. |

Not exposed on this record: `default_import_location`, `drop_sound`, `fuel_categories`, `fuel_value`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `pictures`, `spoil_result`, `spoil_ticks`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / poison-capsule

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 25 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |
| `cr-capsule-poison-capsule-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/poison-capsule. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / raw-fish

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 0 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/raw-fish. |
| `cr-capsule-raw-fish-capsule-action-attack-parameters-ammo-type-action-action-delivery-target-effects-1-damage-amount` | `capsule_action.attack_parameters.ammo_type.action.action_delivery.target_effects.1.damage.amount` | -80 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: capsule/raw-fish. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `send_to_orbit_mode`, `spoil_result`, `spoil_ticks`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / slowdown-capsule

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 30 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 25 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |
| `cr-capsule-slowdown-capsule-capsule-action-attack-parameters-ammo-type-action-1-action-delivery-starting-speed` | `capsule_action.attack_parameters.ammo_type.action.1.action_delivery.starting_speed` | 0.3 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: capsule/slowdown-capsule. |

Not exposed on this record: `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / yumako

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 960 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 0 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako. |
| `cr-capsule-yumako-capsule-action-attack-parameters-ammo-type-action-action-delivery-target-effects-1-damage-amount` | `capsule_action.attack_parameters.ammo_type.action.action_delivery.target_effects.1.damage.amount` | -80 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: capsule/yumako. |

Not exposed on this record: `default_import_location`, `drop_sound`, `fuel_categories`, `fuel_value`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `pictures`, `spoil_result`, `spoil_ticks`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## capsule / yumako-mash

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-consumption-modifier` | `capsule_action.attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-cooldown` | `capsule_action.attack_parameters.cooldown` | 960 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-cooldown-deviation` | `capsule_action.attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-damage-modifier` | `capsule_action.attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-fire-penalty` | `capsule_action.attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-health-penalty` | `capsule_action.attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-lead-target-for-projectile-delay` | `capsule_action.attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-lead-target-for-projectile-speed` | `capsule_action.attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-min-range` | `capsule_action.attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-movement-slow-down-factor` | `capsule_action.attack_parameters.movement_slow_down_factor` | 1 |  | Movement slow down factor. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-range` | `capsule_action.attack_parameters.range` | 0 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-rotate-penalty` | `capsule_action.attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-threatening-asteroid-penalty` | `capsule_action.attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-true-collinear-ejection` | `capsule_action.attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-turn-range` | `capsule_action.attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-use-shooter-direction` | `capsule_action.attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-apply-projection-to-projectile-creation-position` | `capsule_action.attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-projectile-creation-distance` | `capsule_action.attack_parameters.projectile_creation_distance` | 0 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-projectile-orientation-offset` | `capsule_action.attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-range-mode` | `capsule_action.attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-type-clamp-position` | `capsule_action.attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-type-consumption-modifier` | `capsule_action.attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-type-cooldown-modifier` | `capsule_action.attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-type-force-clamp-to-max-range` | `capsule_action.attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-type-range-modifier` | `capsule_action.attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: capsule/yumako-mash. |
| `cr-capsule-yumako-mash-capsule-action-attack-parameters-ammo-type-action-action-delivery-target-effects-1-damage-amount` | `capsule_action.attack_parameters.ammo_type.action.action_delivery.target_effects.1.damage.amount` | -80 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: capsule/yumako-mash. |

Not exposed on this record: `default_import_location`, `drop_sound`, `fuel_categories`, `fuel_value`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `spoil_result`, `spoil_ticks`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## land-mine / land-mine

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-land-mine-land-mine-alert-when-damaged` | `alert_when_damaged` | False |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-circuit-wire-max-distance` | `circuit_wire_max_distance` | 9 | tiles | Circuit wire max distance. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-force-die-on-attack` | `force_die_on_attack` | True |  | Force die on attack. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-max-health` | `max_health` | 15 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-timeout` | `timeout` | 120 | ticks | Timeout. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-trigger-interval` | `trigger_interval` | 10 | ticks | Trigger interval. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-trigger-radius` | `trigger_radius` | 2.5 | tiles | Trigger radius. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-fire-percent` | `resistances.fire.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-acid-percent` | `resistances.acid.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-minable-mining-time` | `minable.mining_time` | 0.5 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-action-action-delivery-source-effects-1-action-radius` | `action.action_delivery.source_effects.1.action.radius` | 6 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-action-action-delivery-source-effects-1-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.source_effects.1.action.action_delivery.target_effects.1.damage.amount` | 250 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-action-action-delivery-source-effects-3-damage-amount` | `action.action_delivery.source_effects.3.damage.amount` | 1000 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-action-action-delivery-source-effects-4-damage-amount` | `action.action_delivery.source_effects.4.damage.amount` | 100 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: land-mine/land-mine. |
| `cr-land-mine-land-mine-action-action-delivery-source-effects-4-radius` | `action.action_delivery.source_effects.4.radius` | 3 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: land-mine/land-mine. |

Not exposed on this record: `ammo_category`, `circuit_connector`, `close_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `dying_explosion`, `fast_replaceable_group`, `flags`, `icon`, `mined_sound`, `name`, `open_sound`, `picture_safe`, `picture_set`, `picture_set_enemy`, `selection_box`, `type`. See exclusion policy below.

## combat-robot / defender

Base game. Changes target this prototype. 
Direct combat consumers: `projectile/defender-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-combat-robot-defender-alert-when-damaged` | `alert_when_damaged` | False |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-follows-player` | `follows_player` | True |  | Follows player. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-friction` | `friction` | 0.01 |  | Friction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-max-health` | `max_health` | 60 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-max-separation-force` | `max_separation_force` | 0.01 |  | Max separation force. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. -1 preserves the native unlimited default. |
| `cr-combat-robot-defender-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-range-from-player` | `range_from_player` | 6 | tiles | Range from player. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-separation-force-factor` | `separation_force_factor` | 0.01 |  | Separation force factor. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-separation-range` | `separation_range` | 1 | tiles | Separation range. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-speed` | `speed` | 0.01 | tiles/tick | Speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-time-to-live` | `time_to_live` | 2700 | ticks | Time to live. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-cooldown` | `attack_parameters.cooldown` | 20 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0.2 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-fire-percent` | `resistances.fire.percent` | 95 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-acid-percent` | `resistances.acid.percent` | 80 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/defender. |
| `cr-combat-robot-defender-attack-parameters-ammo-type-action-action-delivery-target-effects-2-damage-amount` | `attack_parameters.ammo_type.action.action_delivery.target_effects.2.damage.amount` | 8 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: combat-robot/defender. |

Not exposed on this record: `collision_box`, `damaged_trigger_effect`, `destroy_action`, `dying_explosion`, `dying_trigger_effect`, `flags`, `hit_visualization_box`, `icon`, `idle`, `in_motion`, `name`, `order`, `selection_box`, `shadow_idle`, `shadow_in_motion`, `subgroup`, `type`, `water_reflection`, `working_sound`. See exclusion policy below.

## combat-robot / destroyer

Base game. Changes target this prototype. 
Direct combat consumers: `projectile/destroyer-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-combat-robot-destroyer-alert-when-damaged` | `alert_when_damaged` | False |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-follows-player` | `follows_player` | True |  | Follows player. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-friction` | `friction` | 0.01 |  | Friction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-max-health` | `max_health` | 60 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-max-separation-force` | `max_separation_force` | 0.01 |  | Max separation force. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. -1 preserves the native unlimited default. |
| `cr-combat-robot-destroyer-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-range-from-player` | `range_from_player` | 6 | tiles | Range from player. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-separation-force-factor` | `separation_force_factor` | 0.01 |  | Separation force factor. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-separation-range` | `separation_range` | 1.5 | tiles | Separation range. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-speed` | `speed` | 0.01 | tiles/tick | Speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-time-to-live` | `time_to_live` | 7200 | ticks | Time to live. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-cooldown` | `attack_parameters.cooldown` | 20 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0.2 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 2 |  | Native damage coefficient; ammunition and technology still contribute. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-range` | `attack_parameters.range` | 20 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-bounding-box |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-fire-percent` | `resistances.fire.percent` | 95 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-acid-percent` | `resistances.acid.percent` | 90 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-action-action-delivery-max-length` | `attack_parameters.ammo_type.action.action_delivery.max_length` | 25 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: combat-robot/destroyer. |
| `cr-combat-robot-destroyer-attack-parameters-ammo-type-action-action-delivery-duration` | `attack_parameters.ammo_type.action.action_delivery.duration` | 20 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: combat-robot/destroyer. |

Not exposed on this record: `collision_box`, `damaged_trigger_effect`, `destroy_action`, `dying_explosion`, `dying_trigger_effect`, `flags`, `hit_visualization_box`, `icon`, `idle`, `in_motion`, `name`, `order`, `selection_box`, `shadow_idle`, `shadow_in_motion`, `subgroup`, `type`, `water_reflection`, `working_sound`. See exclusion policy below.

## combat-robot / distractor

Base game. Changes target this prototype. 
Direct combat consumers: `projectile/distractor-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-combat-robot-distractor-alert-when-damaged` | `alert_when_damaged` | False |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-follows-player` | `follows_player` | False |  | Follows player. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-friction` | `friction` | 0 |  | Friction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-max-health` | `max_health` | 180 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-max-separation-force` | `max_separation_force` | 0.0 |  | Max separation force. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. -1 preserves the native unlimited default. |
| `cr-combat-robot-distractor-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-range-from-player` | `range_from_player` | 0 | tiles | Range from player. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-separation-force-factor` | `separation_force_factor` | 0.0 |  | Separation force factor. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-separation-range` | `separation_range` | 0.0 | tiles | Separation range. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-speed` | `speed` | 0 | tiles/tick | Speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-time-to-live` | `time_to_live` | 5400 | ticks | Time to live. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-cooldown` | `attack_parameters.cooldown` | 40 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0.2 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 0.5 |  | Native damage coefficient; ammunition and technology still contribute. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-bounding-box |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-fire-percent` | `resistances.fire.percent` | 95 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-acid-percent` | `resistances.acid.percent` | 85 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-action-action-delivery-max-length` | `attack_parameters.ammo_type.action.action_delivery.max_length` | 15 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: combat-robot/distractor. |
| `cr-combat-robot-distractor-attack-parameters-ammo-type-action-action-delivery-duration` | `attack_parameters.ammo_type.action.action_delivery.duration` | 20 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: combat-robot/distractor. |

Not exposed on this record: `collision_box`, `damaged_trigger_effect`, `destroy_action`, `dying_explosion`, `dying_trigger_effect`, `factoriopedia_simulation`, `flags`, `hit_visualization_box`, `icon`, `idle`, `in_motion`, `name`, `order`, `selection_box`, `shadow_idle`, `shadow_in_motion`, `subgroup`, `type`, `water_reflection`, `working_sound`. See exclusion policy below.

## active-defense-equipment / discharge-defense-equipment

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-active-defense-equipment-discharge-defense-equipment-automatic` | `automatic` | False |  | Automatic. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-cooldown` | `attack_parameters.cooldown` | 150 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 10 |  | Native damage coefficient; ammunition and technology still contribute. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-range` | `attack_parameters.range` | 10 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-apply-projection-to-projectile-creation-position` | `attack_parameters.apply_projection_to_projectile_creation_position` | True |  | Apply projection to projectile creation position. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-projectile-creation-distance` | `attack_parameters.projectile_creation_distance` | 0.6 |  | Projectile creation distance. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-projectile-orientation-offset` | `attack_parameters.projectile_orientation_offset` | 0 |  | Projectile orientation offset. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-center |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-energy-consumption` | `attack_parameters.ammo_type.energy_consumption` | 2000000.0 | J | Energy consumption. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 4040000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-action-1-radius` | `attack_parameters.ammo_type.action.1.radius` | 8 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-action-1-action-delivery-1-target-effects-2-distance` | `attack_parameters.ammo_type.action.1.action_delivery.1.target_effects.2.distance` | 4 | tiles | Distance. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-action-1-action-delivery-2-max-length` | `attack_parameters.ammo_type.action.1.action_delivery.2.max_length` | 16 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: active-defense-equipment/discharge-defense-equipment. |
| `cr-active-defense-equipment-discharge-defense-equipment-attack-parameters-ammo-type-action-1-action-delivery-2-duration` | `attack_parameters.ammo_type.action.1.action_delivery.2.duration` | 15 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/discharge-defense-equipment. |

Not exposed on this record: `categories`, `name`, `shape`, `sprite`, `type`. See exclusion policy below.

## active-defense-equipment / personal-laser-defense-equipment

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-active-defense-equipment-personal-laser-defense-equipment-automatic` | `automatic` | True |  | Automatic. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-consumption-modifier` | `attack_parameters.ammo_consumption_modifier` | 1 |  | Native consumption per shot; one unit means one round, not a magazine. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-cooldown` | `attack_parameters.cooldown` | 40 | ticks | Ticks between shots before research. Shots per second = 60 / cooldown. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-cooldown-deviation` | `attack_parameters.cooldown_deviation` | 0 |  | Cooldown deviation. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-damage-modifier` | `attack_parameters.damage_modifier` | 1 |  | Native damage coefficient; ammunition and technology still contribute. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-fire-penalty` | `attack_parameters.fire_penalty` | 0 |  | Fire penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-health-penalty` | `attack_parameters.health_penalty` | 0 |  | Health penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-lead-target-for-projectile-delay` | `attack_parameters.lead_target_for_projectile_delay` | 0 |  | Lead target for projectile delay. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-lead-target-for-projectile-speed` | `attack_parameters.lead_target_for_projectile_speed` | 0 |  | Lead target for projectile speed. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-min-range` | `attack_parameters.min_range` | 0 | tiles | Minimum targeting distance; clamped to maximum range if reversed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-range` | `attack_parameters.range` | 15 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-rotate-penalty` | `attack_parameters.rotate_penalty` | 0 |  | Rotate penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-threatening-asteroid-penalty` | `attack_parameters.threatening_asteroid_penalty` | 0 |  | Threatening asteroid penalty. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-true-collinear-ejection` | `attack_parameters.true_collinear_ejection` | False |  | True collinear ejection. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-turn-range` | `attack_parameters.turn_range` | 1 |  | Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-use-shooter-direction` | `attack_parameters.use_shooter_direction` | False |  | Use shooter direction. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-warmup` | `attack_parameters.warmup` | 0 | ticks | Delay after a shooting order, separate from turret preparation. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-range-mode` | `attack_parameters.range_mode` | center-to-bounding-box |  | Range mode. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-clamp-position` | `attack_parameters.ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-consumption-modifier` | `attack_parameters.ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-cooldown-modifier` | `attack_parameters.ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-energy-consumption` | `attack_parameters.ammo_type.energy_consumption` | 50000.0 | J | Energy consumption. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-force-clamp-to-max-range` | `attack_parameters.ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-range-modifier` | `attack_parameters.ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 220000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-action-action-delivery-max-length` | `attack_parameters.ammo_type.action.action_delivery.max_length` | 15 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: active-defense-equipment/personal-laser-defense-equipment. |
| `cr-active-defense-equipment-personal-laser-defense-equipment-attack-parameters-ammo-type-action-action-delivery-duration` | `attack_parameters.ammo_type.action.action_delivery.duration` | 40 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: active-defense-equipment/personal-laser-defense-equipment. |

Not exposed on this record: `categories`, `name`, `shape`, `sprite`, `type`. See exclusion policy below.

## energy-shield-equipment / energy-shield-equipment

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-energy-shield-equipment-energy-shield-equipment-energy-per-shield` | `energy_per_shield` | 20000.0 | J | Energy per shield. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-equipment. |
| `cr-energy-shield-equipment-energy-shield-equipment-max-shield-value` | `max_shield_value` | 50 | HP | Max shield value. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-equipment. |
| `cr-energy-shield-equipment-energy-shield-equipment-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 120000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-equipment. |
| `cr-energy-shield-equipment-energy-shield-equipment-energy-source-input-flow-limit` | `energy_source.input_flow_limit` | 240000.0 | W | Input flow limit. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-equipment. |

Not exposed on this record: `categories`, `name`, `shape`, `sprite`, `type`. See exclusion policy below.

## energy-shield-equipment / energy-shield-mk2-equipment

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-energy-shield-equipment-energy-shield-mk2-equipment-energy-per-shield` | `energy_per_shield` | 30000.0 | J | Energy per shield. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-mk2-equipment. |
| `cr-energy-shield-equipment-energy-shield-mk2-equipment-max-shield-value` | `max_shield_value` | 150 | HP | Max shield value. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-mk2-equipment. |
| `cr-energy-shield-equipment-energy-shield-mk2-equipment-energy-source-buffer-capacity` | `energy_source.buffer_capacity` | 180000.0 | J | Buffer capacity. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-mk2-equipment. |
| `cr-energy-shield-equipment-energy-shield-mk2-equipment-energy-source-input-flow-limit` | `energy_source.input_flow_limit` | 360000.0 | W | Input flow limit. Uses the native engine property; only this listed path is changed. Scope: energy-shield-equipment/energy-shield-mk2-equipment. |

Not exposed on this record: `categories`, `name`, `shape`, `sprite`, `type`. See exclusion policy below.

## wall / stone-wall

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-wall-stone-wall-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-is-military-target` | `is_military_target` | False |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-max-health` | `max_health` | 350 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-repair-speed-modifier` | `repair_speed_modifier` | 2 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-physical-decrease` | `resistances.physical.decrease` | 3 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-physical-percent` | `resistances.physical.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-impact-decrease` | `resistances.impact.decrease` | 45 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-impact-percent` | `resistances.impact.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-explosion-decrease` | `resistances.explosion.decrease` | 10 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-explosion-percent` | `resistances.explosion.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-fire-percent` | `resistances.fire.percent` | 100 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-laser-percent` | `resistances.laser.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-acid-percent` | `resistances.acid.percent` | 80 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |
| `cr-wall-stone-wall-minable-mining-time` | `minable.mining_time` | 0.2 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: wall/stone-wall. |

Not exposed on this record: `circuit_connector`, `circuit_wire_max_distance`, `close_sound`, `collision_box`, `connected_gate_visualization`, `corpse`, `damaged_trigger_effect`, `default_output_signal`, `dying_explosion`, `fast_replaceable_group`, `flags`, `icon`, `impact_category`, `mined_sound`, `name`, `open_sound`, `pictures`, `repair_sound`, `selection_box`, `type`, `visual_merge_group`, `wall_diode_green`, `wall_diode_green_light_bottom`, `wall_diode_green_light_left`, `wall_diode_green_light_right`, `wall_diode_green_light_top`, `wall_diode_red`, `wall_diode_red_light_bottom`, `wall_diode_red_light_left`, `wall_diode_red_light_right`, `wall_diode_red_light_top`, `water_reflection`. See exclusion policy below.

## gate / gate

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-gate-gate-activation-distance` | `activation_distance` | 3 | tiles | Activation distance. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-alert-when-damaged` | `alert_when_damaged` | True |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: gate/gate. |
| `cr-gate-gate-is-military-target` | `is_military_target` | False |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-max-health` | `max_health` | 350 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-opening-speed` | `opening_speed` | 0.0666666 |  | Opening speed. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-timeout-to-close` | `timeout_to_close` | 5 | ticks | Timeout to close. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-physical-decrease` | `resistances.physical.decrease` | 3 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-physical-percent` | `resistances.physical.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-impact-decrease` | `resistances.impact.decrease` | 45 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-impact-percent` | `resistances.impact.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-explosion-decrease` | `resistances.explosion.decrease` | 10 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-explosion-percent` | `resistances.explosion.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-fire-percent` | `resistances.fire.percent` | 100 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-laser-percent` | `resistances.laser.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-acid-percent` | `resistances.acid.percent` | 80 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |
| `cr-gate-gate-minable-mining-time` | `minable.mining_time` | 0.1 |  | Mining time. Uses the native engine property; only this listed path is changed. Scope: gate/gate. |

Not exposed on this record: `closing_sound`, `collision_box`, `corpse`, `damaged_trigger_effect`, `dying_explosion`, `factoriopedia_simulation`, `fadeout_interval`, `fast_replaceable_group`, `flags`, `horizontal_animation`, `horizontal_rail_animation_left`, `horizontal_rail_animation_right`, `horizontal_rail_base`, `icon`, `impact_category`, `name`, `opening_sound`, `selection_box`, `type`, `vertical_animation`, `vertical_rail_animation_left`, `vertical_rail_animation_right`, `vertical_rail_base`, `wall_patch`. See exclusion policy below.

## armor / heavy-armor

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-armor-heavy-armor-provides-flight` | `provides_flight` | False |  | Provides flight. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-physical-decrease` | `resistances.physical.decrease` | 6 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-physical-percent` | `resistances.physical.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-explosion-decrease` | `resistances.explosion.decrease` | 20 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-explosion-percent` | `resistances.explosion.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-fire-percent` | `resistances.fire.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-acid-percent` | `resistances.acid.percent` | 40 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |
| `cr-armor-heavy-armor-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/heavy-armor. |

Not exposed on this record: `drop_sound`, `factoriopedia_simulation`, `icon`, `infinite`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## armor / light-armor

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-armor-light-armor-provides-flight` | `provides_flight` | False |  | Provides flight. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-physical-decrease` | `resistances.physical.decrease` | 3 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-physical-percent` | `resistances.physical.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-explosion-decrease` | `resistances.explosion.decrease` | 2 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-explosion-percent` | `resistances.explosion.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-fire-percent` | `resistances.fire.percent` | 10 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-acid-percent` | `resistances.acid.percent` | 20 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |
| `cr-armor-light-armor-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/light-armor. |

Not exposed on this record: `drop_sound`, `factoriopedia_simulation`, `icon`, `infinite`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## armor / mech-armor

Space Age only. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-armor-mech-armor-inventory-size-bonus` | `inventory_size_bonus` | 50 |  | Inventory size bonus. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-physical-decrease` | `resistances.physical.decrease` | 10 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-physical-percent` | `resistances.physical.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-explosion-decrease` | `resistances.explosion.decrease` | 60 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-explosion-percent` | `resistances.explosion.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-fire-decrease` | `resistances.fire.decrease` | 10 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-fire-percent` | `resistances.fire.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-acid-percent` | `resistances.acid.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |
| `cr-armor-mech-armor-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/mech-armor. |

Not exposed on this record: `close_sound`, `collision_box`, `drawing_box`, `drop_sound`, `equipment_grid`, `factoriopedia_simulation`, `flight_sound`, `icon`, `infinite`, `inventory_move_sound`, `landing_sound`, `moving_sound`, `name`, `open_sound`, `order`, `pick_sound`, `provides_flight`, `stack_size`, `steps_sound`, `subgroup`, `takeoff_sound`, `type`, `weight`. See exclusion policy below.

## armor / modular-armor

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-armor-modular-armor-inventory-size-bonus` | `inventory_size_bonus` | 10 |  | Inventory size bonus. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-provides-flight` | `provides_flight` | False |  | Provides flight. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-physical-decrease` | `resistances.physical.decrease` | 6 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-physical-percent` | `resistances.physical.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-explosion-decrease` | `resistances.explosion.decrease` | 30 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-explosion-percent` | `resistances.explosion.percent` | 35 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-fire-percent` | `resistances.fire.percent` | 40 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-acid-percent` | `resistances.acid.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |
| `cr-armor-modular-armor-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/modular-armor. |

Not exposed on this record: `close_sound`, `drop_sound`, `equipment_grid`, `factoriopedia_simulation`, `icon`, `infinite`, `inventory_move_sound`, `name`, `open_sound`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## armor / power-armor

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-armor-power-armor-inventory-size-bonus` | `inventory_size_bonus` | 20 |  | Inventory size bonus. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-provides-flight` | `provides_flight` | False |  | Provides flight. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-physical-decrease` | `resistances.physical.decrease` | 8 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-physical-percent` | `resistances.physical.percent` | 30 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-explosion-decrease` | `resistances.explosion.decrease` | 40 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-explosion-percent` | `resistances.explosion.percent` | 40 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-fire-percent` | `resistances.fire.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-acid-percent` | `resistances.acid.percent` | 60 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |
| `cr-armor-power-armor-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor. |

Not exposed on this record: `close_sound`, `drop_sound`, `equipment_grid`, `factoriopedia_simulation`, `icon`, `infinite`, `inventory_move_sound`, `name`, `open_sound`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## armor / power-armor-mk2

Base game. Changes target this prototype. 

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-armor-power-armor-mk2-inventory-size-bonus` | `inventory_size_bonus` | 30 |  | Inventory size bonus. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-provides-flight` | `provides_flight` | False |  | Provides flight. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-physical-decrease` | `resistances.physical.decrease` | 10 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-physical-percent` | `resistances.physical.percent` | 40 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-explosion-decrease` | `resistances.explosion.decrease` | 60 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-explosion-percent` | `resistances.explosion.percent` | 50 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-fire-percent` | `resistances.fire.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-acid-percent` | `resistances.acid.percent` | 70 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |
| `cr-armor-power-armor-mk2-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: armor/power-armor-mk2. |

Not exposed on this record: `close_sound`, `drop_sound`, `equipment_grid`, `factoriopedia_simulation`, `icon`, `infinite`, `inventory_move_sound`, `name`, `open_sound`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / artillery-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/artillery-wagon-cannon`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-artillery-shell-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-artillery-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / atomic-bomb

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/rocket-turret`, `gun/rocket-launcher`, `gun/spidertron-rocket-launcher-1`, `gun/spidertron-rocket-launcher-2`, `gun/spidertron-rocket-launcher-3`, `gun/spidertron-rocket-launcher-4`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-atomic-bomb-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 10 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1.5 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-atomic-bomb-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 0.05 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `pictures`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / cannon-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/tank-cannon`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-cannon-shell-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1.25 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-cannon-shell-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / capture-robot-rocket

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/rocket-turret`, `gun/rocket-launcher`, `gun/spidertron-rocket-launcher-1`, `gun/spidertron-rocket-launcher-2`, `gun/spidertron-rocket-launcher-3`, `gun/spidertron-rocket-launcher-4`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-capture-robot-rocket-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-shoot-protected` | `shoot_protected` | True |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-capture-robot-rocket-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 0.1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `default_import_location`, `drop_sound`, `flags`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / explosive-cannon-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/tank-cannon`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-explosive-cannon-shell-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-cannon-shell-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / explosive-rocket

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/rocket-turret`, `gun/rocket-launcher`, `gun/spidertron-rocket-launcher-1`, `gun/spidertron-rocket-launcher-2`, `gun/spidertron-rocket-launcher-3`, `gun/spidertron-rocket-launcher-4`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-explosive-rocket-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-rocket-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 0.1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / explosive-uranium-cannon-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/tank-cannon`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-explosive-uranium-cannon-shell-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-explosive-uranium-cannon-shell-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `pictures`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / firearm-magazine

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/gun-turret`, `gun/pistol`, `gun/submachine-gun`, `gun/tank-machine-gun`, `gun/vehicle-machine-gun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-firearm-magazine-magazine-size` | `magazine_size` | 10 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-firearm-magazine-ammo-type-action-1-action-delivery-1-target-effects-3-damage-amount` | `ammo_type.action.1.action_delivery.1.target_effects.3.damage.amount` | 5 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / flamethrower-ammo

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/flamethrower`, `gun/tank-flamethrower`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-flamethrower-ammo-magazine-size` | `magazine_size` | 100 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-1-clamp-position` | `ammo_type.1.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-1-consumption-modifier` | `ammo_type.1.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-1-cooldown-modifier` | `ammo_type.1.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-1-force-clamp-to-max-range` | `ammo_type.1.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-1-range-modifier` | `ammo_type.1.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-2-clamp-position` | `ammo_type.2.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-2-consumption-modifier` | `ammo_type.2.consumption_modifier` | 1.125 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-2-cooldown-modifier` | `ammo_type.2.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-2-force-clamp-to-max-range` | `ammo_type.2.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-flamethrower-ammo-ammo-type-2-range-modifier` | `ammo_type.2.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / piercing-rounds-magazine

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/gun-turret`, `gun/pistol`, `gun/submachine-gun`, `gun/tank-machine-gun`, `gun/vehicle-machine-gun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-piercing-rounds-magazine-magazine-size` | `magazine_size` | 10 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-rounds-magazine-ammo-type-action-action-delivery-target-effects-3-damage-amount` | `ammo_type.action.action_delivery.target_effects.3.damage.amount` | 8 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / piercing-shotgun-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/combat-shotgun`, `gun/shotgun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-piercing-shotgun-shell-magazine-size` | `magazine_size` | 10 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | True |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-radius` | `ammo_type.action.1.action_delivery.target_effects.action.radius` | 2.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-repeat-count` | `ammo_type.action.1.action_delivery.target_effects.action.repeat_count` | 18 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-action-delivery-starting-speed` | `ammo_type.action.1.action_delivery.target_effects.action.action_delivery.starting_speed` | 1.2 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-piercing-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-action-delivery-starting-speed-deviation` | `ammo_type.action.1.action_delivery.target_effects.action.action_delivery.starting_speed_deviation` | 0.1 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / railgun-ammo

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/railgun-turret`, `gun/railgun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-railgun-ammo-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-clamp-position` | `ammo_type.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-action-range` | `ammo_type.action.range` | 50 | tiles | Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-action-width` | `ammo_type.action.width` | 1 |  | Width. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-railgun-ammo-ammo-type-action-action-delivery-target-effects-damage-amount` | `ammo_type.action.action_delivery.target_effects.damage.amount` | 10000 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / rocket

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/rocket-turret`, `gun/rocket-launcher`, `gun/spidertron-rocket-launcher-1`, `gun/spidertron-rocket-launcher-2`, `gun/spidertron-rocket-launcher-3`, `gun/spidertron-rocket-launcher-4`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-rocket-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-rocket-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 0.1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / shotgun-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/combat-shotgun`, `gun/shotgun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-shotgun-shell-magazine-size` | `magazine_size` | 10 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | True |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-radius` | `ammo_type.action.1.action_delivery.target_effects.action.radius` | 2.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-repeat-count` | `ammo_type.action.1.action_delivery.target_effects.action.repeat_count` | 12 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-ammo-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-action-delivery-starting-speed` | `ammo_type.action.1.action_delivery.target_effects.action.action_delivery.starting_speed` | 1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-shotgun-shell-ammo-type-action-1-action-delivery-target-effects-action-action-delivery-starting-speed-deviation` | `ammo_type.action.1.action_delivery.target_effects.action.action_delivery.starting_speed_deviation` | 0.1 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / tesla-ammo

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/teslagun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-tesla-ammo-magazine-size` | `magazine_size` | 10 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-action-action-delivery-target-effects-2-action-action-delivery-max-length` | `ammo_type.action.action_delivery.target_effects.2.action.action_delivery.max_length` | 30 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-tesla-ammo-ammo-type-action-action-delivery-target-effects-2-action-action-delivery-duration` | `ammo_type.action.action_delivery.target_effects.2.action.action_delivery.duration` | 30 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `default_import_location`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `stack_size`, `subgroup`, `type`. See exclusion policy below.

## ammo / uranium-cannon-shell

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `gun/tank-cannon`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-uranium-cannon-shell-magazine-size` | `magazine_size` | 1 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-ammo-type-clamp-position` | `ammo_type.clamp_position` | True |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1.25 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-cannon-shell-ammo-type-action-action-delivery-starting-speed` | `ammo_type.action.action_delivery.starting_speed` | 1 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `pictures`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## ammo / uranium-rounds-magazine

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo-turret/gun-turret`, `gun/pistol`, `gun/submachine-gun`, `gun/tank-machine-gun`, `gun/vehicle-machine-gun`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-ammo-uranium-rounds-magazine-magazine-size` | `magazine_size` | 10 |  | Shots per ammunition item. Shared by every weapon using this ammo. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-reload-time` | `reload_time` | 0 | ticks | Reload time. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-shoot-protected` | `shoot_protected` | False |  | Shoot protected. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-ammo-type-clamp-position` | `ammo_type.clamp_position` | False |  | Clamp position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-ammo-type-consumption-modifier` | `ammo_type.consumption_modifier` | 1 |  | Consumption modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-ammo-type-cooldown-modifier` | `ammo_type.cooldown_modifier` | 1 |  | Cooldown modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-ammo-type-force-clamp-to-max-range` | `ammo_type.force_clamp_to_max_range` | False |  | Force clamp to max range. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-ammo-type-range-modifier` | `ammo_type.range_modifier` | 1 |  | Range modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-ammo-uranium-rounds-magazine-ammo-type-action-action-delivery-target-effects-3-damage-amount` | `ammo_type.action.action_delivery.target_effects.3.damage.amount` | 24 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `ammo_category`, `drop_sound`, `icon`, `inventory_move_sound`, `name`, `order`, `pick_sound`, `pictures`, `stack_size`, `subgroup`, `type`, `weight`. See exclusion policy below.

## projectile / atomic-bomb-ground-zero-projectile

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/atomic-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-bomb-ground-zero-projectile-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-action-1-radius` | `action.1.radius` | 3 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-ground-zero-projectile-action-1-action-delivery-target-effects-damage-amount` | `action.1.action_delivery.target_effects.damage.amount` | 100 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `speed_modifier`, `type`. See exclusion policy below.

## projectile / atomic-bomb-wave

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/atomic-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-bomb-wave-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-bomb-wave-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-action-1-radius` | `action.1.radius` | 3 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-action-1-action-delivery-target-effects-damage-amount` | `action.1.action_delivery.target_effects.damage.amount` | 400 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `speed_modifier`, `type`. See exclusion policy below.

## projectile / atomic-bomb-wave-spawns-cluster-nuke-explosion

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/atomic-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-acceleration` | `acceleration` | 0.001 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-cluster-nuke-explosion-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `flags`, `hidden`, `name`, `speed_modifier`, `type`. See exclusion policy below.

## projectile / atomic-bomb-wave-spawns-fire-smoke-explosion

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/atomic-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-fire-smoke-explosion-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `flags`, `hidden`, `name`, `speed_modifier`, `type`. See exclusion policy below.

## projectile / atomic-bomb-wave-spawns-nuclear-smoke

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/atomic-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuclear-smoke-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `flags`, `hidden`, `name`, `speed_modifier`, `type`. See exclusion policy below.

## projectile / atomic-bomb-wave-spawns-nuke-shockwave-explosion

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/atomic-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-bomb-wave-spawns-nuke-shockwave-explosion-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `flags`, `hidden`, `name`, `speed_modifier`, `type`. See exclusion policy below.

## projectile / atomic-rocket

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/atomic-bomb`, `reactor/nuclear-reactor`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-atomic-rocket-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-atomic-rocket-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-turn-speed` | `turn_speed` | 0.003 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | True |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-1-radius` | `action.action_delivery.target_effects.1.radius` | 9 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-10-damage-amount` | `action.action_delivery.target_effects.10.damage.amount (base: action.action_delivery.target_effects.7.damage.amount)` | 400 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-13-radius` | `action.action_delivery.target_effects.13.radius (base: action.action_delivery.target_effects.10.radius)` | 14 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-15-action-radius` | `action.action_delivery.target_effects.15.action.radius (base: action.action_delivery.target_effects.12.action.radius)` | 7 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-15-action-repeat-count` | `action.action_delivery.target_effects.15.action.repeat_count (base: action.action_delivery.target_effects.12.action.repeat_count)` | 1000 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-15-action-action-delivery-starting-speed` | `action.action_delivery.target_effects.15.action.action_delivery.starting_speed (base: action.action_delivery.target_effects.12.action.action_delivery.starting_speed)` | 0.48 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-15-action-action-delivery-starting-speed-deviation` | `action.action_delivery.target_effects.15.action.action_delivery.starting_speed_deviation (base: action.action_delivery.target_effects.12.action.action_delivery.starting_speed_deviation)` | 0.075 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-16-action-radius` | `action.action_delivery.target_effects.16.action.radius (base: action.action_delivery.target_effects.13.action.radius)` | 35 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-16-action-repeat-count` | `action.action_delivery.target_effects.16.action.repeat_count (base: action.action_delivery.target_effects.13.action.repeat_count)` | 1000 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-16-action-action-delivery-starting-speed` | `action.action_delivery.target_effects.16.action.action_delivery.starting_speed (base: action.action_delivery.target_effects.13.action.action_delivery.starting_speed)` | 0.35 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-16-action-action-delivery-starting-speed-deviation` | `action.action_delivery.target_effects.16.action.action_delivery.starting_speed_deviation (base: action.action_delivery.target_effects.13.action.action_delivery.starting_speed_deviation)` | 0.075 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-17-action-radius` | `action.action_delivery.target_effects.17.action.radius (base: action.action_delivery.target_effects.14.action.radius)` | 26 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-17-action-repeat-count` | `action.action_delivery.target_effects.17.action.repeat_count (base: action.action_delivery.target_effects.14.action.repeat_count)` | 1000 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-17-action-action-delivery-starting-speed` | `action.action_delivery.target_effects.17.action.action_delivery.starting_speed (base: action.action_delivery.target_effects.14.action.action_delivery.starting_speed)` | 0.35 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-17-action-action-delivery-starting-speed-deviation` | `action.action_delivery.target_effects.17.action.action_delivery.starting_speed_deviation (base: action.action_delivery.target_effects.14.action.action_delivery.starting_speed_deviation)` | 0.075 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-18-action-radius` | `action.action_delivery.target_effects.18.action.radius (base: action.action_delivery.target_effects.15.action.radius)` | 4 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-18-action-repeat-count` | `action.action_delivery.target_effects.18.action.repeat_count (base: action.action_delivery.target_effects.15.action.repeat_count)` | 700 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-18-action-action-delivery-starting-speed` | `action.action_delivery.target_effects.18.action.action_delivery.starting_speed (base: action.action_delivery.target_effects.15.action.action_delivery.starting_speed)` | 0.325 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-18-action-action-delivery-starting-speed-deviation` | `action.action_delivery.target_effects.18.action.action_delivery.starting_speed_deviation (base: action.action_delivery.target_effects.15.action.action_delivery.starting_speed_deviation)` | 0.075 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-19-action-radius` | `action.action_delivery.target_effects.19.action.radius (base: action.action_delivery.target_effects.16.action.radius)` | 8 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-19-action-repeat-count` | `action.action_delivery.target_effects.19.action.repeat_count (base: action.action_delivery.target_effects.16.action.repeat_count)` | 1000 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-19-action-action-delivery-starting-speed` | `action.action_delivery.target_effects.19.action.action_delivery.starting_speed (base: action.action_delivery.target_effects.16.action.action_delivery.starting_speed)` | 0.325 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-19-action-action-delivery-starting-speed-deviation` | `action.action_delivery.target_effects.19.action.action_delivery.starting_speed_deviation (base: action.action_delivery.target_effects.16.action.action_delivery.starting_speed_deviation)` | 0.075 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-20-action-radius` | `action.action_delivery.target_effects.20.action.radius (base: action.action_delivery.target_effects.17.action.radius)` | 26 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-20-action-repeat-count` | `action.action_delivery.target_effects.20.action.repeat_count (base: action.action_delivery.target_effects.17.action.repeat_count)` | 300 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-20-action-action-delivery-starting-speed` | `action.action_delivery.target_effects.20.action.action_delivery.starting_speed (base: action.action_delivery.target_effects.17.action.action_delivery.starting_speed)` | 0.325 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-20-action-action-delivery-starting-speed-deviation` | `action.action_delivery.target_effects.20.action.action_delivery.starting_speed_deviation (base: action.action_delivery.target_effects.17.action.action_delivery.starting_speed_deviation)` | 0.075 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-21-action-radius` | `action.action_delivery.target_effects.21.action.radius (base: action.action_delivery.target_effects.18.action.radius)` | 8 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-atomic-rocket-action-action-delivery-target-effects-21-action-repeat-count` | `action.action_delivery.target_effects.21.action.repeat_count (base: action.action_delivery.target_effects.18.action.repeat_count)` | 10 |  | Number of applications/spawns. Large counts can exhaust memory or CPU. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / cannon-projectile

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/cannon-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-cannon-projectile-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-cannon-projectile-piercing-damage` | `piercing_damage` | 1000 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 1000 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cannon-projectile-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.2.damage.amount` | 100 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `collision_box`, `final_action`, `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## projectile / capture-robot-rocket

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/capture-robot-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-capture-robot-rocket-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-capture-robot-rocket-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-capture-robot-rocket-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-capture-robot-rocket-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-capture-robot-rocket-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-capture-robot-rocket-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-capture-robot-rocket-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `animation`, `enable_drawing_with_mask`, `flags`, `hidden`, `name`, `rotatable`, `smoke`, `type`. See exclusion policy below.

## projectile / cliff-explosives

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/cliff-explosives`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-cliff-explosives-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-cliff-explosives-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-action-1-action-delivery-target-effects-3-radius` | `action.1.action_delivery.target_effects.3.radius` | 1.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cliff-explosives-action-1-action-delivery-target-effects-5-radius` | `action.1.action_delivery.target_effects.5.radius` | 2 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `shadow`, `type`. See exclusion policy below.

## projectile / cluster-grenade

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/cluster-grenade`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-cluster-grenade-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-cluster-grenade-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-action-2-cluster-count` | `action.2.cluster_count` | 7 |  | Cluster count. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-action-2-distance` | `action.2.distance` | 4 | tiles | Distance. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-action-2-distance-deviation` | `action.2.distance_deviation` | 3 |  | Distance deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-action-2-action-delivery-starting-speed` | `action.2.action_delivery.starting_speed` | 0.25 |  | Starting speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-action-2-action-delivery-starting-speed-deviation` | `action.2.action_delivery.starting_speed_deviation` | 0.3 |  | Starting speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-cluster-grenade-action-2-action-delivery-direction-deviation` | `action.2.action_delivery.direction_deviation` | 0.6 |  | Direction deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `shadow`, `type`. See exclusion policy below.

## projectile / defender-capsule

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/defender-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-defender-capsule-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-defender-capsule-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-defender-capsule-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-defender-capsule-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-defender-capsule-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-defender-capsule-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-defender-capsule-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `animation`, `enable_drawing_with_mask`, `flags`, `hidden`, `light`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / destroyer-capsule

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/destroyer-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-destroyer-capsule-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-destroyer-capsule-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-destroyer-capsule-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-destroyer-capsule-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-destroyer-capsule-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-destroyer-capsule-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-destroyer-capsule-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `animation`, `enable_drawing_with_mask`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / distractor-capsule

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/distractor-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-distractor-capsule-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-distractor-capsule-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-distractor-capsule-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-distractor-capsule-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-distractor-capsule-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-distractor-capsule-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-distractor-capsule-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `animation`, `enable_drawing_with_mask`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / explosive-cannon-projectile

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/explosive-cannon-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-explosive-cannon-projectile-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-explosive-cannon-projectile-piercing-damage` | `piercing_damage` | 100 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 180 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-final-action-action-delivery-target-effects-2-action-radius` | `final_action.action_delivery.target_effects.2.action.radius` | 4 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-final-action-action-delivery-target-effects-2-action-action-delivery-target-effects-1-damage-amount` | `final_action.action_delivery.target_effects.2.action.action_delivery.target_effects.1.damage.amount` | 300 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-cannon-projectile-final-action-action-delivery-target-effects-5-radius` | `final_action.action_delivery.target_effects.5.radius` | 2 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `collision_box`, `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## projectile / explosive-rocket

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/explosive-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-explosive-rocket-acceleration` | `acceleration` | 0.01 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-explosive-rocket-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-turn-speed` | `turn_speed` | 0.003 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | True |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.2.damage.amount` | 50 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-action-action-delivery-target-effects-5-radius` | `action.action_delivery.target_effects.5.radius` | 3.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-action-action-delivery-target-effects-6-action-radius` | `action.action_delivery.target_effects.6.action.radius` | 6.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-rocket-action-action-delivery-target-effects-6-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.6.action.action_delivery.target_effects.1.damage.amount` | 100 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / explosive-uranium-cannon-projectile

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/explosive-uranium-cannon-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-explosive-uranium-cannon-projectile-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-explosive-uranium-cannon-projectile-piercing-damage` | `piercing_damage` | 150 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 350 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-final-action-action-delivery-target-effects-2-action-radius` | `final_action.action_delivery.target_effects.2.action.radius` | 4.25 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-final-action-action-delivery-target-effects-2-action-action-delivery-target-effects-1-damage-amount` | `final_action.action_delivery.target_effects.2.action.action_delivery.target_effects.1.damage.amount` | 315 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-explosive-uranium-cannon-projectile-final-action-action-delivery-target-effects-5-radius` | `final_action.action_delivery.target_effects.5.radius` | 3.25 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `collision_box`, `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## projectile / grenade

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/grenade`, `projectile/cluster-grenade`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-grenade-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-grenade-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-action-1-action-delivery-target-effects-4-radius` | `action.1.action_delivery.target_effects.4.radius` | 2.25 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-action-2-radius` | `action.2.radius` | 6.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-grenade-action-2-action-delivery-target-effects-1-damage-amount` | `action.2.action_delivery.target_effects.1.damage.amount` | 35 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `light`, `name`, `shadow`, `type`. See exclusion policy below.

## projectile / piercing-shotgun-pellet

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/piercing-shotgun-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-piercing-shotgun-pellet-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-piercing-shotgun-pellet-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-piercing-shotgun-pellet-hit-at-collision-position` | `hit_at_collision_position` | True |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-piercing-shotgun-pellet-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-piercing-shotgun-pellet-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-piercing-shotgun-pellet-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-piercing-shotgun-pellet-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-piercing-shotgun-pellet-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.2.damage.amount` | 12 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `collision_box`, `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## projectile / poison-capsule

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/poison-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-poison-capsule-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-poison-capsule-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-poison-capsule-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-poison-capsule-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-poison-capsule-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-poison-capsule-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-poison-capsule-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `action`, `animation`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / rocket

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-rocket-acceleration` | `acceleration` | 0.01 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-rocket-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-turn-speed` | `turn_speed` | 0.003 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | True |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.2.damage.amount` | 200 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-rocket-action-action-delivery-target-effects-5-radius` | `action.action_delivery.target_effects.5.radius` | 1.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / shotgun-pellet

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/shotgun-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-shotgun-pellet-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-shotgun-pellet-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-shotgun-pellet-hit-at-collision-position` | `hit_at_collision_position` | True |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-shotgun-pellet-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-shotgun-pellet-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-shotgun-pellet-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-shotgun-pellet-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-shotgun-pellet-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.2.damage.amount` | 8 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `collision_box`, `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## projectile / slowdown-capsule

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/slowdown-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-slowdown-capsule-acceleration` | `acceleration` | 0.005 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-slowdown-capsule-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-slowdown-capsule-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-slowdown-capsule-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-slowdown-capsule-piercing-damage` | `piercing_damage` | 0 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-slowdown-capsule-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-slowdown-capsule-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-slowdown-capsule-action-2-radius` | `action.2.radius` | 9 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `shadow`, `smoke`, `type`. See exclusion policy below.

## projectile / uranium-cannon-projectile

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/uranium-cannon-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-projectile-uranium-cannon-projectile-acceleration` | `acceleration` | 0 |  | Acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-direction-only` | `direction_only` | False |  | Direction only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-hit-at-collision-position` | `hit_at_collision_position` | False |  | Hit at collision position. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-projectile-uranium-cannon-projectile-piercing-damage` | `piercing_damage` | 2200 |  | Piercing damage. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-turn-speed` | `turn_speed` | 1 | turns/tick | Turn speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-turning-speed-increases-exponentially-with-projectile-speed` | `turning_speed_increases_exponentially_with_projectile_speed` | False |  | Turning speed increases exponentially with projectile speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 2000 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-projectile-uranium-cannon-projectile-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.2.damage.amount` | 200 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `collision_box`, `final_action`, `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## artillery-projectile / artillery-projectile

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/artillery-shell`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-artillery-projectile-artillery-projectile-reveal-map` | `reveal_map` | True |  | Reveal map. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-artillery-projectile-artillery-projectile-action-action-delivery-target-effects-1-action-radius` | `action.action_delivery.target_effects.1.action.radius` | 4 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-artillery-projectile-artillery-projectile-action-action-delivery-target-effects-1-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.action.action_delivery.target_effects.1.damage.amount` | 1000 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-artillery-projectile-artillery-projectile-action-action-delivery-target-effects-1-action-action-delivery-target-effects-2-damage-amount` | `action.action_delivery.target_effects.1.action.action_delivery.target_effects.2.damage.amount` | 1000 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-artillery-projectile-artillery-projectile-final-action-action-delivery-target-effects-3-radius` | `final_action.action_delivery.target_effects.3.radius` | 3.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `chart_picture`, `flags`, `height_from_ground`, `hidden`, `map_color`, `name`, `picture`, `shadow`, `type`. See exclusion policy below.

## beam / chain-tesla-gun-beam-bounce

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `chain-active-trigger/chain-tesla-gun-chain`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-chain-tesla-gun-beam-bounce-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-gun-beam-bounce-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-gun-beam-bounce-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 30 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-gun-beam-bounce-action-action-delivery-target-effects-2-distance` | `action.action_delivery.target_effects.2.distance` | 0.25 | tiles | Distance. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `target_offset`, `type`, `width`, `working_sound`. See exclusion policy below.

## beam / chain-tesla-gun-beam-start

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/tesla-ammo`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-chain-tesla-gun-beam-start-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-gun-beam-start-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-gun-beam-start-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 30 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-gun-beam-start-action-action-delivery-target-effects-2-distance` | `action.action_delivery.target_effects.2.distance` | 0.5 | tiles | Distance. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `target_offset`, `type`, `width`, `working_sound`. See exclusion policy below.

## beam / chain-tesla-turret-beam-bounce

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `chain-active-trigger/chain-tesla-turret-chain`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-chain-tesla-turret-beam-bounce-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-turret-beam-bounce-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-turret-beam-bounce-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 120 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-turret-beam-bounce-action-action-delivery-target-effects-2-distance` | `action.action_delivery.target_effects.2.distance` | 0.25 | tiles | Distance. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `target_offset`, `type`, `width`, `working_sound`. See exclusion policy below.

## beam / chain-tesla-turret-beam-start

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `electric-turret/tesla-turret`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-chain-tesla-turret-beam-start-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-turret-beam-start-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-turret-beam-start-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 120 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-chain-tesla-turret-beam-start-action-action-delivery-target-effects-2-distance` | `action.action_delivery.target_effects.2.distance` | 0.5 | tiles | Distance. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `target_offset`, `type`, `width`, `working_sound`. See exclusion policy below.

## beam / electric-beam

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `combat-robot/destroyer`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-electric-beam-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-electric-beam-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-electric-beam-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 10 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `target_offset`, `type`, `width`, `working_sound`. See exclusion policy below.

## beam / electric-beam-no-sound

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `active-defense-equipment/discharge-defense-equipment`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-electric-beam-no-sound-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-electric-beam-no-sound-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-electric-beam-no-sound-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 10 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `target_offset`, `type`, `width`. See exclusion policy below.

## beam / laser-beam

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `active-defense-equipment/personal-laser-defense-equipment`, `combat-robot/distractor`, `electric-turret/laser-turret`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-beam-laser-beam-action-triggered-automatically` | `action_triggered_automatically` | False |  | Action triggered automatically. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-laser-beam-damage-interval` | `damage_interval` | 20 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-beam-laser-beam-action-action-delivery-target-effects-1-damage-amount` | `action.action_delivery.target_effects.1.damage.amount` | 10 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `graphics_set`, `hidden`, `name`, `random_target_offset`, `type`, `width`, `working_sound`. See exclusion policy below.

## stream / flamethrower-fire-stream

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `fluid-turret/flamethrower-turret`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-stream-flamethrower-fire-stream-particle-buffer-size` | `particle_buffer_size` | 90 |  | Particle buffer size. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-particle-horizontal-speed` | `particle_horizontal_speed` | 0.25 | tiles/tick | Particle horizontal speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-particle-horizontal-speed-deviation` | `particle_horizontal_speed_deviation` | 0.025 | tiles/tick | Particle horizontal speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-particle-spawn-interval` | `particle_spawn_interval` | 2 |  | Particle spawn interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-particle-spawn-timeout` | `particle_spawn_timeout` | 8 |  | Particle spawn timeout. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-particle-vertical-acceleration` | `particle_vertical_acceleration` | 0.003 |  | Particle vertical acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-target-initial-position-only` | `target_initial_position_only` | False |  | Target initial position only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-action-1-radius` | `action.1.radius` | 2.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-flamethrower-fire-stream-action-1-action-delivery-target-effects-2-damage-amount` | `action.1.action_delivery.target_effects.2.damage.amount` | 3 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `particle`, `particle_end_alpha`, `particle_fade_out_threshold`, `particle_loop_exit_threshold`, `particle_loop_frame_count`, `particle_start_alpha`, `particle_start_scale`, `shadow`, `smoke_sources`, `spine_animation`, `type`. See exclusion policy below.

## stream / handheld-flamethrower-fire-stream

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/flamethrower-ammo`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-stream-handheld-flamethrower-fire-stream-particle-buffer-size` | `particle_buffer_size` | 65 |  | Particle buffer size. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-particle-horizontal-speed` | `particle_horizontal_speed` | 0.25 | tiles/tick | Particle horizontal speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-particle-horizontal-speed-deviation` | `particle_horizontal_speed_deviation` | 0.025 | tiles/tick | Particle horizontal speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-particle-spawn-interval` | `particle_spawn_interval` | 2 |  | Particle spawn interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-particle-spawn-timeout` | `particle_spawn_timeout` | 2 |  | Particle spawn timeout. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-particle-vertical-acceleration` | `particle_vertical_acceleration` | 0.003 |  | Particle vertical acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-target-initial-position-only` | `target_initial_position_only` | False |  | Target initial position only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-action-1-radius` | `action.1.radius` | 2.5 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-action-1-action-delivery-target-effects-2-damage-amount` | `action.1.action_delivery.target_effects.2.damage.amount` | 2 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-handheld-flamethrower-fire-stream-action-2-action-delivery-target-effects-1-initial-ground-flame-count` | `action.2.action_delivery.target_effects.1.initial_ground_flame_count` | 2 |  | Initial ground flame count. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `particle`, `particle_end_alpha`, `particle_fade_out_threshold`, `particle_loop_exit_threshold`, `particle_loop_frame_count`, `particle_start_alpha`, `particle_start_scale`, `shadow`, `smoke_sources`, `spine_animation`, `type`. See exclusion policy below.

## stream / tank-flamethrower-fire-stream

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/flamethrower-ammo`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-stream-tank-flamethrower-fire-stream-particle-buffer-size` | `particle_buffer_size` | 65 |  | Particle buffer size. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-particle-horizontal-speed` | `particle_horizontal_speed` | 0.45 | tiles/tick | Particle horizontal speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-particle-horizontal-speed-deviation` | `particle_horizontal_speed_deviation` | 0.045 | tiles/tick | Particle horizontal speed deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-particle-spawn-interval` | `particle_spawn_interval` | 2 |  | Particle spawn interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-particle-spawn-timeout` | `particle_spawn_timeout` | 2 |  | Particle spawn timeout. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-particle-vertical-acceleration` | `particle_vertical_acceleration` | 0.0015 |  | Particle vertical acceleration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-target-initial-position-only` | `target_initial_position_only` | False |  | Target initial position only. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-action-1-radius` | `action.1.radius` | 4 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-stream-tank-flamethrower-fire-stream-action-1-action-delivery-target-effects-1-damage-amount` | `action.1.action_delivery.target_effects.1.damage.amount` | 7 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `particle`, `particle_end_alpha`, `particle_fade_out_threshold`, `particle_loop_exit_threshold`, `particle_loop_frame_count`, `particle_start_alpha`, `particle_start_scale`, `shadow`, `smoke_sources`, `spine_animation`, `type`. See exclusion policy below.

## fire / fire-flame

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `stream/flamethrower-fire-stream`, `stream/handheld-flamethrower-fire-stream`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-fire-fire-flame-add-fuel-cooldown` | `add_fuel_cooldown` | 10 | ticks | Add fuel cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-damage-multiplier-decrease-per-tick` | `damage_multiplier_decrease_per_tick` | 0.005 |  | Damage multiplier decrease per tick. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-damage-multiplier-increase-per-added-fuel` | `damage_multiplier_increase_per_added_fuel` | 1 |  | Damage multiplier increase per added fuel. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-initial-lifetime` | `initial_lifetime` | 120 | ticks | Initial fire lifetime. Kept at or below maximum lifetime when changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-lifetime-increase-by` | `lifetime_increase_by` | 150 | ticks | Lifetime increase by. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-lifetime-increase-cooldown` | `lifetime_increase_cooldown` | 4 | ticks | Lifetime increase cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-maximum-damage-multiplier` | `maximum_damage_multiplier` | 6 |  | Maximum damage multiplier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-maximum-lifetime` | `maximum_lifetime` | 1800 | ticks | Maximum lifetime. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-maximum-spread-count` | `maximum_spread_count` | 100 |  | Maximum spread count. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-spread-delay` | `spread_delay` | 300 | ticks | Spread delay. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-spread-delay-deviation` | `spread_delay_deviation` | 180 | ticks | Spread delay deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-tree-dying-factor` | `tree_dying_factor` | 0 |  | Tree dying factor. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-damage-per-tick-amount` | `damage_per_tick.amount` | 0.2166666666666667 | HP/tick | Native damage-per-tick amount; scheduling follows the native damage interval. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `burnt_patch_alpha_default`, `burnt_patch_alpha_variations`, `burnt_patch_lifetime`, `burnt_patch_pictures`, `delay_between_initial_flames`, `emissions_per_second`, `fade_in_duration`, `fade_out_duration`, `flags`, `flame_alpha`, `flame_alpha_deviation`, `hidden`, `light`, `light_size_modifier_maximum`, `light_size_modifier_per_flame`, `name`, `on_fuel_added_action`, `pictures`, `smoke`, `smoke_source_pictures`, `spawn_entity`, `type`, `working_sound`. See exclusion policy below.

## fire / fire-flame-on-tree

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `fire/fire-flame`, `fire/fire-flame-on-tree`, `sticker/fire-sticker`, `tree/ashland-lichen-tree-flaming`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-fire-fire-flame-on-tree-add-fuel-cooldown` | `add_fuel_cooldown` | 10 | ticks | Add fuel cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-damage-multiplier-decrease-per-tick` | `damage_multiplier_decrease_per_tick` | 0.0 |  | Damage multiplier decrease per tick. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-damage-multiplier-increase-per-added-fuel` | `damage_multiplier_increase_per_added_fuel` | 0.0 |  | Damage multiplier increase per added fuel. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-initial-lifetime` | `initial_lifetime` | 300 | ticks | Initial fire lifetime. Kept at or below maximum lifetime when changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-lifetime-increase-by` | `lifetime_increase_by` | 20 | ticks | Lifetime increase by. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-lifetime-increase-cooldown` | `lifetime_increase_cooldown` | 10 | ticks | Lifetime increase cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-maximum-damage-multiplier` | `maximum_damage_multiplier` | 1.0 |  | Maximum damage multiplier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-maximum-lifetime` | `maximum_lifetime` | 4294967295 | ticks | Maximum lifetime. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-maximum-spread-count` | `maximum_spread_count` | 100 |  | Maximum spread count. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-spread-delay` | `spread_delay` | 300 | ticks | Spread delay. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-spread-delay-deviation` | `spread_delay_deviation` | 180 | ticks | Spread delay deviation. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-tree-dying-factor` | `tree_dying_factor` | 0.8 |  | Tree dying factor. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-fire-fire-flame-on-tree-damage-per-tick-amount` | `damage_per_tick.amount` | 0.5833333333333334 | HP/tick | Native damage-per-tick amount; scheduling follows the native damage interval. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `delay_between_initial_flames`, `emissions_per_second`, `fade_in_duration`, `fade_out_duration`, `flags`, `flame_alpha`, `flame_alpha_deviation`, `hidden`, `light`, `localised_name`, `name`, `pictures`, `small_tree_fire_pictures`, `smoke`, `smoke_fade_in_duration`, `smoke_fade_out_duration`, `smoke_source_pictures`, `spawn_entity`, `type`, `working_sound`. See exclusion policy below.

## smoke-with-trigger / poison-cloud

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/poison-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-smoke-with-trigger-poison-cloud-action-cooldown` | `action_cooldown` | 30 | ticks | Action cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-smoke-with-trigger-poison-cloud-attach-to-target` | `attach_to_target` | False |  | Attach to target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-smoke-with-trigger-poison-cloud-duration` | `duration` | 1200 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-smoke-with-trigger-poison-cloud-fade-when-attachment-is-destroyed` | `fade_when_attachment_is_destroyed` | False |  | Fade when attachment is destroyed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-smoke-with-trigger-poison-cloud-action-action-delivery-target-effects-action-radius` | `action.action_delivery.target_effects.action.radius` | 11 | tiles | Action radius in tiles. Large areas and repeated actions can be expensive. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-smoke-with-trigger-poison-cloud-action-action-delivery-target-effects-action-action-delivery-target-effects-damage-amount` | `action.action_delivery.target_effects.action.action_delivery.target_effects.damage.amount` | 8 | HP | Absolute damage per application, before native modifiers and resistances. Negative values can heal. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `affected_by_wind`, `animation`, `color`, `created_effect`, `cyclic`, `fade_away_duration`, `flags`, `hidden`, `name`, `particle_count`, `particle_distance_scale_factor`, `particle_duration_variation`, `particle_scale_factor`, `particle_spread`, `render_layer`, `show_when_smoke_off`, `spread_duration`, `spread_duration_variation`, `type`, `wave_distance`, `wave_speed`. See exclusion policy below.

## sticker / bioflux-speed-regen-sticker

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/bioflux`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-bioflux-speed-regen-sticker-damage-interval` | `damage_interval` | 15 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-duration-in-ticks` | `duration_in_ticks` | 960 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-bioflux-speed-regen-sticker-target-movement-modifier` | `target_movement_modifier` | 1.5 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-use-damage-substitute` | `use_damage_substitute` | False |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-bioflux-speed-regen-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-damage-per-tick-amount` | `damage_per_tick.amount` | -4 | HP/tick | Native damage-per-tick amount; scheduling follows the native damage interval. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `single_particle`, `type`. See exclusion policy below.

## sticker / bioflux-speed-regen-sticker-behind

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/bioflux`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-bioflux-speed-regen-sticker-behind-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-duration-in-ticks` | `duration_in_ticks` | 960 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-target-movement-modifier` | `target_movement_modifier` | 1 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-bioflux-speed-regen-sticker-behind-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `render_layer`, `single_particle`, `type`. See exclusion policy below.

## sticker / fire-sticker

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `stream/flamethrower-fire-stream`, `stream/handheld-flamethrower-fire-stream`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-fire-sticker-damage-interval` | `damage_interval` | 10 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-duration-in-ticks` | `duration_in_ticks` | 1800 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-fire-spread-radius` | `fire_spread_radius` | 0.75 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-fire-sticker-target-movement-modifier` | `target_movement_modifier` | 0.8 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-fire-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-fire-sticker-damage-per-tick-amount` | `damage_per_tick.amount` | 16.666666666666668 | HP/tick | Native damage-per-tick amount; scheduling follows the native damage interval. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `spread_fire_entity`, `type`. See exclusion policy below.

## sticker / jellynut-speed-sticker

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/jelly`, `capsule/jellynut`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-jellynut-speed-sticker-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-duration-in-ticks` | `duration_in_ticks` | 720 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-jellynut-speed-sticker-target-movement-modifier` | `target_movement_modifier` | 1.5 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-jellynut-speed-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `single_particle`, `type`. See exclusion policy below.

## sticker / jellynut-speed-sticker-behind

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/jelly`, `capsule/jellynut`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-jellynut-speed-sticker-behind-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-duration-in-ticks` | `duration_in_ticks` | 720 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-jellynut-speed-sticker-behind-target-movement-modifier` | `target_movement_modifier` | 1 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-jellynut-speed-sticker-behind-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-jellynut-speed-sticker-behind-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `render_layer`, `single_particle`, `type`. See exclusion policy below.

## sticker / shotgun-impact-sticker

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/piercing-shotgun-pellet`, `projectile/shotgun-pellet`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-shotgun-impact-sticker-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-duration-in-ticks` | `duration_in_ticks` | 100 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-shotgun-impact-sticker-target-movement-modifier` | `target_movement_modifier` | 1 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-target-movement-modifier-from` | `target_movement_modifier_from` | 0.5 |  | Target movement modifier from. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-target-movement-modifier-to` | `target_movement_modifier_to` | 1 |  | Target movement modifier to. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-shotgun-impact-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-shotgun-impact-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## sticker / slowdown-sticker

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/slowdown-capsule`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-slowdown-sticker-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-duration-in-ticks` | `duration_in_ticks` | 1800 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-slowdown-sticker-target-movement-modifier` | `target_movement_modifier` | 0.25 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-slowdown-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-slowdown-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `hidden`, `name`, `type`. See exclusion policy below.

## sticker / stun-sticker

Base game. Shared resource; changing it affects every consumer. 
Direct combat consumers: `active-defense-equipment/discharge-defense-equipment`, `land-mine/land-mine`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-stun-sticker-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-duration-in-ticks` | `duration_in_ticks` | 180 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-stun-sticker-target-movement-modifier` | `target_movement_modifier` | 0 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-stun-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-stun-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## sticker / tesla-turret-slow

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `beam/chain-tesla-gun-beam-bounce`, `beam/chain-tesla-gun-beam-start`, `beam/chain-tesla-turret-beam-bounce`, `beam/chain-tesla-turret-beam-start`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-tesla-turret-slow-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-duration-in-ticks` | `duration_in_ticks` | 120 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-tesla-turret-slow-target-movement-modifier` | `target_movement_modifier` | 0.5 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-slow-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-tesla-turret-slow-vehicle-speed-modifier` | `vehicle_speed_modifier` | 0.75 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## sticker / tesla-turret-stun

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `beam/chain-tesla-gun-beam-bounce`, `beam/chain-tesla-gun-beam-start`, `beam/chain-tesla-turret-beam-bounce`, `beam/chain-tesla-turret-beam-start`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-tesla-turret-stun-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-duration-in-ticks` | `duration_in_ticks` | 30 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-tesla-turret-stun-target-movement-modifier` | `target_movement_modifier` | 0.05 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-tesla-turret-stun-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-tesla-turret-stun-vehicle-speed-modifier` | `vehicle_speed_modifier` | 0.25 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `flags`, `hidden`, `name`, `type`. See exclusion policy below.

## sticker / yumako-regen-sticker

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/yumako`, `capsule/yumako-mash`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-yumako-regen-sticker-damage-interval` | `damage_interval` | 15 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-duration-in-ticks` | `duration_in_ticks` | 720 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-yumako-regen-sticker-target-movement-modifier` | `target_movement_modifier` | 1 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-use-damage-substitute` | `use_damage_substitute` | False |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-yumako-regen-sticker-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-damage-per-tick-amount` | `damage_per_tick.amount` | -4 | HP/tick | Native damage-per-tick amount; scheduling follows the native damage interval. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `single_particle`, `type`. See exclusion policy below.

## sticker / yumako-regen-sticker-behind

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `capsule/yumako`, `capsule/yumako-mash`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-sticker-yumako-regen-sticker-behind-damage-interval` | `damage_interval` | 1 | ticks | Damage interval. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-duration-in-ticks` | `duration_in_ticks` | 720 | ticks | Duration in ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-fire-spread-cooldown` | `fire_spread_cooldown` | 30 |  | Fire spread cooldown. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-fire-spread-radius` | `fire_spread_radius` | 1 |  | Fire spread radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-ground-target` | `ground_target` | False |  | Ground target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-target-movement-max` | `target_movement_max` | -1 |  | Target movement max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-yumako-regen-sticker-behind-target-movement-modifier` | `target_movement_modifier` | 1 |  | Multiplier of target movement speed; zero immobilizes. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-use-damage-substitute` | `use_damage_substitute` | True |  | Use damage substitute. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-vehicle-friction-modifier` | `vehicle_friction_modifier` | 1 |  | Vehicle friction modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-sticker-yumako-regen-sticker-behind-vehicle-speed-max` | `vehicle_speed_max` | -1 |  | Vehicle speed max. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-sticker-yumako-regen-sticker-behind-vehicle-speed-modifier` | `vehicle_speed_modifier` | 1 |  | Vehicle speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `animation`, `flags`, `hidden`, `name`, `render_layer`, `single_particle`, `type`. See exclusion policy below.

## chain-active-trigger / chain-tesla-gun-chain

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `ammo/tesla-ammo`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-chain-active-trigger-chain-tesla-gun-chain-fork-chance` | `fork_chance` | 0.3 |  | Chance of an additional chain branch, from 0 to 1. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-fork-chance-increase-per-quality-level` | `fork_chance_increase_per_quality_level` | 0.05 |  | Fork chance increase per quality level. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-jump-delay-ticks` | `jump_delay_ticks` | 6 | ticks | Jump delay ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-max-forks` | `max_forks` | 4294967295 |  | Max forks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-max-forks-per-jump` | `max_forks_per_jump` | 1 |  | Max forks per jump. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-max-jumps` | `max_jumps` | 12 |  | Max jumps. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-max-range` | `max_range` | -1 | tiles | Maximum travel or chain distance; affects all consumers of this effect. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-max-range-per-jump` | `max_range_per_jump` | 12 | tiles | Max range per jump. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-action-action-delivery-max-length` | `action.action_delivery.max_length` | 12.5 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-gun-chain-action-action-delivery-duration` | `action.action_delivery.duration` | 30 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `name`, `type`. See exclusion policy below.

## chain-active-trigger / chain-tesla-turret-chain

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `electric-turret/tesla-turret`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-chain-active-trigger-chain-tesla-turret-chain-fork-chance` | `fork_chance` | 0.05 |  | Chance of an additional chain branch, from 0 to 1. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-fork-chance-increase-per-quality-level` | `fork_chance_increase_per_quality_level` | 0.05 |  | Fork chance increase per quality level. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-jump-delay-ticks` | `jump_delay_ticks` | 6 | ticks | Jump delay ticks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-max-forks` | `max_forks` | 4294967295 |  | Max forks. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-max-forks-per-jump` | `max_forks_per_jump` | 1 |  | Max forks per jump. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-max-jumps` | `max_jumps` | 10 |  | Max jumps. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. Large counts can exhaust CPU or memory. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-max-range` | `max_range` | -1 | tiles | Maximum travel or chain distance; affects all consumers of this effect. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-max-range-per-jump` | `max_range_per_jump` | 12 | tiles | Max range per jump. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-action-action-delivery-max-length` | `action.action_delivery.max_length` | 12.5 | tiles | Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-chain-active-trigger-chain-tesla-turret-chain-action-action-delivery-duration` | `action.action_delivery.duration` | 30 | ticks | Duration. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `name`, `type`. See exclusion policy below.

## capture-robot / capture-robot

Space Age only. Shared resource; changing it affects every consumer. 
Direct combat consumers: `projectile/capture-robot-rocket`.

| Setting | Exact property | Official default | Unit | Meaning |
| --- | --- | --- | --- | --- |
| `cr-capture-robot-capture-robot-alert-when-damaged` | `alert_when_damaged` | False |  | Alert when damaged. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-capture-speed` | `capture_speed` | 1 |  | Capture speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-create-ghost-on-death` | `create_ghost_on_death` | True |  | Create ghost on death. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-healing-per-tick` | `healing_per_tick` | 0 | HP/tick | Health regenerated per tick. Negative values cause health loss. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-is-military-target` | `is_military_target` | True |  | Is military target. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-max-health` | `max_health` | 60 | HP | Max health. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-max-speed` | `max_speed` | -1 | tiles/tick | Max speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. -1 preserves the native unlimited default. |
| `cr-capture-robot-capture-robot-overkill-fraction` | `overkill_fraction` | 0.05 |  | Overkill fraction. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-repair-speed-modifier` | `repair_speed_modifier` | 1 |  | Repair speed modifier. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-search-radius` | `search_radius` | 1 | tiles | Search radius. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-speed` | `speed` | 0.01 | tiles/tick | Speed. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-physical-decrease` | `resistances.physical.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-physical-percent` | `resistances.physical.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-impact-decrease` | `resistances.impact.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-impact-percent` | `resistances.impact.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-poison-decrease` | `resistances.poison.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-poison-percent` | `resistances.poison.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-explosion-decrease` | `resistances.explosion.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-explosion-percent` | `resistances.explosion.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-fire-decrease` | `resistances.fire.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-fire-percent` | `resistances.fire.percent` | 95 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-laser-decrease` | `resistances.laser.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-laser-percent` | `resistances.laser.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-acid-decrease` | `resistances.acid.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-acid-percent` | `resistances.acid.percent` | 90 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-electric-decrease` | `resistances.electric.decrease` | 0 | HP | Decrease. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |
| `cr-capture-robot-capture-robot-resistances-electric-percent` | `resistances.electric.percent` | 0 | % | Percent. Uses the native engine property; only this listed path is changed. Scope: shared resource; all consumers listed in PARAMETERS.md. |

Not exposed on this record: `capture_animation`, `collision_box`, `damaged_trigger_effect`, `destroy_action`, `dying_explosion`, `flags`, `hidden`, `hit_visualization_box`, `icon`, `name`, `order`, `selection_box`, `type`, `water_reflection`, `working_sound`. See exclusion policy below.

## Dependencies and exclusions

- Range changes raise embedded beam delivery length limits when they would otherwise truncate the configured range. Explicit delivery length overrides take precedence. Increasing a turret range raises an insufficient explicit preparation radius unless it is also configured. Shared projectile/ammo ranges are separate controls and never silently rewritten by a gun setting. Artillery targeting uses its shared gun; manual range coefficients belong to each artillery entity.
- Reversed min/max ranges are clamped with a log. Fire initial lifetime is clamped to its maximum if either changes. Impossible fluid-turret state overrides forced by the engine are omitted. Exponential projectile turning requires nonzero acceleration; otherwise that toggle is kept disabled and logged. The dependency repairs are listed in the runtime-free data-stage code.
- Graphics, sound, sprite/particle geometry, identifiers, references to other prototypes, collision masks, equipment grid/shape references and recipe/technology definitions are excluded. These cannot be meaningful independent numeric controls without changing resource structure. Omitted fields above are an audit inventory, not a claim that every numeric field is impossible.
- Inherited optional fields without a finite documented default, union-valued structures without a single independent numeric interpretation, and purely visual animation speeds are not fabricated. Native state-transition speeds are exposed only when the matching animation exists. The fluid turret always requires fuel before attacking, so the engine-forced start-state flag is omitted. Mech armor flight cannot be disabled independently of its collision/drawing boxes and is omitted; other armor flight toggles require space travel. Capsule warmup is excluded because nonzero warmup is invalid for capsule actions.
- Artillery and discharge remotes contain identifiers but no independent attack parameters. Their behavior is configured on artillery entities/gun and discharge equipment. Food use-on-self capsules are included for combat healing/buff research; spoilage and agricultural production are outside scope.
- Player character melee stats, enemy units/spawners/worms, hostile acid/demolisher effects not reachable from player combat resources, transport movement engines, crafting and general power generation equipment are outside this player-weapon/defense catalog. Shared player effects may still have other consumers; inspect the complete native reference graph before experiments.
- Shared resources are explicitly labeled. No per-weapon cloning of ammunition or projectiles is performed; modifying a shared ammo/beam/fire/sticker affects all its consumers, potentially including enemies or environmental fires. Weapon-local coefficients and embedded actions stay local.
- Startup settings apply to existing and newly placed entities. Inventory shrinkage can lose items; extreme ranges, radii, repeat counts and branching can exhaust memory/CPU. The million-tile spatial input guard is not a safety guarantee.
- The original gun-turret field-specific exclusions and conversions are retained. Default settings never materialize optional fields or normalize native data.
