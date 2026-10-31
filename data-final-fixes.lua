local definitions = require("prototypes.weapons")

local function value(weapon, key)
  return settings.startup["cr-"..weapon.."-"..key].value
end

local function extend_beams(node, range)
  if type(node) ~= "table" then return end
  if node.type == "beam" and node.max_length and node.max_length < range then node.max_length = range end
  for _, child in pairs(node) do
    if type(child) == "table" then extend_beams(child,range) end
  end
end

local function joules(text)
  local number, prefix = text:match("^([%d%.eE%+%-]+)%s*([kMGT]?)J$")
  assert(number,"Unexpected vanilla energy format: "..text)
  return tonumber(number) * ({[""]=1,k=1000,M=1000000,G=1000000000,T=1000000000000})[prefix]
end

local function energy_cost(prototype, attack, cost, original, entity_cost)
  if cost == original then return end
  if entity_cost then prototype.energy_per_shot = tostring(cost).."J"
  else attack.ammo_type.energy_consumption = tostring(cost).."J" end
  local source = prototype.energy_source
  local capacity = joules(source.buffer_capacity)
  -- Keep the vanilla headroom so the changed shot can be afforded after native drain handling.
  local required = cost + math.max(0,capacity-original)
  if required > capacity then source.buffer_capacity = tostring(required).."J" end
end

for _, weapon in ipairs(definitions.weapons) do
  if not weapon.expansion or mods["space-age"] then
    for _, name in ipairs(weapon.prototypes or {weapon.prototype or weapon.id}) do
      local prototype = data.raw[weapon.kind][name]
      local attack = prototype.attack_parameters
      local range = value(weapon.id,"range")
      if range ~= weapon.range then
        attack.range = range
        extend_beams(attack.ammo_type,range)
        if prototype.prepare_range and prototype.prepare_range < range then prototype.prepare_range = range end
      end
      local cooldown = value(weapon.id,"cooldown")
      if cooldown ~= weapon.cooldown then attack.cooldown = cooldown end
      local damage = value(weapon.id,"damage-modifier")
      if damage ~= weapon.damage then attack.damage_modifier = damage end
      if weapon.resource == "ammo" then
        local cost = value(weapon.id,"ammo-consumption-modifier")
        if cost ~= weapon.cost then attack.ammo_consumption_modifier = cost end
      elseif weapon.resource == "fluid" then
        local cost = value(weapon.id,"fluid-consumption")
        if cost ~= weapon.cost then
          attack.fluid_consumption = cost
        end
      else
        energy_cost(prototype,attack,value(weapon.id,"energy-per-shot"),weapon.cost,false)
      end
      if weapon.energy then
        energy_cost(prototype,attack,value(weapon.id,"energy-per-shot"),weapon.energy,true)
      end
      if weapon.chain then
        local jumps = value(weapon.id,"chain-jumps")
        if jumps ~= weapon.jumps then data.raw["chain-active-trigger"][weapon.chain].max_jumps = jumps end
      end
      if weapon.artillery then
        local manual = value(weapon.id,"manual-range")
        if manual ~= 560 or range ~= weapon.range then
          for _, kind in ipairs({"artillery-turret","artillery-wagon"}) do
            data.raw[kind][kind].manual_range_modifier = manual/range
          end
        end
      end
    end
  end
end

-- Native speeds use turns/tick; the public input uses degrees/second.
local speed = value("artillery","rotation-speed")
if speed ~= 21.6 then
  for _, entity in ipairs({"artillery-turret","artillery-wagon"}) do
    data.raw[entity][entity].turret_rotation_speed = speed/21600
  end
end
local radius = value("artillery","blast-radius")
if radius ~= 4 then
  data.raw["artillery-projectile"]["artillery-projectile"].action.action_delivery.target_effects[1].action.radius = radius
end

if mods["space-age"] then
  local length = settings.startup["cr-railgun-ammo-line-length"].value
  if length ~= 50 then data.raw.ammo["railgun-ammo"].ammo_type.action.range = length end
end
