local turret = data.raw["ammo-turret"]["gun-turret"]
local definitions = require("prototypes.gun-turret-settings")

for _, definition in ipairs(definitions) do
  local value = settings.startup["cr-gun-turret-" .. definition.key].value
  -- Leaving defaults untouched also preserves implicit engine defaults and DLC changes.
  if value ~= definition.default then
    if definition.attack then
      turret.attack_parameters[definition.attack] = value
    elseif definition.field then
      turret[definition.field] = value
      if definition.secondary then turret[definition.secondary] = value end
    elseif definition.duration then
      turret[definition.duration] = 1 / value
      turret[definition.duration .. "_secondary"] = 1 / value
    elseif definition.resistance then
      turret.resistances = turret.resistances or {}
      local resistance
      for _, candidate in ipairs(turret.resistances) do
        if candidate.type == definition.resistance then resistance = candidate end
      end
      if not resistance then
        resistance = {type = definition.resistance}
        turret.resistances[#turret.resistances + 1] = resistance
      end
      resistance[definition.component] = value
    elseif definition.special == "prepare-range" then
      if value >= 0 then turret.prepare_range = value end
    elseif definition.special == "healing" then
      turret.healing_per_tick = value / 60
    elseif definition.special == "mining" then
      turret.minable.mining_time = value
    elseif definition.special == "heating-energy" then
      if value >= 0 and feature_flags.freezing then
        turret.heating_energy = tostring(value) .. "kW"
      end
    end
  end
end

-- A reversed interval would make the turret unable to acquire targets.
local attack = turret.attack_parameters
if (attack.min_range or 0) > attack.range then
  log("Combat Reconfigured: minimum range exceeds maximum range; clamping minimum range to maximum range.")
  attack.min_range = attack.range
end
