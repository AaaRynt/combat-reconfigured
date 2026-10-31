-- Measure native barrel orientation increments while tracking an off-axis target.
script.on_init(function()
  local surface=game.create_surface('cr-rotation',{autoplace_settings={
    entity={treat_missing_as_default=false},decorative={treat_missing_as_default=false}}})
  storage.cases={};storage.start=game.tick;storage.surface=surface
  for index=1,2 do
    local x=(index-1)*512
    surface.request_to_generate_chunks({x,0},1);surface.request_to_generate_chunks({x+100,0},1)
  end
  surface.force_generate_chunk_requests()
  for index,name in ipairs({'artillery-turret','artillery-wagon'}) do
    local x=(index-1)*512
    if name=='artillery-wagon' then
      for _,y in ipairs({-2,0,2}) do surface.create_entity{name='straight-rail',position={x,y},force='player',direction=defines.direction.north} end
    end
    local weapon=surface.create_entity{name=name,position={x,0},force='player'}
    weapon.relative_turret_orientation=0
    weapon.insert{name='artillery-shell',count=10}
    local target=surface.create_entity{name='biter-spawner',position={x+100,0},force='enemy'}
    target.disabled_by_script=true
    storage.cases[#storage.cases+1]={name=name,weapon=weapon,previous=0,maximum=0,target=target.position}
  end
end)
script.on_event(defines.events.on_tick,function()
  local elapsed=game.tick-storage.start
  for _,case in ipairs(storage.cases) do
    local orientation=case.weapon.relative_turret_orientation
    local delta=math.abs((orientation-case.previous+0.5)%1-0.5)
    case.maximum=math.max(case.maximum,delta);case.previous=orientation
    if elapsed==10 then
      storage.surface.create_entity{name='artillery-flare',position=case.target,force='player',movement={0,0},height=0,vertical_speed=0,frame_speed=1}
    end
  end
  if elapsed<600 then return end
  for _,case in ipairs(storage.cases) do
    local expected=settings.startup['cr-artillery-rotation-speed'].value/21600
    assert(math.abs(case.maximum-expected)<0.00001,case.name..' observed speed '..case.maximum..' expected '..expected)
  end
  script.finish_test()
end)
