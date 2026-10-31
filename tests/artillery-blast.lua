-- Observe native shell splash from both consumers, without replacing shell actions.
script.on_init(function()
  local surface=game.create_surface('cr-blast',{autoplace_settings={
    entity={treat_missing_as_default=false},decorative={treat_missing_as_default=false}}})
  storage.cases={};storage.weapons={};storage.start=game.tick;storage.surface=surface
  for index=1,2 do
    local x=(index-1)*512
    surface.request_to_generate_chunks({x,0},1)
    surface.request_to_generate_chunks({x,-100},1)
  end
  surface.force_generate_chunk_requests()
  for index,name in ipairs({'artillery-turret','artillery-wagon'}) do
    local x=(index-1)*512
    if name=='artillery-wagon' then
      for _,y in ipairs({-2,0,2}) do surface.create_entity{name='straight-rail',position={x,y},force='player',direction=defines.direction.north} end
    end
    local weapon=surface.create_entity{name=name,position={x,0},force='player'}
    weapon.insert{name='artillery-shell',count=1}
    storage.weapons[#storage.weapons+1]={x=x,name=name}
    for _,offset in ipairs({0,7,12}) do
      local target=surface.create_entity{name='biter-spawner',position={x+offset,-100},force=offset==0 and 'enemy' or 'neutral'}
      target.disabled_by_script=true
      storage.cases[target.unit_number]={offset=offset,hits=0,weapon=name}
    end
  end
end)
script.on_event(defines.events.on_entity_damaged,function(event)
  local case=storage.cases[event.entity.unit_number]
  if case then case.hits=case.hits+1;event.entity.health=event.entity.max_health end
end)
script.on_event(defines.events.on_tick,function()
  local elapsed=game.tick-storage.start
  if elapsed==10 then
    for _,case in ipairs(storage.weapons) do
      storage.surface.create_entity{name='artillery-flare',position={case.x,-100},force='player',movement={0,0},height=0,vertical_speed=0,frame_speed=1}
    end
  end
  if elapsed<900 then return end
  local expanded=settings.startup['cr-artillery-blast-radius'].value==8
  for _,case in pairs(storage.cases) do
    local expected=case.offset==0 or (case.offset==7 and expanded)
    assert((case.hits>0)==expected,case.weapon..' incorrect splash at offset '..case.offset)
  end
  script.finish_test()
end)
