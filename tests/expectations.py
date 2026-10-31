"""Independent expected native paths for the small public setting surface."""
import copy
import re

KEYS=['ammo-consumption-modifier','damage-modifier','energy-per-shot','fluid-consumption','manual-range','chain-jumps','line-length','rotation-speed','blast-radius','cooldown','range']


def split(name):
    for key in KEYS:
        if name.endswith('-'+key):return name[3:-len(key)-1],key
    raise AssertionError(name)


def target(data,weapon):
    if weapon=='artillery':return data['gun']['artillery-wagon-cannon']
    if weapon=='spidertron-rocket-launcher':return data['gun']['spidertron-rocket-launcher-1']
    for kind in ['gun','ammo-turret','electric-turret','fluid-turret']:
        if weapon in data[kind]:return data[kind][weapon]
    raise AssertionError(weapon)


def energy(text):
    number,prefix=re.fullmatch(r'([\d.eE+-]+)([kMGT]?)J',text).groups()
    return float(number)*{'':1,'k':1e3,'M':1e6,'G':1e9,'T':1e12}[prefix]


def defaults_and_limits(data,settings):
    for name,p in settings.items():
        weapon,key=split(name);default=p['default_value']
        if key=='rotation-speed':
            original=data['artillery-turret']['artillery-turret']['turret_rotation_speed']*21600;bounds=(1,360)
            assert data['artillery-wagon']['artillery-wagon']['turret_rotation_speed']*21600==original
        elif key=='blast-radius':original=data['artillery-projectile']['artillery-projectile']['action']['action_delivery']['target_effects'][0]['action']['radius'];bounds=(0.5,32)
        elif key=='line-length':original=data['ammo']['railgun-ammo']['ammo_type']['action']['range'];bounds=(1,256)
        elif key=='chain-jumps':
            chain='chain-tesla-gun-chain' if weapon=='teslagun' else 'chain-tesla-turret-chain'
            original=data['chain-active-trigger'][chain]['max_jumps'];bounds=(1,16)
        elif key=='manual-range':original=560;bounds=(33,4096)
        else:
            entity=target(data,weapon);attack=entity['attack_parameters']
            if key=='range':original=attack['range'];bounds=((attack.get('min_range',0)+1),1024 if weapon=='artillery' else 256)
            elif key=='cooldown':original=attack['cooldown'];bounds=(1,3600)
            elif key=='damage-modifier':original=attack.get('damage_modifier',1);bounds=(0,10)
            elif key=='fluid-consumption':original=attack['fluid_consumption'];bounds=(0,10)
            elif key=='energy-per-shot':
                original=energy(entity.get('energy_per_shot') or attack['ammo_type']['energy_consumption']);bounds=(0,100000000)
            else:
                original=attack.get('ammo_consumption_modifier',1)
                single=attack.get('ammo_category') in ['rocket','cannon-shell','artillery-shell','railgun']
                bounds=(0,1 if single else 10)
        assert original==default,(name,original,default)
        assert (p['minimum_value'],p['maximum_value'])==bounds,(name,bounds)


def mutated(settings):
    values={}
    for index,(name,p) in enumerate(sorted(settings.items()),1):
        _,key=split(name);default=p['default_value']
        if key=='range':value=default*1.25+index/1000
        elif key=='cooldown':value=default+2+index/1000
        elif key=='damage-modifier':value=default+0.2+index/1000
        elif key=='ammo-consumption-modifier':value=0.5 if p['maximum_value']==1 else 2+index/1000
        elif key=='energy-per-shot':value=default*2+index
        elif key=='fluid-consumption':value=2.5
        elif key=='chain-jumps':value=default+1
        elif key=='manual-range':value=700
        elif key=='line-length':value=80
        elif key=='rotation-speed':value=45+index/1000
        elif key=='blast-radius':value=8
        assert p['minimum_value']<=value<=p['maximum_value']
        values[name]=value
    return values


def expected(data,overrides):
    result=copy.deepcopy(data)
    def extend(node,value):
        if isinstance(node,list):
            for child in node:extend(child,value)
        elif isinstance(node,dict):
            if node.get('type')=='beam' and 'max_length'in node:node['max_length']=max(node['max_length'],value)
            for child in node.values():extend(child,value)
    for name,value in overrides.items():
        weapon,key=split(name)
        if weapon=='spidertron-rocket-launcher':
            for index in range(1,5):
                result['gun'][f'spidertron-rocket-launcher-{index}']['attack_parameters'][key.replace('-','_')]=value
            continue
        if key=='rotation-speed':
            for kind in ['artillery-turret','artillery-wagon']:result[kind][kind]['turret_rotation_speed']=value/21600
            continue
        if key=='blast-radius':
            result['artillery-projectile']['artillery-projectile']['action']['action_delivery']['target_effects'][0]['action']['radius']=value
            continue
        if key=='line-length':result['ammo']['railgun-ammo']['ammo_type']['action']['range']=value;continue
        if key=='chain-jumps':
            chain='chain-tesla-gun-chain' if weapon=='teslagun' else 'chain-tesla-turret-chain'
            result['chain-active-trigger'][chain]['max_jumps']=value;continue
        if key=='manual-range':continue
        entity=target(result,weapon);attack=entity['attack_parameters']
        if key=='range':
            attack['range']=value;extend(attack.get('ammo_type'),value)
            if 'prepare_range'in entity:entity['prepare_range']=max(entity['prepare_range'],value)
        elif key in ['cooldown','damage-modifier','ammo-consumption-modifier','fluid-consumption']:
            attack[key.replace('-','_')]=value
        elif key=='energy-per-shot':
            original=target(data,weapon)
            oldcost=energy(original.get('energy_per_shot') or original['attack_parameters']['ammo_type']['energy_consumption'])
            if 'energy_per_shot'in entity:entity['energy_per_shot']=str(value)+'J'
            else:attack['ammo_type']['energy_consumption']=str(value)+'J'
            capacity=energy(original['energy_source']['buffer_capacity'])
            required=value+max(0,capacity-oldcost)
            if required>capacity:entity['energy_source']['buffer_capacity']=str(required)+'J'
    if 'cr-artillery-range'in overrides or 'cr-artillery-manual-range'in overrides:
        ratio=overrides.get('cr-artillery-manual-range',560)/target(result,'artillery')['attack_parameters']['range']
        for kind in ['artillery-turret','artillery-wagon']:result[kind][kind]['manual_range_modifier']=ratio
    return result


def normalize_energy(data):
    if isinstance(data,list):return [normalize_energy(v) for v in data]
    if isinstance(data,dict):
        # The engine dump rounds derived native rotation doubles during JSON serialization.
        return {k:(float(format(v,'.12g')) if k=='turret_rotation_speed' else normalize_energy(v)) for k,v in data.items()}
    if isinstance(data,str) and re.fullmatch(r'[\d.eE+-]+[kMGT]?J',data):return energy(data)
    return data
