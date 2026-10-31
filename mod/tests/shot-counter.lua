-- Test-only launch marker, appended after unchanged native actions. Never shipped in the mod.
local function mark(ammo)
  if not ammo.action then
    for _,variant in ipairs(ammo) do mark(variant) end
    return
  end
  local actions=ammo.action
  if actions.type then actions={actions};ammo.action=actions end
  actions[#actions+1]={type='direct',action_delivery={type='instant',source_effects={{type='script',effect_id='cr-test-shot'}}}}
end
for _,name in ipairs({'firearm-magazine','flamethrower-ammo','artillery-shell','railgun-ammo','tesla-ammo'}) do
  mark(data.raw.ammo[name].ammo_type)
end
mark(data.raw['electric-turret']['laser-turret'].attack_parameters.ammo_type)
mark(data.raw['electric-turret']['tesla-turret'].attack_parameters.ammo_type)
mark(data.raw['fluid-turret']['flamethrower-turret'].attack_parameters.ammo_type)

-- Remove target resistances only in resource tests so coefficient ratios are directly observable.
data.raw['unit-spawner']['biter-spawner'].resistances={}
