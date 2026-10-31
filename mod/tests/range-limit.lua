-- Exercise the public range ceiling with normal quality and no research.
script.on_init(function()
  local surface=game.create_surface('cr-range-limit',{autoplace_settings={
    entity={treat_missing_as_default=false},decorative={treat_missing_as_default=false}}})
  storage.cases={};storage.start=game.tick
  for index,distance in ipairs({250,270}) do
    local x=(index-1)*768
    surface.request_to_generate_chunks({x,0},1)
    surface.request_to_generate_chunks({x,-distance},1)
  end
  surface.force_generate_chunk_requests()
  for index,distance in ipairs({250,270}) do
    local x=(index-1)*768
    local turret=surface.create_entity{name='gun-turret',position={x,0},force='player',direction=defines.direction.north}
    turret.insert{name='firearm-magazine',count=20}
    local target=surface.create_entity{name='biter-spawner',position={x,-distance},force='enemy'}
    target.disabled_by_script=true
    storage.cases[target.unit_number]={distance=distance,hits=0}
  end
end)
script.on_event(defines.events.on_entity_damaged,function(event)
  local case=storage.cases[event.entity.unit_number]
  if case then case.hits=case.hits+1;event.entity.health=event.entity.max_health end
end)
script.on_event(defines.events.on_tick,function()
  if game.tick-storage.start<900 then return end
  for _,case in pairs(storage.cases) do
    assert((case.hits>0)==(case.distance<256),'Incorrect firing at '..case.distance)
  end
  script.finish_test()
end)
