local definitions = require("prototypes.weapons")
local settings = {}
for index, definition in ipairs(definitions.settings) do
  if not definition.expansion or mods["space-age"] then
    local description = {"", {"cr-setting-description."..definition.key, tostring(definition.default), tostring(definition.blind_spot or 0)},
      "\n", {"cr-note.bounds", tostring(definition.min), tostring(definition.max)}}
    if definition.weapon == "artillery" then
      description = {"", description, "\n", {"cr-note.artillery-shared"}}
    elseif definition.weapon == "spidertron-rocket-launcher" then
      description = {"", description, "\n", {"cr-note.spidertron-shared"}}
    end
    settings[#settings+1] = {
      type=definition.type, name=definition.name, setting_type="startup",
      default_value=definition.default, minimum_value=definition.min, maximum_value=definition.max,
      localised_name={"cr-setting-name."..definition.key, {"cr-weapon."..definition.weapon}},
      localised_description=description, order=string.format("a-%03d",index)
    }
  end
end
data:extend(settings)
