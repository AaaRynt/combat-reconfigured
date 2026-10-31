-- The public automatic/manual inputs are shared by the turret and wagon.
script.on_init(function()
  local surface=game.create_surface('cr-artillery',{autoplace_settings={
    entity={treat_missing_as_default=false},decorative={treat_missing_as_default=false}}})
  local cases={
    {name='artillery-turret',distance=90},{name='artillery-wagon',distance=90},
    {name='artillery-turret',distance=200,manual=true},{name='artillery-wagon',distance=200,manual=true},
    {name='artillery-turret',distance=320,manual=true,outside=true},{name='artillery-wagon',distance=320,manual=true,outside=true}}
  storage.cases={};storage.start=game.tick;storage.surface=surface
  for index,case in ipairs(cases) do
    local x=(index-1)*512
    surface.request_to_generate_chunks({x,0},1)
    surface.request_to_generate_chunks({x,-case.distance},1)
  end
  surface.force_generate_chunk_requests()
  for index,case in ipairs(cases) do
    local x=(index-1)*512
    if case.name=='artillery-wagon' then
      for _,y in ipairs({-2,0,2}) do
        surface.create_entity{name='straight-rail',position={x,y},direction=defines.direction.north,force='player'}
      end
    end
    local weapon=surface.create_entity{name=case.name,position={x,0},force='player'}
    weapon.insert{name='artillery-shell',count=10}
    local target=surface.create_entity{name='biter-spawner',position={x,-case.distance},force='enemy'}
    target.disabled_by_script=true
    case.target=target;case.hits=0;storage.cases[target.unit_number]=case
  end
end)
script.on_event(defines.events.on_entity_damaged,function(event)
  local case=storage.cases[event.entity.unit_number]
  if case then case.hits=case.hits+1;event.entity.health=event.entity.max_health end
end)
script.on_event(defines.events.on_tick,function()
  local elapsed=game.tick-storage.start
  if elapsed==300 then
    for _,case in pairs(storage.cases) do
      if case.manual then
        assert(case.hits==0,'Automatic fire exceeded configured 100-tile range')
        assert(storage.surface.create_entity{name='artillery-flare',position=case.target.position,force='player',
          movement={0,0},height=0,vertical_speed=0,frame_speed=1})
      end
    end
  end
  if elapsed<1200 then return end
  for _,case in pairs(storage.cases) do
    assert((case.hits>0)==(not case.outside),'Incorrect '..(case.manual and 'manual' or 'automatic')..' targeting: '..case.name..' at '..case.distance)
  end
  script.finish_test()
end)
