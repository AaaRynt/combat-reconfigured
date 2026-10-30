#!/usr/bin/env python3
"""Real attacks with increased beam, projectile and line ranges, plus fluid/artillery/robot mechanisms."""
from pathlib import Path
import tempfile
import run as common

with tempfile.TemporaryDirectory(prefix='cr-weapons-') as directory:
    folder=Path(directory)
    overrides={
      'cr-electric-turret-laser-turret-attack-parameters-range':50,
      'cr-fluid-turret-flamethrower-turret-attack-parameters-range':50,
      'cr-electric-turret-tesla-turret-attack-parameters-range':50,
      'cr-ammo-turret-railgun-turret-attack-parameters-range':70,
      'cr-gun-railgun-attack-parameters-range':70,
      'cr-ammo-railgun-ammo-ammo-type-action-range':80,
      'cr-gun-pistol-attack-parameters-range':30,
    }
    mods=common.setup(folder,True,True,overrides)
    (folder/'config.ini').write_text('[path]\nread-data=/Applications/factorio.app/Contents/data\nwrite-data='+str(folder/'user')+'\n')
    scenario=folder/'user/scenarios/cr-weapons';scenario.mkdir(parents=True)
    (scenario/'control.lua').write_text((common.ROOT/'tests/weapons.lua').read_text())
    output=common.execute(['/Applications/factorio.app/Contents/MacOS/factorio','--config',str(folder/'config.ini'),'--mod-directory',str(mods),'--test-scenario','cr-weapons'],folder)
    print('\n'.join(line for line in output.splitlines() if 'actual combat passed' in line or 'Test passed' in line))
