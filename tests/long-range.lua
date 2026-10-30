-- Exercise target acquisition over ungenerated space without generating the intervening map.
script.on_init(function()
  local range = settings.startup["cr-gun-turret-range"].value
  local distance = range - 10
  local surface = game.create_surface("cr-long-range", {
    autoplace_settings = {
      entity = {treat_missing_as_default = false},
      decorative = {treat_missing_as_default = false}
    }
  })
  surface.request_to_generate_chunks({0, 0}, 1)
  surface.request_to_generate_chunks({0, -distance}, 1)
  surface.force_generate_chunk_requests()
  storage.turret = surface.create_entity{
    name = "gun-turret", position = {0, 0}, force = "player", direction = defines.direction.north
  }
  storage.target = surface.create_entity{
    name = "gun-turret", position = {0, -distance}, force = "enemy"
  }
  assert(storage.turret and storage.target)
  storage.turret.insert{name = "firearm-magazine", count = 1}
end)

script.on_event(defines.events.on_entity_damaged, function(event)
  if event.entity == storage.target then
    assert(event.cause == storage.turret)
    assert(event.final_damage_amount == 5)
    log("Combat Reconfigured: the long-range turret hit its distant target.")
    script.finish_test()
  end
end)

script.on_event(defines.events.on_tick, function()
  assert(game.tick < 180, "Expected the turret to acquire and hit its distant target")
end)
