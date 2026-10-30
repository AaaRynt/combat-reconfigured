-- Defaults are from Factorio 2.1.24 base data and the prototype API.
local float_max = 3.402823466e38
local uint32_max = 4294967295
-- A configuration guard for spatial queries, not an engine safety guarantee.
local distance_max = 1000000

local definitions = {
  {key = "range", default = 18, min = 0, max = distance_max, attack = "range"},
  {key = "min-range", default = 0, min = 0, max = distance_max, attack = "min_range"},
  {key = "prepare-range", default = -1, min = -1, max = distance_max, special = "prepare-range"},
  {key = "cooldown", default = 6, min = 0.001, max = uint32_max, attack = "cooldown"},
  {key = "warmup", type = "int-setting", default = 0, min = 0, max = uint32_max, attack = "warmup"},
  {key = "cooldown-deviation", default = 0, min = 0, max = 1, attack = "cooldown_deviation"},
  {key = "damage-modifier", default = 1, min = 0, max = float_max, attack = "damage_modifier"},
  {key = "ammo-consumption-modifier", default = 1, min = 0, max = float_max, attack = "ammo_consumption_modifier"},
  {key = "rotation-speed", default = 0.015, min = 0, max = 1, field = "rotation_speed", secondary = "rotation_speed_secondary"},
  {key = "preparing-time", default = 12.5, min = 1, max = uint32_max, duration = "preparing_speed"},
  {key = "folding-time", default = 12.5, min = 1, max = uint32_max, duration = "folding_speed"},
  {key = "inventory-size", type = "int-setting", default = 1, min = 1, max = 65535, field = "inventory_size"},
  {key = "automated-ammo-count", type = "int-setting", default = 10, min = 0, max = uint32_max, field = "automated_ammo_count"},
  {key = "prepare-with-no-ammo", type = "bool-setting", default = true, field = "prepare_with_no_ammo"},
  {key = "shoot-in-prepare-state", type = "bool-setting", default = false, field = "shoot_in_prepare_state"},
  {key = "start-attacking-only-when-can-shoot", type = "bool-setting", default = false, field = "start_attacking_only_when_can_shoot"},
  {key = "leave-attacking-if-shoot-fails", type = "bool-setting", default = true, field = "leave_attacking_if_shoot_fails"},
  {key = "can-retarget-while-starting-attack", type = "bool-setting", default = false, field = "can_retarget_while_starting_attack"},
  {key = "allow-turning-when-starting-attack", type = "bool-setting", default = false, field = "allow_turning_when_starting_attack"},
  {key = "range-mode", type = "string-setting", default = "center-to-center", allowed = {"center-to-center", "bounding-box-to-bounding-box", "center-to-bounding-box"}, attack = "range_mode"},
  {key = "health-penalty", default = 10, min = -float_max, max = float_max, attack = "health_penalty"},
  {key = "rotate-penalty", default = 0, min = -float_max, max = float_max, attack = "rotate_penalty"},
  {key = "fire-penalty", default = 0, min = -float_max, max = float_max, attack = "fire_penalty"},
  {key = "threatening-asteroid-penalty", default = -20, min = -float_max, max = float_max, attack = "threatening_asteroid_penalty"},
  {key = "call-for-help-radius", default = 40, min = 0, max = distance_max, field = "call_for_help_radius"},
  {key = "max-health", default = 400, min = 1, max = float_max, field = "max_health"},
  {key = "healing-per-second", default = 0, min = -float_max, max = float_max, special = "healing"},
  {key = "repair-speed-modifier", default = 1, min = 0, max = float_max, field = "repair_speed_modifier"},
  {key = "is-military-target", type = "bool-setting", default = true, field = "is_military_target"},
  {key = "alert-when-attacking", type = "bool-setting", default = true, field = "alert_when_attacking"},
  {key = "alert-when-damaged", type = "bool-setting", default = true, field = "alert_when_damaged"},
  {key = "create-ghost-on-death", type = "bool-setting", default = true, field = "create_ghost_on_death"},
  {key = "circuit-wire-max-distance", default = 9, min = 0, max = distance_max, field = "circuit_wire_max_distance"},
  {key = "mining-time", default = 0.5, min = 0, max = float_max, special = "mining"},
  {key = "heating-energy", default = -1, min = -1, max = float_max, special = "heating-energy"}
}

-- Only official damage types are exposed; no third-party prototype discovery.
for _, damage_type in ipairs({"physical", "impact", "poison", "explosion", "fire", "laser", "acid", "electric"}) do
  for _, component in ipairs({"decrease", "percent"}) do
    definitions[#definitions + 1] = {
      key = "resistance-" .. damage_type .. "-" .. component,
      default = 0,
      min = 0,
      max = component == "percent" and 100 or float_max,
      resistance = damage_type,
      component = component
    }
  end
end

return definitions
