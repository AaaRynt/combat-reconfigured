-- Explicit vanilla 2.1.24 targets. Values are base values, before native research and quality.
-- resource = ammo coefficient, fluid units/shot, embedded energy J/shot, or entity energy J/shot.
local weapons = {
  {id="gun-turret", kind="ammo-turret", range=18, cooldown=6, damage=1, resource="ammo", cost=1},
  {id="laser-turret", kind="electric-turret", range=24, cooldown=40, damage=2, resource="energy", cost=800000},
  {id="flamethrower-turret", kind="fluid-turret", range=30, min_range=6, cooldown=4, damage=1, resource="fluid", cost=0.2},
  {id="rocket-turret", kind="ammo-turret", range=36, min_range=15, cooldown=120, damage=1, resource="ammo", cost=1, expansion=true},
  {id="tesla-turret", kind="electric-turret", range=30, cooldown=120, damage=1, resource="energy", cost=12000000, expansion=true, chain="chain-tesla-turret-chain", jumps=10},
  {id="railgun-turret", kind="ammo-turret", range=40, min_range=3.5, cooldown=170, damage=1, resource="ammo", cost=1, expansion=true, energy=10000000},
  {id="pistol", kind="gun", range=15, cooldown=15, damage=1, resource="ammo", cost=1},
  {id="submachine-gun", kind="gun", range=18, cooldown=6, damage=1, resource="ammo", cost=1},
  {id="shotgun", kind="gun", range=15, cooldown=40, damage=1, resource="ammo", cost=1},
  {id="combat-shotgun", kind="gun", range=15, cooldown=30, damage=1.5, resource="ammo", cost=1},
  {id="rocket-launcher", kind="gun", range=36, cooldown=60, damage=1, resource="ammo", cost=1},
  {id="flamethrower", kind="gun", range=15, min_range=3, cooldown=1, damage=1, resource="ammo", cost=1},
  {id="railgun", kind="gun", range=40, cooldown=120, damage=1, resource="ammo", cost=1, expansion=true},
  {id="teslagun", kind="gun", range=24, cooldown=60, damage=1, resource="ammo", cost=1, expansion=true, chain="chain-tesla-gun-chain", jumps=12},
  {id="vehicle-machine-gun", kind="gun", range=20, cooldown=4, damage=1, resource="ammo", cost=1},
  {id="tank-machine-gun", kind="gun", range=20, cooldown=4, damage=1, resource="ammo", cost=1},
  {id="tank-cannon", kind="gun", range=30, min_range=5, cooldown=90, damage=1, resource="ammo", cost=1},
  {id="tank-flamethrower", kind="gun", range=9, min_range=3, cooldown=1, damage=1, resource="ammo", cost=1},
  {id="artillery", prototype="artillery-wagon-cannon", kind="gun", range=224, min_range=32, cooldown=200, damage=1, resource="ammo", cost=1, artillery=true}
}
weapons[#weapons+1] = {id="spidertron-rocket-launcher", kind="gun", range=36,
  cooldown=60, damage=1, resource="ammo", cost=1,
  prototypes={"spidertron-rocket-launcher-1","spidertron-rocket-launcher-2",
    "spidertron-rocket-launcher-3","spidertron-rocket-launcher-4"}}

local single_round = {['rocket-turret']=true, ['rocket-launcher']=true, ['railgun']=true,
  ['railgun-turret']=true, ['tank-cannon']=true, ['artillery']=true}
local settings = {}
local function add(weapon, key, default, minimum, maximum, kind)
  settings[#settings+1] = {name="cr-"..weapon.id.."-"..key, weapon=weapon.id, key=key,
    default=default, min=minimum, max=maximum, type=kind or "double-setting", expansion=weapon.expansion,
    shared=weapon.artillery or weapon.prototypes ~= nil, blind_spot=weapon.min_range or 0}
end
for _, weapon in ipairs(weapons) do
  add(weapon,"range",weapon.range,(weapon.min_range or 0)+1,weapon.artillery and 1024 or 256)
  add(weapon,"cooldown",weapon.cooldown,1,3600)
  add(weapon,"damage-modifier",weapon.damage,0,10)
  local cost_key = weapon.resource == "ammo" and "ammo-consumption-modifier"
    or weapon.resource == "fluid" and "fluid-consumption" or "energy-per-shot"
  local ammo_limit = single_round[weapon.id] or weapon.id:find("spidertron",1,true)
  local maximum = weapon.resource == "energy" and 100000000
    or weapon.resource == "fluid" and 10 or ammo_limit and 1 or 10
  add(weapon,cost_key,weapon.cost,0,maximum)
  if weapon.energy then add(weapon,"energy-per-shot",weapon.energy,0,100000000) end
  if weapon.chain then add(weapon,"chain-jumps",weapon.jumps,1,16,"int-setting") end
  if weapon.artillery then
    add(weapon,"manual-range",560,33,4096)
    add(weapon,"blast-radius",4,0.5,32)
    add(weapon,"rotation-speed",21.6,1,360)
  end
end
settings[#settings+1] = {name="cr-railgun-ammo-line-length",weapon="railgun-ammo",key="line-length",
  default=50,min=1,max=256,type="double-setting",expansion=true,shared=true}

return {weapons=weapons, settings=settings}
