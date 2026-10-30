#!/usr/bin/env python3
"""All-catalog registration, mapping and isolation checks in the real engine."""
import argparse
import configparser
import json
import math
from pathlib import Path
import tempfile
import run as common

ROOT = common.ROOT
CATALOG = json.loads((ROOT / 'tests/catalog.json').read_text())


def expected_value(e, expansion):
    return e['default'] if expansion else e.get('base_default', e['default'])


def read_field(root, e, expansion):
    value = root[e['kind']][e['prototype']]
    path = e['path'] if expansion else e.get('base_path',e['path'])
    if e.get('resistance'):
        return next(r for r in value['resistances'] if r['type'] == path[1])[path[2]]
    for key in path:
        value = value[key-1] if isinstance(key, int) else value[key]
    return value



def write_field(root, e, value, expansion):
    node=root[e['kind']][e['prototype']]
    path=e['path'] if expansion else e.get('base_path',e['path'])
    if e.get('resistance'):
        node.setdefault('resistances',[])
        match=next((r for r in node['resistances'] if r['type']==path[1]),None)
        if match is None:
            match={'type':path[1]};node['resistances'].append(match)
        match[path[2]]=value
        return
    for key in path[:-1]:
        if isinstance(key,int):node=node[key-1]
        else:node=node.setdefault(key,{})
    if isinstance(path[-1],int):node[path[-1]-1]=value
    else:node[path[-1]]=value

def alternative(e, expansion):
    value = expected_value(e, expansion)
    if e.get('sentinel'): return 100
    if e['type'] == 'bool-setting': return not value
    if e['type'] == 'string-setting': return next(x for x in e['allowed'] if x != value)
    delta = 1 if e['type'] == 'int-setting' else max(abs(value)*0.05, 0.05)
    candidate = value + delta
    if candidate > e['max']: candidate = value - delta
    if e['path'][-1] == 'turn_range': candidate = 0.25 if value != 0.25 else 0.5
    return max(e['min'], min(e['max'], candidate))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--keep',type=Path)
    args=parser.parse_args()
    if args.keep:args.keep.mkdir(parents=True,exist_ok=False);work=args.keep.resolve()
    else:
        temporary=tempfile.TemporaryDirectory(prefix='cr-catalog-');work=Path(temporary.name)
    locales=[]
    for language in ['en','zh-CN']:
        cfg=configparser.ConfigParser(interpolation=None,delimiters=('=',),strict=True)
        cfg.read(ROOT/'locale'/language/'catalog.cfg')
        assert set(cfg['mod-setting-name']) == set(cfg['mod-setting-description'])
        assert set(cfg['mod-setting-name']) == {e['name'] for e in CATALOG['entries']}
        locales.append(set(cfg['mod-setting-name']))
    assert locales[0] == locales[1]

    def run(name, expansion, enabled=True, overrides=None):
        folder=work/name; mods=common.setup(folder,enabled,expansion,overrides)
        config=folder/'config.ini';config.write_text('[path]\nread-data=/Applications/factorio.app/Contents/data\nwrite-data='+str(folder/'user')+'\n')
        output=common.execute(['/Applications/factorio.app/Contents/MacOS/factorio','--config',str(config),'--mod-directory',str(mods),'--check-unused-prototype-data','--dump-data'],folder)
        # Reject unused non-visual fields introduced by the catalog.
        warnings=[line for line in output.splitlines() if 'was not used' in line and 'ROOT.' in line]
        assert not warnings, '\n'.join(warnings)
        data=json.loads((folder/'user/script-output/data-raw-dump.json').read_text())
        settings=json.loads((folder/'user/script-output/mod-settings-dump.json').read_text())
        print('PASS',name,flush=True)
        return data,{key:value for group in settings.values() for key,value in group.items()}

    mapped=0
    for expansion in [False,True]:
        suffix='space-age' if expansion else 'base'
        vanilla,_=run('vanilla-'+suffix,expansion,False)
        default,settings=run('default-'+suffix,expansion)
        assert vanilla==default
        active=[e for e in CATALOG['entries'] if expansion or (not e['expansion'] and not e.get('feature'))]
        assert len(settings)==len(active)+51
        for e in active:
            prototype=settings[e['name']]
            assert prototype['type']==e['type']
            assert prototype['default_value']==expected_value(e,expansion),e['name']
        # Mutate every catalog option, one prototype family at a time. Compare all other prototypes.
        for kind in sorted({e['kind'] for e in active}):
            batch=[e for e in active if e['kind']==kind and (expansion or not e.get('freezing'))]
            overrides={e['name']:alternative(e,expansion) for e in batch}
            actual,_=run('mapping-'+suffix+'-'+kind,expansion,overrides=overrides)
            for e in batch:
                value=read_field(actual,e,expansion); wanted=overrides[e['name']]
                if e.get('energy'):
                    # Engine preserves the literal energy string in data.raw.
                    assert value.endswith(e['energy'])
                    value=float(value[:-len(e['energy'])])
                if isinstance(wanted,(int,float)) and not isinstance(wanted,bool):
                    assert math.isclose(value,wanted,rel_tol=1e-8,abs_tol=1e-8),(e['name'],value,wanted)
                else:assert value==wanted,(e['name'],value,wanted)
                mapped+=1
            expected=json.loads(json.dumps(vanilla))
            for e in batch:write_field(expected,e,read_field(actual,e,expansion),expansion)
            assert actual==expected,'An unlisted path or unrelated prototype changed: '+kind
    def key(kind, prototype, path):
        return next(e['name'] for e in CATALOG['entries'] if e['kind']==kind and e['prototype']==prototype and e['path']==path)
    laser_range=key('electric-turret','laser-turret',['attack_parameters','range'])
    flame_range=key('fluid-turret','flamethrower-turret',['attack_parameters','range'])
    laser_length=key('electric-turret','laser-turret',['attack_parameters','ammo_type','action','action_delivery','max_length'])
    derived,_=run('range-dependencies',True,overrides={laser_range:60,flame_range:60})
    assert derived['electric-turret']['laser-turret']['attack_parameters']['ammo_type']['action']['action_delivery']['max_length']==60
    assert derived['fluid-turret']['flamethrower-turret']['prepare_range']==60
    assert derived['beam']==vanilla['beam']
    explicit,_=run('explicit-limits',True,overrides={laser_range:60,laser_length:30,
        key('electric-turret','laser-turret',['attack_parameters','min_range']):80,
        key('fire','fire-flame',['initial_lifetime']):1000,key('fire','fire-flame',['maximum_lifetime']):100})
    assert explicit['electric-turret']['laser-turret']['attack_parameters']['ammo_type']['action']['action_delivery']['max_length']==30
    assert explicit['electric-turret']['laser-turret']['attack_parameters']['min_range']==60
    assert explicit['fire']['fire-flame']['initial_lifetime']==100
    print('PASS catalog: all registered settings,',mapped,'field mutations, exact defaults and family isolation.',flush=True)

if __name__=='__main__':main()
