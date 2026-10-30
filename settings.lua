local definitions = require("prototypes.gun-turret-settings")
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
