-- Only explicitly changed startup values are written. No runtime scanning or entity replacement.
local catalog = require("prototypes.catalog")
local changed, explicit = {}, {}

local function parent_at(root, path)
  for index = 1, #path - 1 do
    local key = path[index]
    if not root[key] then root[key] = {} end
    root = root[key]
  end
  return root, path[#path]
end

for _, definition in ipairs(catalog) do
  local setting = settings.startup[definition.name]
  local default = definition.default
  if not mods["space-age"] and definition.base_default ~= nil then default = definition.base_default end
  if setting and setting.value ~= default and (not definition.freezing or feature_flags.freezing)
    and (not definition.sentinel or setting.value >= 0) then
    local prototype = data.raw[definition.kind] and data.raw[definition.kind][definition.prototype]
    if prototype then
      local path = not mods["space-age"] and definition.base_path or definition.path
      local value = setting.value
      if definition.energy then value = tostring(value) .. definition.energy end
      if definition.resistance then
        prototype.resistances = prototype.resistances or {}
        local resistance
        for _, candidate in ipairs(prototype.resistances) do
          if candidate.type == definition.path[2] then resistance = candidate end
        end
        if not resistance then
          resistance = {type = definition.path[2]}
          prototype.resistances[#prototype.resistances + 1] = resistance
        end
        resistance[definition.path[3]] = value
      elseif definition.path[#definition.path] ~= "prepare_range" or value >= 0 then
        local parent, key = parent_at(prototype, path)
        parent[key] = value
      end
      changed[prototype] = true
      explicit[prototype] = explicit[prototype] or {}
      explicit[prototype][table.concat(path, ".")] = true
    end
  end
end

local function repair_attack(prototype, attack, path)
  if not attack or not attack.range then return end
  if (attack.min_range or 0) > attack.range then
    log("Combat Reconfigured: clamping reversed attack interval on " .. prototype.name)
    attack.min_range = attack.range
  end
  if prototype.prepare_range and prototype.prepare_range < attack.range and explicit[prototype]
    and explicit[prototype][path .. ".range"] and not explicit[prototype].prepare_range then
    prototype.prepare_range = attack.range
  end
  -- Beam limits are embedded on the firing weapon, not on the shared beam prototype.
  local function extend_delivery(value, current)
    if type(value) ~= "table" then return end
    if value.type == "beam" and value.max_length and value.max_length < attack.range then
      if not (explicit[prototype] and explicit[prototype][current .. ".max_length"]) then
        value.max_length = attack.range
      end
    end
    for key, child in pairs(value) do
      if type(child) == "table" then extend_delivery(child, current .. "." .. tostring(key)) end
    end
  end
  extend_delivery(attack.ammo_type, path .. ".ammo_type")
end

-- Retained gun-turret range edits must participate in dependency handling too.
local gun = data.raw["ammo-turret"]["gun-turret"]
if settings.startup["cr-gun-turret-range"].value ~= 18 then changed[gun] = true end
for prototype in pairs(changed) do
  repair_attack(prototype, prototype.attack_parameters, "attack_parameters")
  if prototype.capsule_action then
    repair_attack(prototype, prototype.capsule_action.attack_parameters, "capsule_action.attack_parameters")
  end
  if prototype.type == "fire" and prototype.initial_lifetime and prototype.maximum_lifetime
    and prototype.initial_lifetime > prototype.maximum_lifetime then
    log("Combat Reconfigured: clamping initial fire lifetime on " .. prototype.name)
    prototype.initial_lifetime = prototype.maximum_lifetime
  end
  if prototype.turning_speed_increases_exponentially_with_projectile_speed and prototype.acceleration == 0 then
    log("Combat Reconfigured: exponential projectile turning requires nonzero acceleration; keeping it disabled on " .. prototype.name)
    prototype.turning_speed_increases_exponentially_with_projectile_speed = false
  end
end
