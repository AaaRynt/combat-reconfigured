local definitions = require("prototypes.catalog").gun_turret
local prototypes = {}

for index, definition in ipairs(definitions) do
  prototypes[#prototypes + 1] = {
    type = definition.type or "double-setting",
    name = "cr-gun-turret-" .. definition.key,
    setting_type = "startup",
    default_value = definition.default,
    minimum_value = definition.min,
    maximum_value = definition.max,
    allowed_values = definition.allowed,
    hidden = definition.special == "heating-energy" and not feature_flags.freezing or nil,
    order = string.format("a[gun-turret]-%03d", index)
  }
end

data:extend(prototypes)

local catalog = require("prototypes.catalog").catalog
for index, definition in ipairs(catalog) do
  if (not definition.expansion or mods["space-age"])
    and (not definition.feature or feature_flags[definition.feature]) then
    local default = definition.default
    if not mods["space-age"] and definition.base_default ~= nil then default = definition.base_default end
    local prototype = {
      type = definition.type,
      name = definition.name,
      setting_type = "startup",
      default_value = default,
      localised_name = {"", {"?", {"item-name." .. definition.prototype},
        {"entity-name." .. definition.prototype}, {"equipment-name." .. definition.prototype}, definition.prototype},
        " — ", {"mod-setting-name." .. definition.name}},
      order = definition.prototype == "gun-turret" and string.format("a[gun-turret]-z-%05d", index)
        or string.format("b[experimental]-%05d", index),
      hidden = definition.freezing and not feature_flags.freezing or nil,
      allowed_values = definition.allowed
    }
    if definition.type == "double-setting" or definition.type == "int-setting" then
      prototype.minimum_value = definition.min
      prototype.maximum_value = definition.max
    end
    data:extend({prototype})
  end
end
