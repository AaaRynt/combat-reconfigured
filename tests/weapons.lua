-- Actual combat checks for distinct native mechanisms. Never loaded by the installed mod.
script.on_init(function()
  local surface = game.create_surface('cr-mechanisms', {autoplace_settings={
    entity={treat_missing_as_default=false}, decorative={treat_missing_as_default=false}}})
  storage.cases = {}
  storage.start = game.tick
  local cases = {
    {name='laser-turret', distance=45, power=true},
    {name='flamethrower-turret', distance=45, fluid=true, direction=defines.direction.north},
    {name='rocket-turret', distance=30, ammo='rocket'},
    {name='tesla-turret', distance=45, power=true},
    {name='railgun-turret', distance=60, power=true, ammo='railgun-ammo', direction=defines.direction.north},
    {name='artillery-turret', distance=120, ammo='artillery-shell', artillery=true},
    {name='pistol', distance=25, ammo='firearm-magazine', gun=true},
    {name='railgun', distance=60, ammo='railgun-ammo', gun=true},
    {name='shotgun', distance=10, ammo='shotgun-shell', gun=true},
    {name='rocket-launcher', distance=30, ammo='rocket', gun=true},
    {name='flamethrower', distance=20, ammo='flamethrower-ammo', gun=true},
    {name='artillery-wagon', distance=120, ammo='artillery-shell', artillery=true},
    {name='teslagun', distance=35, ammo='tesla-ammo', gun=true}
  }
  for index, case in ipairs(cases) do
    local x = (index-1)*256
    surface.request_to_generate_chunks({x,0},1)
    surface.request_to_generate_chunks({x,-case.distance},1)
  end
  surface.force_generate_chunk_requests()
  for index, case in ipairs(cases) do
    local x = (index-1)*256
    -- A spawner is also a valid automatic artillery target.
    local target = surface.create_entity{name='biter-spawner',position={x,-case.distance},force='enemy'}
    target.disabled_by_script = true
    local weapon
    if case.gun then
      weapon = surface.create_entity{name='character',position={x,0},force='player'}
      weapon.get_inventory(defines.inventory.character_guns).insert{name=case.name,count=1}
      weapon.get_inventory(defines.inventory.character_ammo).insert{name=case.ammo,count=100}
      weapon.selected_gun_index=1
      weapon.shooting_state={state=defines.shooting.shooting_enemies,position=target.position}
    else
      if case.name=='artillery-wagon' then
        for _, y in ipairs({-2,0,2}) do surface.create_entity{name='straight-rail',position={x,y},direction=defines.direction.north,force='player'} end
      end
      weapon = surface.create_entity{name=case.name,position={x,0},force='player',direction=case.direction}
      if case.ammo then weapon.insert{name=case.ammo,count=20} end
    end
    assert(weapon and target)
    if case.fluid then weapon.insert_fluid{name='light-oil',amount=100} end
    storage.cases[target.unit_number]={weapon=weapon,target=target,name=case.name,power=case.power,fluid=case.fluid,gun=case.gun,hits=0}
  end
end)

script.on_event(defines.events.on_entity_damaged,function(event)
  local case=storage.cases[event.entity.unit_number]
  if case and event.final_damage_amount>0 then
    case.hits=case.hits+1
    event.entity.health=event.entity.max_health
  end
end)

script.on_event(defines.events.on_tick,function()
  for _,case in pairs(storage.cases) do
    if case.power then case.weapon.energy=1000000000 end
    if case.fluid then case.weapon.insert_fluid{name='light-oil',amount=100} end
    if case.gun then case.weapon.shooting_state={state=defines.shooting.shooting_enemies,position=case.target.position} end
  end
  if game.tick-storage.start<900 then return end
  for _,case in pairs(storage.cases) do
    assert(case.hits>0,'No real damage observed for '..case.name)
    log('Combat Reconfigured: actual combat passed for '..case.name..' ('..case.hits..' damage events).')
  end
  script.finish_test()
end)
