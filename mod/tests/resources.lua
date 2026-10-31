-- One-shot observations measure native inventory, fluid and electrical costs, not only data exports.
local function setting(id,key) return settings.startup['cr-'..id..'-'..key].value end
script.on_init(function()
  local surface=game.create_surface('cr-resource-tests',{autoplace_settings={entity={treat_missing_as_default=false},decorative={treat_missing_as_default=false}}})
  storage.cases={};storage.by_weapon={};storage.start=game.tick
  local cases={
    {id='gun-turret',ammo='firearm-magazine',magazine=10},
    {id='pistol',ammo='firearm-magazine',magazine=10,handheld=true},
    {id='laser-turret',electric=true,drain=24000},
    {id='tesla-turret',electric=true,drain=1000000},
    {id='railgun-turret',electric=true,drain=0,ammo='railgun-ammo',magazine=1},
    {id='flamethrower-turret',fluid=true},
    {id='flamethrower',handheld=true,ammo='flamethrower-ammo',magazine=100},
    {id='artillery',entity='artillery-turret',ammo='artillery-shell',magazine=1,artillery=true},
    {id='artillery',entity='artillery-wagon',ammo='artillery-shell',magazine=1,artillery=true},
    {id='teslagun',handheld=true,ammo='tesla-ammo',magazine=10},
    {id='railgun',handheld=true,ammo='railgun-ammo',magazine=1}
  }
  for index,case in ipairs(cases) do
    local x=(index-1)*256
    surface.request_to_generate_chunks({x,0},1)
    surface.request_to_generate_chunks({x,-120},1)
  end
  surface.force_generate_chunk_requests()
  for index,case in ipairs(cases) do
    local x=(index-1)*256
    local tiles={}
    for y=-5,5 do for dx=-4,4 do tiles[#tiles+1]={name='grass-1',position={x+dx,y}} end end
    for y=-125,-5 do for dx=-4,4 do tiles[#tiles+1]={name='grass-1',position={x+dx,y}} end end
    surface.set_tiles(tiles)
    local distance=case.artillery and 100 or ((case.id=='pistol' or case.id=='gun-turret' or case.id=='flamethrower') and 10 or 20)
    local target=surface.create_entity{name='biter-spawner',position={x,-distance},force='enemy'}
    target.disabled_by_script=true
    local weapon
    if case.handheld then
      weapon=surface.create_entity{name='character',position={x,0},force='player'}
      weapon.get_inventory(defines.inventory.character_guns).insert{name=case.id,count=1}
      weapon.selected_gun_index=1
      case.inventory=weapon.get_inventory(defines.inventory.character_ammo)
    else
      if case.entity=='artillery-wagon' then
        for _,y in ipairs({-2,0,2}) do surface.create_entity{name='straight-rail',position={x,y},force='player',direction=defines.direction.north} end
      end
      weapon=surface.create_entity{name=case.entity or case.id,position={x,0},force='player',direction=defines.direction.north}
      if case.ammo then
        case.inventory=weapon.get_inventory(case.artillery and defines.inventory.artillery_turret_ammo or defines.inventory.turret_ammo)
        if case.entity=='artillery-wagon' then case.inventory=weapon.get_inventory(defines.inventory.artillery_wagon_ammo) end
      end
    end
    assert(weapon and target)
    if case.inventory then case.inventory.insert{name=case.ammo,count=20} end
    case.weapon=weapon;case.target=target;case.hits=0;case.stopped=false;case.shots=0;case.damage_values={}
    case.goal=case.magazine==1 and 2 or 1
    storage.by_weapon[weapon.unit_number]=case
    case.expected_ammo=case.ammo and setting(case.id,'ammo-consumption-modifier') or nil
    case.expected_energy=case.electric and setting(case.id,'energy-per-shot') or nil
    case.expected_fluid=case.fluid and setting(case.id,'fluid-consumption') or nil
    storage.cases[target.unit_number]=case
  end
end)

local function ammunition(case)
  if not case.inventory then return nil end
  local total=0
  for index=1,#case.inventory do
    local stack=case.inventory[index]
    if stack.valid_for_read then total=total+(stack.count-1)*case.magazine+stack.ammo end
  end
  return total
end

local function stop(case)
  case.stopped=true
  if case.handheld then case.weapon.shooting_state={state=defines.shooting.not_shooting,position=case.target.position}
  else
    case.weapon.disabled_by_script=true
    if case.artillery then case.weapon.artillery_auto_targeting=false end
  end
end

script.on_event(defines.events.on_entity_damaged,function(event)
  local case=storage.cases[event.entity.unit_number]
  if case and event.final_damage_amount>0 then
    case.hits=case.hits+1
    case.first_damage=case.first_damage or event.final_damage_amount
    case.damage_values[string.format('%.4f',event.final_damage_amount)]=true
    event.entity.health=event.entity.max_health
  end
end)

script.on_event(defines.events.on_script_trigger_effect,function(event)
  if event.effect_id~='cr-test-shot' or not event.source_entity then return end
  local case=storage.by_weapon[event.source_entity.unit_number]
  if case then case.shots=case.shots+1;if case.shots>=case.goal then stop(case) end end
end)

script.on_event(defines.events.on_tick,function()
  for _,case in pairs(storage.cases) do
    local ammo=ammunition(case)
    if not case.initial_ammo then case.initial_ammo=ammo end
    if case.prior_energy then
      local spent=case.prior_energy-case.weapon.energy
      local drain=case.drain/60
      if spent>drain+1 then case.observed_energy=(case.observed_energy or 0)+spent-drain end
      case.prior_energy=nil
    end
    if case.prior_fluid then
      local spent=case.prior_fluid-case.weapon.get_fluid_count('light-oil')
      if spent>0.0001 then case.observed_fluid=(case.observed_fluid or 0)+spent end
      case.prior_fluid=nil
    end
    if not case.stopped then
      if case.electric then case.weapon.energy=1e15;case.prior_energy=case.weapon.energy end
      if case.fluid then case.weapon.insert_fluid{name='light-oil',amount=100000};case.prior_fluid=case.weapon.get_fluid_count('light-oil') end
      if case.handheld then case.weapon.shooting_state={state=defines.shooting.shooting_enemies,position=case.target.position} end
    end
  end
  if game.tick-storage.start<900 then return end
  local results={}
  for _,case in pairs(storage.cases) do
    log('RESOURCE '..case.id..'/'..tostring(case.entity)..' hits='..case.hits..' ammo='..tostring(case.inventory and case.initial_ammo-ammunition(case))..' energy='..tostring(case.observed_energy)..' fluid='..tostring(case.observed_fluid))
  end
  for _,case in pairs(storage.cases) do
    assert(case.shots==case.goal,case.id..' launch count '..case.shots)
    assert(case.hits>0,'No actual damage: '..case.id..' / '..tostring(case.entity))
    local spent=case.inventory and case.initial_ammo-ammunition(case) or nil
    if spent then assert(math.abs(spent-case.expected_ammo*case.goal)<0.01,case.id..' ammo: '..spent..' expected '..case.expected_ammo*case.goal) end
    if case.electric then
      local cost=case.observed_energy or 0
      assert(math.abs(cost-case.expected_energy*case.goal)<math.max(20000,case.expected_energy*0.01),case.id..' energy: '..cost..' expected '..case.expected_energy*case.goal)
    end
    if case.fluid then
      local cost=case.observed_fluid or 0
      assert(math.abs(cost-case.expected_fluid*case.goal)<0.01,case.id..' fluid: '..cost..' expected '..case.expected_fluid*case.goal)
    end
    results[#results+1]={weapon=case.id,entity=case.entity,hits=case.hits,ammo=spent,energy=case.observed_energy,fluid=case.observed_fluid,first_damage=case.first_damage,damage_values=case.damage_values}
  end
  helpers.write_file('resources.json',helpers.table_to_json(results))
  script.finish_test()
end)
