-- Save a vanilla entity, then reload it with changed startup settings and this mod enabled.
script.on_init(function()
  local surface = game.surfaces[1]
  surface.request_to_generate_chunks({0, 0}, 1)
  surface.force_generate_chunk_requests()
  local position = surface.find_non_colliding_position("gun-turret", {0, 0}, 32, 1)
  local turret = surface.create_entity{name = "gun-turret", position = position, force = "player"}
  assert(turret)
  turret.health = 123
  turret.insert{name = "firearm-magazine", count = 7}
  storage.turret = turret
  storage.unit_number = turret.unit_number
end)

script.on_event(defines.events.on_tick, function()
  if script.test_arg == "reload" then
    local turret = storage.turret
    assert(turret.valid and turret.unit_number == storage.unit_number)
    assert(turret.max_health == 1000)
    assert(math.abs(turret.get_health_ratio() - 123 / 400) < 0.0001,
      "Expected native health ratio preservation; actual HP: " .. turret.health)
    assert(#turret.get_inventory(defines.inventory.turret_ammo) == 4)
    assert(turret.get_item_count("firearm-magazine") == 7)
    assert(turret.prototype.attack_parameters.range == 60)
    log("Combat Reconfigured: saved vanilla turret retained its identity, health ratio and ammo; new settings applied.")
    script.finish_test()
  elseif not storage.saved then
    storage.saved = true
    game.server_save("cr-existing")
  end
end)
