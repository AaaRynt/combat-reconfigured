-- Runs only as a headless test scenario, never as part of the installed mod.
local function setting(key)
  return settings.startup["cr-gun-turret-" .. key].value
end

script.on_init(function()
  local surface = game.create_surface("cr-combat", {
    autoplace_settings = {
      entity = {treat_missing_as_default = false},
      decorative = {treat_missing_as_default = false}
    }
  })
  local force = game.forces.player
  force.technologies["physical-projectile-damage-1"].researched = true
  force.technologies["weapon-shooting-speed-1"].researched = true
  assert(force.get_ammo_damage_modifier("bullet") > 0)
  assert(force.get_turret_attack_modifier("gun-turret") > 0)
  assert(force.get_gun_speed_modifier("bullet") > 0)

  storage.cases = {}
  storage.start_tick = game.tick
  local range = setting("range")
  local cases = {
    {quality = "normal", distance = range * 0.8, should_fire = true},
    {quality = "normal", distance = range * 1.1, should_fire = false},
    {quality = "rare", distance = range * 1.1, should_fire = true},
    {quality = "legendary", distance = range * 1.4, should_fire = true},
    {quality = "legendary", distance = range * 1.6, should_fire = false}
  }
  for index, definition in ipairs(cases) do
    local x = (index - 1) * 256
    surface.request_to_generate_chunks({x, 0}, 1)
    surface.request_to_generate_chunks({x, -definition.distance}, 1)
  end
  surface.force_generate_chunk_requests()
  for index, definition in ipairs(cases) do
    local x = (index - 1) * 256
    local turret = surface.create_entity{
      name = "gun-turret", position = {x, 0}, force = force,
      quality = definition.quality, direction = defines.direction.north
    }
    assert(turret)
    turret.insert{name = "firearm-magazine", count = 20}
    assert(#turret.get_inventory(defines.inventory.turret_ammo) == setting("inventory-size"))
    local expected_health = prototypes.entity["gun-turret"].get_max_health(definition.quality)
    assert(math.abs(turret.max_health - expected_health) < 0.01)
    if definition.quality == "normal" then assert(expected_health == setting("max-health")) end
    if definition.quality == "legendary" then assert(expected_health > setting("max-health")) end
    local target = surface.create_entity{
      name = "gun-turret", position = {x, -definition.distance}, force = "enemy"
    }
    assert(target)
    storage.cases[target.unit_number] = {
      turret = turret, target = target, should_fire = definition.should_fire, shots = {}, quality = definition.quality
    }
  end
end)

script.on_event(defines.events.on_entity_damaged, function(event)
  local case = storage.cases[event.entity.unit_number]
  if not case then return end
  local force = game.forces.player
  local expected = 5 * setting("damage-modifier") * (1 + force.get_ammo_damage_modifier("bullet"))
    * (1 + force.get_turret_attack_modifier("gun-turret"))
  assert(math.abs(event.final_damage_amount - expected) < 0.01,
    "Ammo and turret damage research must multiply the configured coefficient")
  case.shots[#case.shots + 1] = game.tick
  event.entity.health = event.entity.max_health
end)

script.on_event(defines.events.on_tick, function()
  if game.tick - storage.start_tick < 300 then return end
  for _, case in pairs(storage.cases) do
    if case.should_fire then
      assert(#case.shots >= 10, "Expected firing at " .. case.quality .. " quality")
      local average_interval = (case.shots[#case.shots] - case.shots[1]) / (#case.shots - 1)
      local expected_interval = setting("cooldown") / (1 + game.forces.player.get_gun_speed_modifier("bullet"))
      assert(math.abs(average_interval - expected_interval) < 0.15, "Shooting speed research must affect the configured interval")
      if setting("ammo-consumption-modifier") == 0 then
        local inventory = case.turret.get_inventory(defines.inventory.turret_ammo)
        assert(inventory.get_item_count("firearm-magazine") == 20 and inventory[1].ammo == 10,
          "Zero consumption must preserve loaded ammunition")
      end
    else
      assert(#case.shots == 0, "Target outside " .. case.quality .. " range must not be shot")
    end
  end
  log("Combat Reconfigured: combat, research, quality range, quality health and inventory checks passed.")
  script.finish_test()
end)
