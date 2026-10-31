#!/usr/bin/env python3
"""Public v1.0.0 validation; no builds, extra dependencies, player mods or saves."""
import argparse
import configparser
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import support
import expectations

ROOT=support.ROOT


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--factorio',type=Path,default=Path('/Applications/factorio.app/Contents/MacOS/factorio'))
    parser.add_argument('--data',type=Path)
    parser.add_argument('--keep',type=Path)
    args=parser.parse_args();data=args.data or args.factorio.resolve().parents[1]/'data'
    if args.keep:args.keep.mkdir(parents=True,exist_ok=False);work=args.keep.resolve()
    else:
        temporary=tempfile.TemporaryDirectory(prefix='combat-public-');work=Path(temporary.name)

    info=json.loads((ROOT/'info.json').read_text())
    mod_folder=info['name']+'_'+info['version']
    vanillas={}

    def run(name,expansion=False,enabled=True,overrides=None,scenario=None,test_arg=None,shot_counter=False,package=None):
        folder=work/name;mods=support.setup(folder,enabled,expansion,overrides)
        if package:
            shutil.rmtree(mods/mod_folder)
            shutil.copy2(package,mods/package.name)
        if shot_counter:
            shutil.copy2(ROOT/'tests/shot-counter.lua',mods/'cr-check_0.0.1/data-final-fixes.lua')
        (folder/'config.ini').write_text('[path]\nread-data='+str(data)+'\nwrite-data='+str(folder/'user')+'\n')
        command=[str(args.factorio),'--config',str(folder/'config.ini'),'--mod-directory',str(mods),'--check-unused-prototype-data']
        if scenario:
            destination=folder/'user/scenarios/cr-check';destination.mkdir(parents=True)
            (destination/'control.lua').write_text((ROOT/'tests'/scenario).read_text())
            command+=['--test-scenario','cr-check']
            if test_arg:command+=['--test-arg',test_arg]
        else:command+=['--dump-data']
        output=support.execute(command,folder)
        assert 'Value ROOT.' not in output,output
        print('PASS',name,flush=True)
        if scenario:return output
        raw=json.loads((folder/'user/script-output/data-raw-dump.json').read_text())
        settings=json.loads((folder/'user/script-output/mod-settings-dump.json').read_text())
        flat={name:p for group in settings.values() for name,p in group.items()}
        return raw,flat

    locales=[]
    for language in ['en','zh-CN']:
        cfg=configparser.ConfigParser(interpolation=None,delimiters=('=',),strict=True)
        cfg.read(ROOT/'locale'/language/'settings.cfg');locales.append(cfg)
    assert {s:set(locales[0][s]) for s in locales[0].sections()}=={s:set(locales[1][s]) for s in locales[1].sections()}
    assert json.loads((ROOT/'info.json').read_text())['version']=='1.0.0'
    for file in [ROOT/'settings.lua',ROOT/'data-final-fixes.lua',*(ROOT/'prototypes').glob('*.lua')]:
        assert 'experiments' not in file.read_text(),file
    for expansion in [False,True]:
        suffix='space-age' if expansion else 'base'
        vanilla,_=run('vanilla-'+suffix,expansion,False)
        vanillas[suffix]=vanilla
        actual,settings=run('defaults-'+suffix,expansion)
        assert actual==vanilla,'Every prototype must equal vanilla at defaults'
        assert len(settings)==(87 if expansion else 63),len(settings)
        assert {n for n in settings if n.startswith('cr-gun-turret-')}=={
            'cr-gun-turret-range','cr-gun-turret-cooldown','cr-gun-turret-damage-modifier','cr-gun-turret-ammo-consumption-modifier'}
        for n,p in settings.items():
            assert p['type'] in ['int-setting','double-setting']
            assert p['setting_type']=='startup'
            assert not p.get('hidden',False)
            label=p['localised_name'][0]
            assert label.split('.')[1] in locales[0]['cr-setting-name']
        expectations.defaults_and_limits(vanilla,settings)
        for boundary in ['minimum_value','maximum_value']:
            values={name:p[boundary] for name,p in settings.items() if p[boundary]!=p['default_value']}
            changed,_=run(boundary+'-'+suffix,expansion,overrides=values)
            assert expectations.normalize_energy(changed)==expectations.normalize_energy(expectations.expected(vanilla,values)),boundary
        values=expectations.mutated(settings)
        changed,_=run('all-controls-'+suffix,expansion,overrides=values)
        assert expectations.normalize_energy(changed)==expectations.normalize_energy(expectations.expected(vanilla,values)), 'Incorrect mapping or unexpected side effect'
        print('PASS exact vanilla defaults, bounds and',len(settings),'public control mutations:',suffix,flush=True)
        for weapon in ['gun-turret','laser-turret','flamethrower-turret','artillery','spidertron-rocket-launcher']+(['railgun-turret','teslagun','railgun-ammo'] if expansion else []):
            subset={name:value for name,value in values.items() if expectations.split(name)[0]==weapon}
            isolated,_=run('isolation-'+suffix+'-'+weapon,expansion,overrides=subset)
            assert expectations.normalize_energy(isolated)==expectations.normalize_energy(expectations.expected(vanilla,subset)),weapon
    # Real research, range and resource regressions use only the public identifiers.
    run('gun-default-research-quality',True,scenario='combat.lua')
    run('gun-configured-research-quality',True,overrides={'cr-gun-turret-range':60,'cr-gun-turret-cooldown':3,
        'cr-gun-turret-damage-modifier':2,'cr-gun-turret-ammo-consumption-modifier':0},scenario='combat.lua')
    ranges={'cr-laser-turret-range':50,'cr-flamethrower-turret-range':50,'cr-tesla-turret-range':50,
        'cr-railgun-turret-range':70,'cr-railgun-range':70,'cr-railgun-ammo-line-length':80,
        'cr-pistol-range':30,'cr-flamethrower-range':25,'cr-teslagun-range':40}
    run('actual-expanded-ranges',True,overrides=ranges,scenario='weapons.lua')
    run('actual-maximum-gun-range',overrides={'cr-gun-turret-range':256,'cr-gun-turret-cooldown':120},scenario='range-limit.lua')
    run('actual-artillery-auto-manual',True,overrides={'cr-artillery-range':100,'cr-artillery-manual-range':300},scenario='artillery.lua')
    run('artillery-blast-default',True,scenario='artillery-blast.lua')
    run('artillery-blast-expanded',True,overrides={'cr-artillery-blast-radius':8},scenario='artillery-blast.lua')
    run('artillery-rotation',True,overrides={'cr-artillery-rotation-speed':90},scenario='artillery-rotation.lua')
    resource_weapons=['gun-turret','pistol','laser-turret','tesla-turret','railgun-turret',
        'flamethrower-turret','flamethrower','artillery','teslagun','railgun']
    costs={f'cr-{name}-cooldown':300 for name in resource_weapons}
    for name in ['gun-turret','pistol','flamethrower','teslagun']:
        costs[f'cr-{name}-ammo-consumption-modifier']=2
    for name in ['railgun-turret','artillery','railgun']:
        costs[f'cr-{name}-ammo-consumption-modifier']=0.5
    costs.update({'cr-laser-turret-energy-per-shot':1600000,'cr-tesla-turret-energy-per-shot':24000000,
        'cr-railgun-turret-energy-per-shot':20000000,'cr-flamethrower-turret-fluid-consumption':2})
    run('actual-positive-costs',True,overrides=costs,scenario='resources.lua',shot_counter=True)
    free={name:(value if name.endswith('-cooldown') else 0) for name,value in costs.items()}
    free.update({f'cr-{name}-damage-modifier':(4 if name=='laser-turret' else 2) for name in resource_weapons})
    run('actual-zero-costs-double-damage',True,overrides=free,scenario='resources.lua',shot_counter=True)
    positive=json.loads((work/'actual-positive-costs/user/script-output/resources.json').read_text())
    doubled=json.loads((work/'actual-zero-costs-double-damage/user/script-output/resources.json').read_text())
    positive={(r['weapon'],r.get('entity')):r for r in positive}
    for row in doubled:
        baseline=positive[(row['weapon'],row.get('entity'))]
        assert abs(row['first_damage']-baseline['first_damage']*2)<0.01,row['weapon']
    print('PASS measured native resource costs and doubled damage in 11 combat cases',flush=True)
    spec=importlib.util.spec_from_file_location('package',ROOT/'scripts/package.py')
    packaging=importlib.util.module_from_spec(spec);spec.loader.exec_module(packaging)
    artifact=packaging.create(work/(mod_folder+'.zip'))
    for expansion in [False,True]:
        suffix='space-age' if expansion else 'base'
        packaged,_=run('packaged-defaults-'+suffix,expansion,package=artifact)
        assert packaged==vanillas[suffix],'Packaged defaults must equal vanilla: '+suffix
        if expansion:
            run('packaged-combat-'+suffix,True,scenario='combat.lua',package=artifact)
        else:
            run('packaged-combat-'+suffix,overrides={'cr-artillery-range':100,'cr-artillery-manual-range':300},
                scenario='artillery.lua',package=artifact)
    print('PASS explicit ZIP contents, source bytes and installed ZIP combat in base and Space Age',flush=True)
    if args.keep:print('Test files:',work)

if __name__=='__main__':main()
