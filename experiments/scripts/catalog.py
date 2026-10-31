#!/usr/bin/env python3
"""Refresh the reviewed experimental catalog from official 2.1.24 dumps, without building.
Usage: python3 scripts/catalog.py --base BASE_JSON --space-age SA_JSON --api API_JSON
The committed catalog is used directly by Factorio; this tool is development-only.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FMAX = 3.402823466e38
UMAX = 4294967295
DIST = 1000000

# Explicitly reviewed behavioral fields, never a recursive sweep of arbitrary numeric data.
FIELDS = {
 'EntityWithHealthPrototype': 'max_health healing_per_tick repair_speed_modifier overkill_fraction alert_when_damaged create_ghost_on_death',
 'EntityWithOwnerPrototype': 'is_military_target',
 'TurretPrototype': 'rotation_speed rotation_speed_secondary prepare_range call_for_help_radius shoot_in_prepare_state start_attacking_only_when_can_shoot leave_attacking_if_shoot_fails attack_from_start_frame allow_turning_when_starting_attack can_retarget_while_starting_attack alert_when_attacking circuit_wire_max_distance',
 'AmmoTurretPrototype': 'inventory_size automated_ammo_count prepare_with_no_ammo energy_per_shot',
 'FluidTurretPrototype': 'fluid_buffer_size fluid_buffer_input_flow activation_buffer_ratio',
 'ArtilleryTurretPrototype': 'inventory_size ammo_stack_limit automated_ammo_count turret_rotation_speed manual_range_modifier alert_when_attacking disable_automatic_firing turn_after_shooting_cooldown cannon_parking_speed circuit_wire_max_distance',
 'ArtilleryWagonPrototype': 'inventory_size ammo_stack_limit automated_ammo_count turret_rotation_speed manual_range_modifier disable_automatic_firing turn_after_shooting_cooldown cannon_parking_speed',
 'CombatRobotPrototype': 'time_to_live follows_player friction range_from_player speed separation_range max_separation_force separation_force_factor',
 'CaptureRobotPrototype': 'capture_speed search_radius speed',
 'FlyingRobotPrototype': 'speed max_speed',
 'LandMinePrototype': 'trigger_radius timeout trigger_interval force_die_on_attack circuit_wire_max_distance',
 'ActiveDefenseEquipmentPrototype': 'automatic',
 'EnergyShieldEquipmentPrototype': 'max_shield_value energy_per_shield',
 'CarPrototype': 'turret_rotation_speed turret_return_timeout immune_to_all_impacts immune_to_cliff_impacts immune_to_rock_impacts immune_to_tree_impacts',
 'SpiderVehiclePrototype': 'automatic_weapon_cycling chain_shooting_cooldown_modifier torso_rotation_speed',
 'GatePrototype': 'activation_distance opening_speed timeout_to_close',
 'AmmoItemPrototype': 'magazine_size reload_time shoot_protected',
 'ArmorPrototype': 'inventory_size_bonus provides_flight',
 'ProjectilePrototype': 'acceleration max_speed piercing_damage turn_speed direction_only hit_at_collision_position turning_speed_increases_exponentially_with_projectile_speed',
 'ArtilleryProjectilePrototype': 'reveal_map',
 'BeamPrototype': 'damage_interval action_triggered_automatically',
 'ChainActiveTriggerPrototype': 'max_jumps max_range_per_jump max_range jump_delay_ticks fork_chance fork_chance_increase_per_quality_level max_forks_per_jump max_forks',
 'FluidStreamPrototype': 'particle_buffer_size particle_spawn_interval particle_spawn_timeout particle_horizontal_speed particle_horizontal_speed_deviation particle_vertical_acceleration target_initial_position_only initial_action',
 'FireFlamePrototype': 'damage_multiplier_decrease_per_tick damage_multiplier_increase_per_added_fuel maximum_damage_multiplier initial_lifetime maximum_lifetime lifetime_increase_by lifetime_increase_cooldown add_fuel_cooldown maximum_spread_count spread_delay spread_delay_deviation tree_dying_factor',
 'SmokeWithTriggerPrototype': 'action_cooldown attach_to_target fade_when_attachment_is_destroyed',
 'SmokePrototype': 'duration',
 'StickerPrototype': 'duration_in_ticks damage_interval fire_spread_cooldown fire_spread_radius ground_target target_movement_max target_movement_modifier target_movement_modifier_from target_movement_modifier_to vehicle_friction_modifier vehicle_speed_max vehicle_speed_modifier vehicle_speed_modifier_from vehicle_speed_modifier_to use_damage_substitute',
 'BaseAttackParameters': 'range min_range cooldown cooldown_deviation damage_modifier ammo_consumption_modifier warmup turn_range fire_penalty rotate_penalty health_penalty threatening_asteroid_penalty lead_target_for_projectile_speed lead_target_for_projectile_delay movement_slow_down_factor movement_slow_down_cooldown true_collinear_ejection use_shooter_direction',
 'ProjectileAttackParameters': 'projectile_creation_distance projectile_orientation_offset apply_projection_to_projectile_creation_position',
 'AmmoType': 'energy_consumption range_modifier cooldown_modifier consumption_modifier clamp_position force_clamp_to_max_range',
 'ElectricEnergySource': 'buffer_capacity input_flow_limit output_flow_limit drain',
 'StreamAttackParameters': 'fluid_consumption',
}
ROOT_KINDS = ['ammo-turret','electric-turret','fluid-turret','artillery-turret','gun','car','spider-vehicle','artillery-wagon','capsule','land-mine','combat-robot','active-defense-equipment','energy-shield-equipment','wall','gate','armor','ammo']
SHARED_KINDS = ['projectile','artillery-projectile','beam','stream','fire','smoke-with-trigger','sticker','chain-active-trigger','capture-robot']
# Resource references are traversed only to these behavioral prototype families.
REFS = {'projectile':['projectile','artillery-projectile'],'beam':['beam'],'stream':['stream'],
 'chain':['chain-active-trigger'],'sticker':['sticker'],'smoke_name':['smoke-with-trigger'],
 'entity_name':['combat-robot','capture-robot','projectile','fire','smoke-with-trigger'],
 'spread_fire_entity':['fire'],'spawn_entity':['fire'],'fire':['fire']}
NOTES = {
 'range': ('Maximum targeting distance before native quality bonuses. Very large ranges can exhaust memory.', '品质加成前的最大索敌距离。超大射程可能耗尽内存。'),
 'min_range': ('Minimum targeting distance; clamped to maximum range if reversed.', '最小索敌距离；超过最大射程时限制为最大射程。'),
 'cooldown': ('Ticks between shots before research. Shots per second = 60 / cooldown.', '研究加成前的射击间隔。每秒射数 = 60 / 间隔。'),
 'warmup': ('Delay after a shooting order, separate from turret preparation.', '接到射击指令后的延迟，与炮塔展开准备时间分开。'),
 'damage_modifier': ('Native damage coefficient; ammunition and technology still contribute.', '原生伤害系数；弹药和科技加成仍然生效。'),
 'ammo_consumption_modifier': ('Native consumption per shot; one unit means one round, not a magazine.', '原生每次射击消耗系数；一单位是一发子弹而非整个弹匣。'),
 'magazine_size': ('Shots per ammunition item. Shared by every weapon using this ammo.', '每件弹药的射击次数；影响所有使用该弹药的武器。'),
 'max_length': ('Delivery travel limit. Range edits raise this limit only when necessary; an explicit value takes precedence.', '攻击传递距离限制。修改射程仅在必要时提高此限制；显式填写本项时优先使用此值。'),
 'max_range': ('Maximum travel or chain distance; affects all consumers of this effect.', '最大飞行或连锁距离；影响此效果的所有使用者。'),
 'amount': ('Absolute damage per application, before native modifiers and resistances. Negative values can heal.', '每次施加的绝对伤害，随后应用原生系数与抗性。负值可治疗。'),
 'radius': ('Action radius in tiles. Large areas and repeated actions can be expensive.', '动作作用半径，单位格。大范围和重复动作可能消耗大量资源。'),
 'repeat_count': ('Number of applications/spawns. Large counts can exhaust memory or CPU.', '作用或生成次数。过大可能耗尽内存或 CPU。'),
 'inventory_size': ('Inventory slots. Shrinking inventories may discard stored items.', '库存槽数；减少槽数可能丢失已存物品。'),
 'manual_range_modifier': ('Artillery manual targeting range coefficient. Automatic range is in the shared artillery gun.', '火炮手动瞄准射程系数；自动射程由共享火炮武器设置控制。'),
 'turn_range': ('Fraction of a full circle. Engine clamps values between 0.5 and 1 to 0.5, except exactly 1.', '完整圆周的比例。引擎会将 0.5 与 1 之间的值限制为 0.5，恰好 1 除外。'),
 'healing_per_tick': ('Health regenerated per tick. Negative values cause health loss.', '每 tick 恢复生命；负值造成掉血。'),
 'initial_lifetime': ('Initial fire lifetime. Kept at or below maximum lifetime when changed.', '火焰初始寿命；修改时不超过最大寿命。'),
 'prepare_range': ('Native preparation search radius, separate from firing range. -1 preserves automatic behavior.', '原生准备索敌半径，与开火射程分开。-1 保留自动行为。'),
 'target_movement_modifier': ('Multiplier of target movement speed; zero immobilizes.', '目标移动速度系数；0 使目标无法移动。'),
 'fork_chance': ('Chance of an additional chain branch, from 0 to 1.', '额外连锁分支概率，0 到 1。'),
}
ZH = dict(x.split(':',1) for x in '''range:射程
min_range:最小射程
cooldown:射击间隔
cooldown_deviation:间隔随机偏差
damage_modifier:伤害系数
ammo_consumption_modifier:弹药消耗系数
warmup:开火延迟
turn_range:攻击圆周比例
fire_penalty:燃烧目标惩罚
rotate_penalty:转向惩罚
health_penalty:目标生命比例惩罚
threatening_asteroid_penalty:威胁性星岩惩罚
lead_target_for_projectile_speed:弹道预判速度
lead_target_for_projectile_delay:弹道预判延迟
movement_slow_down_factor:开火移动速度系数
movement_slow_down_cooldown:开火减速持续时间
true_collinear_ejection:共线发射
max_health:最大生命值
healing_per_tick:每 tick 生命恢复
repair_speed_modifier:维修速度系数
overkill_fraction:过量伤害预测余量
alert_when_damaged:受损警报
create_ghost_on_death:死亡后生成幽灵
is_military_target:军事目标
rotation_speed:转向速度
rotation_speed_secondary:备用转向速度
prepare_range:准备索敌半径
call_for_help_radius:呼叫支援半径
shoot_in_prepare_state:准备状态中射击
start_attacking_only_when_can_shoot:可射击时才开始攻击
leave_attacking_if_shoot_fails:射击失败时退出攻击
attack_from_start_frame:从开始帧攻击
allow_turning_when_starting_attack:开始攻击时转向
can_retarget_while_starting_attack:开始攻击时重选目标
alert_when_attacking:攻击警报
circuit_wire_max_distance:信号线连接距离
inventory_size:库存槽数
automated_ammo_count:自动补弹目标
prepare_with_no_ammo:无弹药时准备
energy_per_shot:每次射击能量
fluid_buffer_size:流体弹药缓冲容量
fluid_buffer_input_flow:流体弹药输入流量
activation_buffer_ratio:重新激活缓冲比例
ammo_stack_limit:弹药堆叠限制
turret_rotation_speed:炮台转向速度
manual_range_modifier:火炮手动射程系数
disable_automatic_firing:禁止自动开火
turn_after_shooting_cooldown:开火后转向延迟
cannon_parking_speed:炮管归位速度
time_to_live:存活时间
follows_player:跟随玩家
friction:摩擦系数
range_from_player:与玩家距离
speed:速度
separation_range:分离作用距离
max_separation_force:最大分离力
separation_force_factor:分离力系数
capture_speed:捕获速度
search_radius:搜索半径
trigger_radius:触发半径
timeout:布设后武装延迟
trigger_interval:触发检查间隔
force_die_on_attack:攻击后自毁
automatic:自动攻击
max_shield_value:护盾容量
energy_per_shield:每点护盾能耗
turret_return_timeout:炮台回正延迟
immune_to_all_impacts:免疫全部碰撞
immune_to_cliff_impacts:免疫悬崖碰撞
immune_to_rock_impacts:免疫岩石碰撞
immune_to_tree_impacts:免疫树木碰撞
automatic_weapon_cycling:自动轮换武器
chain_shooting_cooldown_modifier:轮换开火间隔系数
torso_rotation_speed:躯干转向速度
activation_distance:启动距离
opening_speed:开门速度
timeout_to_close:关闭延迟
magazine_size:弹匣容量
reload_time:换弹额外时间
shoot_protected:允许攻击受保护目标
inventory_size_bonus:背包容量加成
provides_flight:提供飞行
acceleration:加速度
max_speed:最大速度
piercing_damage:穿透生命预算
turn_speed:弹道转向速度
direction_only:仅按方向飞行
hit_at_collision_position:在碰撞位置命中
turning_speed_increases_exponentially_with_projectile_speed:转向随弹速指数增长
reveal_map:揭示地图
damage_interval:伤害施加间隔
action_triggered_automatically:自动触发伤害
max_jumps:最大连锁跳数
max_range_per_jump:每跳最大距离
max_range:最大距离
jump_delay_ticks:连锁跳跃延迟
fork_chance:分支概率
fork_chance_increase_per_quality_level:每品质等级分支概率增量
max_forks_per_jump:每跳最大分支
max_forks:总分支上限
particle_buffer_size:流弹缓冲数量
particle_spawn_interval:流弹生成间隔
particle_spawn_timeout:流弹停止生成延迟
particle_horizontal_speed:流弹水平速度
particle_horizontal_speed_deviation:流弹水平速度偏差
particle_vertical_acceleration:流弹垂直加速度
target_initial_position_only:仅瞄准初始位置
damage_multiplier_decrease_per_tick:每 tick 伤害系数衰减
damage_multiplier_increase_per_added_fuel:补充燃料伤害系数增量
maximum_damage_multiplier:最大伤害系数
initial_lifetime:初始寿命
maximum_lifetime:最大寿命
lifetime_increase_by:寿命延长量
lifetime_increase_cooldown:延长寿命冷却
add_fuel_cooldown:补充燃料冷却
maximum_spread_count:最大蔓延次数
spread_delay:蔓延延迟
spread_delay_deviation:蔓延延迟偏差
tree_dying_factor:树木死亡系数
action_cooldown:效果施加间隔
attach_to_target:附着于目标
fade_when_attachment_is_destroyed:目标消失后消散
duration:持续时间
duration_in_ticks:持续时间
fire_spread_cooldown:火焰蔓延冷却
fire_spread_radius:火焰蔓延半径
ground_target:禁止目标飞行
target_movement_max:目标速度上限
target_movement_modifier:目标移动速度系数
target_movement_modifier_from:初始移动速度系数
target_movement_modifier_to:最终移动速度系数
vehicle_friction_modifier:载具摩擦系数
vehicle_speed_max:载具速度上限
vehicle_speed_modifier:载具速度系数
vehicle_speed_modifier_from:初始载具速度系数
vehicle_speed_modifier_to:最终载具速度系数
use_damage_substitute:使用替代伤害
energy_consumption:射击能耗
range_modifier:弹药射程系数
cooldown_modifier:弹药射击间隔系数
consumption_modifier:弹药消耗系数
clamp_position:将瞄准位置限制在射程内
force_clamp_to_max_range:强制射向最大射程
buffer_capacity:能量缓冲容量
input_flow_limit:能量输入功率
output_flow_limit:能量输出功率
drain:待机功率
fluid_consumption:每次射击流体消耗
amount:伤害数值
radius:作用半径
repeat_count:重复次数
starting_speed:初始飞行速度
starting_speed_deviation:初始飞行速度偏差
max_length:攻击传递最大距离
direction_deviation:散射方向偏差
range_deviation:射程随机偏差
projectile_count:投射物数量
probability:生效概率
distance:距离
volume:流体容量
energy_usage:功耗
energy:能量
max_distance:最大距离
count:数量
preparing_speed:准备速度
folding_speed:收起速度
starting_attack_speed:开始攻击速度
ending_attack_speed:结束攻击速度
percent:百分比抗性
decrease:固定抗性
heating_energy:防冻供热需求
mining_time:采掘时间
physical:物理
impact:撞击
poison:毒素
explosion:爆炸
fire:火焰
laser:激光
acid:酸液
electric:电击'''.splitlines())


ZH.update({'use_shooter_direction':'使用射手朝向','projectile_creation_distance':'投射物生成距离','projectile_orientation_offset':'发射方向偏移','apply_projection_to_projectile_creation_position':'发射位置应用投影','cluster_count':'集群数量','distance_deviation':'距离偏差','initial_ground_flame_count':'初始地面火焰数量','range_mode':'射程测量方式','width':'线性攻击宽度'})

def lua(v):
 if isinstance(v,dict): return '{'+','.join('['+json.dumps(k)+']='+lua(x) for k,x in v.items() if x is not None)+'}'
 if isinstance(v,list): return '{'+','.join(lua(x) for x in v)+'}'
 if isinstance(v,bool): return 'true' if v else 'false'
 return json.dumps(v,ensure_ascii=True)

def get(obj,path,default=None):
 try:
  for key in path: obj=obj[key-1] if isinstance(key,int) else obj[key]
  return obj
 except (KeyError,IndexError,TypeError): return default


def counterpart(source, target, path):
 def signature(value):
  if not isinstance(value,dict):return None
  return (value.get('type'),get(value,['damage','type']),value.get('source_type'),value.get('beam'),value.get('projectile'),value.get('entity_name'))
 result=[]
 for key in path:
  if isinstance(key,int):
   if not isinstance(source,list) or key>len(source):return None
   chosen=source[key-1];sig=signature(chosen)
   ordinal=sum(signature(v)==sig for v in source[:key])
   if isinstance(target,list):
    matches=[(i,v) for i,v in enumerate(target,1) if signature(v)==sig]
    if len(matches)<ordinal:return None
    i,target=matches[ordinal-1];result.append(i)
   elif isinstance(target,dict) and ordinal==1 and signature(target)==sig:pass
   else:return None
   source=chosen
  else:
   if isinstance(target,list):
    matches=[(i,v) for i,v in enumerate(target,1) if signature(v)==signature(source)]
    if not matches:return None
    i,target=matches[0];result.append(i)
   if not isinstance(target,dict):return None
   result.append(key);target=target.get(key)
   source=source.get(key) if isinstance(source,dict) else None
 return result

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--base',type=Path,required=True); ap.add_argument('--space-age',type=Path,required=True); ap.add_argument('--api',type=Path,required=True); args=ap.parse_args()
 base=json.loads(args.base.read_text()); space=json.loads(args.space_age.read_text()); api=json.loads(args.api.read_text()); types={p['name']:p for p in api['prototypes']+api['types']}; bykind={p['typename']:p['name'] for p in api['prototypes'] if 'typename'in p}
 def props(name):
  p=types[name]; return {**(props(p['parent']) if p.get('parent') else {}),**{x['name']:x for x in p.get('properties',[])}}
 def reviewed(name):
  p=types[name]; return set(FIELDS.get(name,'').split()) | (reviewed(p['parent']) if p.get('parent') else set())
 selected={(k,n) for k in ROOT_KINDS for n in space.get(k,{})}
 def refs(obj):
  if isinstance(obj,list):
   for x in obj: yield from refs(x)
  elif isinstance(obj,dict):
   for k,v in obj.items():
    if k in REFS and isinstance(v,str):
     for kind in REFS[k]:
      if v in space.get(kind,{}): yield kind,v
    if k=='created_effect':continue
    if isinstance(v,(dict,list)): yield from refs(v)
 while True:
  extra={r for k,n in selected for r in refs(space[k][n])}
  if extra<=selected:break
  selected|=extra
 # Ignore smoke-only visual dummies; they have no damaging action.
 selected={x for x in selected if not (x[0]=='smoke-with-trigger' and 'action' not in space[x[0]][x[1]])}
 reverse={}
 for k,records in space.items():
  if not isinstance(records,dict):continue
  for n,prototype in records.items():
   for ref in set(refs(prototype)):reverse.setdefault(ref,set()).add(k+'/'+n)
 entries=[]; groups=[]; omitted={}; used=set()
 legacy_src=(ROOT/'prototypes/catalog.lua').read_text().split('-- Generated additional settings.')[0]
 legacy_paths={}
 for line in legacy_src.splitlines():
  m=re.search(r'key = "([^"]+)"',line)
  if not m:continue
  key=m[1]; f=re.search(r'(attack|field|duration) = "([^"]+)"',line)
  if f: legacy_paths[key]=(['attack_parameters',f[2]] if f[1]=='attack' else [f[2]])
 for key,path in {'prepare-range':['prepare_range'],'healing-per-second':['healing_per_tick'],'mining-time':['minable','mining_time'],'heating-energy':['heating_energy']}.items(): legacy_paths[key]=path
 legacy_skip={tuple(v) for v in legacy_paths.values()}
 legacy_skip|={('rotation_speed_secondary',),('preparing_speed_secondary',),('folding_speed_secondary',)}
 def add(kind,name,path,value,meta=None,**opts):
  if value is None or not isinstance(value,(bool,int,float,str)):return
  if kind=='ammo-turret' and name=='gun-turret' and (tuple(path) in legacy_skip or path[0]=='resistances'):return
  ident='cr-'+kind+'-'+name+'-'+('-'.join(str(x).replace('_','-') for x in path))
  if ident in used:return
  field=str(path[-1]); meta=meta or {}; dtype=meta.get('type'); energy=dtype=='Energy'
  seen=set()
  while isinstance(dtype,str) and dtype not in ['float','double','uint8','uint16','uint32','MapTick','FluidAmount'] and dtype in types and dtype not in seen and isinstance(types[dtype].get('type'),str):
   seen.add(dtype);dtype=types[dtype]['type']
  if energy:
   m=re.fullmatch(r'([\d.eE+-]+)\s*([kMGTPEZY]?)?([JW])',str(value))
   if not m:return
   value=float(m[1])*10**(3*('kMGTPEZY'.find(m[2])+1) if m[2] else 0)
  typ='bool-setting' if isinstance(value,bool) else 'double-setting'
  maxval=FMAX; minval=0
  if dtype in ['uint8','uint16','uint32','MapTick','ItemCountType','ItemStackIndex'] or opts.get('integer'):
   typ='int-setting';maxval={'uint8':255,'uint16':65535,'ItemStackIndex':65535}.get(dtype,UMAX)
  if field in ['amount','healing_per_tick','fire_penalty','rotate_penalty','health_penalty','threatening_asteroid_penalty','acceleration']:minval=-FMAX
  if field in ['target_movement_max','vehicle_speed_max','prepare_range','max_speed','max_range']:minval=-1
  if field in ['cooldown','movement_slow_down_cooldown']: minval=0.001;maxval=UMAX
  if field in ['max_health','energy_per_shield','cannon_parking_speed','manual_range_modifier','capture_speed']:minval=0.001
  if field in ['magazine_size','inventory_size','ammo_stack_limit','trigger_interval','damage_interval','duration_in_ticks','maximum_lifetime']:minval=1
  if field in ['cooldown_deviation','probability','fork_chance','activation_buffer_ratio','rotation_speed','rotation_speed_secondary','turn_range','percent']:maxval=100 if field=='percent' else 1
  if any(t in field for t in ['range','radius','max_length','max_distance','distance']) and field not in ['range_modifier','range_deviation']:maxval=DIST
  if field.endswith('_speed') and field in ['preparing_speed','folding_speed','starting_attack_speed','ending_attack_speed']:minval=0.000000001;maxval=1
  if field in ['range_modifier','cooldown_modifier']:minval=0.001
  if field=='projectile_creation_distance':minval=-DIST;maxval=DIST
  if field=='projectile_orientation_offset':minval=-1;maxval=1
  if field=='fluid_buffer_size' or field=='volume':minval=0.001
  if isinstance(value,(int,float)) and value < 0:minval=min(minval,value)
  unit='J' if energy and str(meta.get('energy_unit','J'))=='J' else ''
  if energy:unit='W' if field in ['input_flow_limit','output_flow_limit','drain','heating_energy','energy_usage'] else 'J'
  if not unit:
   if field in ['fluid_consumption']:unit='fluid/shot'
   elif field=='fluid_buffer_input_flow':unit='fluid/tick'
   elif field in ['speed','max_speed','particle_horizontal_speed','particle_horizontal_speed_deviation']:unit='tiles/tick'
   elif field in ['rotation_speed','rotation_speed_secondary','turret_rotation_speed','torso_rotation_speed','turn_speed']:unit='turns/tick'
   elif field in ['range','min_range','prepare_range','radius','max_range','max_range_per_jump','max_length','distance','trigger_radius','search_radius','call_for_help_radius','circuit_wire_max_distance','activation_distance','separation_range','range_from_player']:unit='tiles'
   elif field in ['cooldown','warmup','reload_time','time_to_live','timeout','trigger_interval','damage_interval','duration','duration_in_ticks','jump_delay_ticks','action_cooldown','timeout_to_close','turn_after_shooting_cooldown','turret_return_timeout','initial_lifetime','maximum_lifetime','spread_delay','spread_delay_deviation','lifetime_increase_by','lifetime_increase_cooldown','add_fuel_cooldown','movement_slow_down_cooldown']:unit='ticks'
   elif field in ['max_health','amount','decrease','max_shield_value']:unit='HP'
   elif field=='healing_per_tick':unit='HP/tick'
   elif field=='percent':unit='%'
  if len(path)>1 and path[-2]=='damage_per_tick':unit='HP/tick'
  english=field.replace('_',' ').capitalize(); zh=ZH.get(field,english)
  desc,desczh=NOTES.get(field,(english+'. Uses the native engine property; only this listed path is changed.',zh+'。使用引擎原生属性，仅修改列出的字段。'))
  shared=kind in SHARED_KINDS or kind=='ammo' or (kind=='gun' and name=='artillery-wagon-cannon')
  if len(path)>1 and path[-2]=='damage_per_tick':desc='Native damage-per-tick amount; scheduling follows the native damage interval.';desczh='原生每 tick 伤害量；施加时机遵循原生伤害间隔。'
  desc += ' Scope: '+('shared resource; all consumers listed in PARAMETERS.md.' if shared else kind+'/'+name+'.')
  desczh += ' 影响范围：'+('共享资源，详见 PARAMETERS.md 中的全部使用者。' if shared else name+'。')
  if field in ['max_jumps','max_forks','max_forks_per_jump','projectile_count','count','repeat_count']:desc+=' Large counts can exhaust CPU or memory.';desczh+=' 数量过大可能耗尽 CPU 或内存。'
  e=dict(name=ident,kind=kind,prototype=name,path=path,default=value,type=typ,min=minval,max=maxval,unit=unit,energy=unit if energy else None,expansion=name not in base.get(kind,{}),label=english,zh=zh,description=desc,description_zh=desczh,shared=shared)
  if typ=='bool-setting':e.pop('min');e.pop('max')
  # Space Age sometimes changes base prototypes; defaults must match the active official data.
  basepath=counterpart(space[kind][name],base.get(kind,{}).get(name,{}),path) if not opts.get('resistance') else path
  if name in base.get(kind,{}) and basepath is None:e['expansion']=True
  if basepath is not None and basepath!=path:e['base_path']=basepath
  bv=get(base.get(kind,{}).get(name,{}),basepath or path)
  if bv is not None and bv!=get(space[kind][name],path) and not energy and isinstance(bv,(int,float,bool,str)):e['base_default']=bv
  if field in ['max_speed','max_range','target_movement_max','vehicle_speed_max'] and value == -1:
   e['sentinel']=True;e['description']+=' -1 preserves the native unlimited default.';e['description_zh']+=' -1 保留原生无限制默认值。'
  if field=='provides_flight':e['feature']='space_travel'
  e.update(opts); entries.append(e);used.add(ident)
 def scalar_fields(kind,name,obj,path,typename,keys=None):
  pp=props(typename)
  for key in sorted(keys if keys is not None else reviewed(typename)):
   m=pp.get(key)
   if not m:continue
   if key=='provides_flight' and (obj.get('collision_box') or obj.get('drawing_box')):continue
   if kind=='fluid-turret' and key=='start_attacking_only_when_can_shoot':continue
   v=obj.get(key)
   if v is None:
    default=m.get('default');v=default.get('value') if isinstance(default,dict) and default.get('complex_type')=='literal' else None
   if v is None and isinstance(m.get('default'),str) and 'uint32' in m['default'].lower():v=UMAX
   if v is None and key in ['max_speed','max_range']:v=-1
   if v is None:continue
   if not isinstance(v,(bool,int,float,str)):continue
   if not isinstance(m['type'],str) or m['type'] not in ['boolean','float','double','uint8','uint16','uint32','MapTick','ItemCountType','ItemStackIndex','Energy','FluidAmount','Speed','RealOrientation']:continue
   add(kind,name,path+[key],v,m)
 def actions(kind,name,obj,path=()):
  if isinstance(obj,list):
   for i,v in enumerate(obj,1):actions(kind,name,v,(*path,i))
  elif isinstance(obj,dict):
   # Only behavioral action branches, with numeric leaves on known trigger types.
   typ=obj.get('type')
   allowed={
    'area':['radius','repeat_count','probability'], 'direct':['repeat_count','probability'],
    'line':['range','width','range_effects','repeat_count'],
    'projectile':['starting_speed','starting_speed_deviation','direction_deviation','range_deviation','max_range'],
    'stream':['starting_speed','starting_speed_deviation'],
    'beam':['max_length','duration'], 'damage':['amount'], 'damage-tile':['radius'],
    'push-back':['distance'], 'create-entity':['repeat_count'], 'create-fire':['initial_ground_flame_count'],
    'create-smoke':['duration'], 'cluster':['cluster_count','distance','distance_deviation','repeat_count'],
    'destroy-cliffs':['radius'], 'destroy-decoratives':['radius']}.get(typ,[])
   if 'damage' in obj and isinstance(obj['damage'],dict):
    add(kind,name,list(path)+['damage','amount'],obj['damage'].get('amount'))
   for key in allowed:
    if key in obj and isinstance(obj[key],(bool,int,float)):
     add(kind,name,list(path)+[key],obj[key],integer=key in ['repeat_count','cluster_count','duration','initial_ground_flame_count'])
   for key in ['action','final_action','action_on_die','attack_parameters','capsule_action','ammo_type','action_delivery','source_effects','target_effects']:
    if key in obj:actions(kind,name,obj[key],(*path,key))
 for kind,name in sorted(selected,key=lambda x: ((ROOT_KINDS+SHARED_KINDS).index(x[0]),x[1])):
  p=space[kind][name]; begin=len(entries); scalar_fields(kind,name,p,[],bykind[kind])
  if kind in ['ammo-turret','electric-turret','fluid-turret']:
   for key in ['preparing_speed','folding_speed','starting_attack_speed','ending_attack_speed']:
    if key.replace('_speed','_animation') in p:add(kind,name,[key],p.get(key,p.get('default_speed',1)))
  for path in [['attack_parameters'],['capsule_action','attack_parameters']]:
   attack=get(p,path)
   if not isinstance(attack,dict):continue
   keys=reviewed('BaseAttackParameters')
   if kind=='capsule':keys-= {'warmup'}
   if kind not in ['gun','capsule']:keys-= {'movement_slow_down_factor','movement_slow_down_cooldown'}
   scalar_fields(kind,name,attack,path,'BaseAttackParameters',keys)
   if attack.get('type')=='projectile':scalar_fields(kind,name,attack,path,'ProjectileAttackParameters',reviewed('ProjectileAttackParameters')-reviewed('BaseAttackParameters'))
   if attack.get('type')=='stream':scalar_fields(kind,name,attack,path,'StreamAttackParameters',{'fluid_consumption'})
   if 'range_mode' in props('BaseAttackParameters'):
    add(kind,name,path+['range_mode'],attack.get('range_mode','center-to-center'),type='string-setting',allowed=['center-to-center','bounding-box-to-bounding-box','center-to-bounding-box'])
   if 'ammo_type' in attack and isinstance(attack['ammo_type'],dict):scalar_fields(kind,name,attack['ammo_type'],path+['ammo_type'],'AmmoType')
   if 'fluids' in attack:
    for i,f in enumerate(attack['fluids'],1):add(kind,name,path+['fluids',i,'damage_modifier'],f.get('damage_modifier',1))
  if kind=='ammo':
   ammo=p['ammo_type']; variants=enumerate(ammo,1) if isinstance(ammo,list) else [(None,ammo)]
   for i,v in variants:scalar_fields(kind,name,v,['ammo_type']+([i] if i else []),'AmmoType')
  if 'max_health' in p or kind=='armor':
   for damage in ['physical','impact','poison','explosion','fire','laser','acid','electric']:
    existing=next((r for r in p.get('resistances',[]) if r['type']==damage),{})
    for component in ['decrease','percent']:
     add(kind,name,['resistances',damage,component],existing.get(component,0),resistance=True)
  if 'energy_source' in p and p['energy_source']['type']=='electric':scalar_fields(kind,name,p['energy_source'],['energy_source'],'ElectricEnergySource')
  for key in ['energy_usage','energy_per_shot','energy_per_shield']:
   if key in p:add(kind,name,[key],p[key],{'type':'Energy'})
  if 'minable'in p:add(kind,name,['minable','mining_time'],p['minable']['mining_time'])
  if 'heating_energy'in p:add(kind,name,['heating_energy'],p['heating_energy'],{'type':'Energy'},freezing=True)
  if 'fluid_box'in p:add(kind,name,['fluid_box','volume'],p['fluid_box']['volume'])
  for key in ['damage_per_tick','damage']:
   if isinstance(p.get(key),dict) and 'amount'in p[key]:add(kind,name,[key,'amount'],p[key]['amount'])
  actions(kind,name,p)
  for attackpath in [['attack_parameters'],['capsule_action','attack_parameters']]:
   a=get(p,attackpath)
   if isinstance(a,dict) and 'ammo_type'in a:actions(kind,name,a['ammo_type'],tuple(attackpath+['ammo_type']))
  groupentries=entries[begin:]
  if kind=='ammo':
   category=p.get('ammo_category'); ammo=p.get('ammo_type',{})
   if not category and isinstance(ammo,dict):category=ammo.get('category')
   reverse[(kind,name)]={k+'/'+n for k in ['gun','ammo-turret'] for n,v in space.get(k,{}).items() if category and v.get('attack_parameters',{}).get('ammo_category')==category}
  if groupentries:groups.append(dict(kind=kind,name=name,expansion=name not in base.get(kind,{}),settings=len(groupentries),shared=kind in SHARED_KINDS or kind=='ammo',consumers=sorted(reverse.get((kind,name),set()))))
  covered={e['path'][0] for e in groupentries}
  omitted[kind+'/'+name]=sorted(k for k in p if k not in covered)
 # Persist plain data: easy to delete individual settings without introducing runtime discovery.
 (ROOT/'prototypes/catalog.lua').write_text(legacy_src.rstrip()+'\n\n-- Generated additional settings. Refreshed by scripts/catalog.py.\nlocal catalog = {\n'+',\n'.join('  '+lua({k:v for k,v in e.items() if k not in ['label','zh','description','description_zh','shared']}) for e in entries)+'\n}\n\nreturn {gun_turret=definitions, catalog=catalog}\n')
 (ROOT/'tests/catalog.json').write_text(json.dumps(dict(entries=entries,groups=groups,omitted=omitted),indent=2,ensure_ascii=False)+'\n')
 for language in ['en','zh-CN']:
  lines=['[mod-setting-name]']
  for e in entries:
   label=e['label'] if language=='en' else e['zh']; path='.'.join(map(str,e['path'][:-1])); shared=(' [shared]' if language=='en' else ' [共享]') if e['shared'] else ''
   lines.append(e['name']+'='+shared.strip()+(' / ' if shared else '')+(path+' / ' if path else '')+label+(' ('+e['unit']+')' if e['unit'] else ''))
  lines+=['','[mod-setting-description]']
  for e in entries:
   default=e['default']; text=e['description'] if language=='en' else e['description_zh']
   text+=(' Default: ' if language=='en' else ' 默认值：')+str(default)+(' '+e['unit'] if e['unit'] else '')+'.'
   text+=(' Exact field: ' if language=='en' else ' 精确字段：')+'.'.join(map(str,e['path']))+'.'
   if 'base_default'in e:text+=(' Base-game default: ' if language=='en' else ' 基础游戏默认值：')+str(e['base_default'])+'.'
   lines.append(e['name']+'='+text)
  lines+=['','[string-mod-setting]']
  choices={'center-to-center':('Center to center','中心到中心'),'bounding-box-to-bounding-box':('Bounding box to bounding box','包围盒到包围盒'),'center-to-bounding-box':('Center to bounding box','中心到包围盒')}
  for e in entries:
   for choice in e.get('allowed',[]):
    labels=choices[choice];lines.append(e['name']+'-'+choice+'='+labels[0 if language=='en' else 1])
  import configparser, io
  merged=configparser.ConfigParser(interpolation=None,delimiters=('=',));merged.optionxform=str
  merged.read(ROOT/'locale'/language/'settings.cfg')
  for section in ['mod-setting-name','mod-setting-description','string-mod-setting']:
   for key in list(merged[section]):
    if not key.startswith('cr-gun-turret-'):del merged[section][key]
  generated=configparser.ConfigParser(interpolation=None,delimiters=('=',));generated.optionxform=str
  generated.read_string('\n'.join(lines))
  for section in generated.sections():
   for key,value in generated[section].items():merged[section][key]=value
  output=io.StringIO();merged.write(output,space_around_delimiters=False)
  (ROOT/'locale'/language/'settings.cfg').write_text(output.getvalue().rstrip()+'\n')
 # Include the retained legacy settings with their original user-facing explanations.
 import configparser
 cfg=configparser.ConfigParser(interpolation=None,delimiters=('=',));cfg.read(ROOT/'locale/en/settings.cfg')
 doc=['# Combat Reconfigured experimental parameter inventory','','See the [experimental README](README.md) and [validation notes](TESTING.md).','','Official source: Factorio 2.1.24 base + Space Age prototype dumps and matching API. All defaults are no-ops. Native research/quality remain active. Paths with numeric components use Lua one-based array indices. Energy settings use absolute joules or watts; 60 ticks = one second.','','## Retained gun turret controls','','These 51 `cr-gun-turret-*` controls share `prototypes/catalog.lua` with all additional settings. Their specialized conversions are preserved, and the generated entries avoid overlapping their paths.','', '| Setting | Default | Meaning |','| --- | --- | --- |']
 for key,text in cfg['mod-setting-description'].items():
  if not key.startswith('cr-gun-turret-'):continue
  default=re.search(r'Default: ([^.]+(?:\.[0-9]+)?)',text)
  doc.append('| `'+key+'` | '+(default[1] if default else 'See description')+' | '+text.replace('|','/')+' |')
 doc+=['','## Catalog summary','',f'{len(entries)} additional settings across {len(groups)} prototype records; {len(entries)+51} settings total with Space Age. Only available official content is registered.','', '| Prototype family | Records | Settings |','| --- | ---: | ---: |']
 for kind in ROOT_KINDS+SHARED_KINDS:
  gs=[g for g in groups if g['kind']==kind]
  if gs:doc.append(f'| {kind} | {len(gs)} | {sum(g["settings"] for g in gs)} |')
 for g in groups:
  doc+=['',f'## {g["kind"]} / {g["name"]}', '',('Space Age only. ' if g['expansion'] else 'Base game. ')+('Shared resource; changing it affects every consumer. ' if g['shared'] else 'Changes target this prototype. ')]
  if g['consumers']:doc+=['Direct combat consumers: '+', '.join('`'+x+'`' for x in g['consumers'])+'.']
  if g['kind']=='gun' and g['name']=='artillery-wagon-cannon':doc+=['Shared by the artillery turret and artillery wagon.']
  doc+=['','| Setting | Exact property | Official default | Unit | Meaning |','| --- | --- | --- | --- | --- |']
  for e in entries:
   if (e['kind'],e['prototype'])!=(g['kind'],g['name']):continue
   doc.append('| `'+e['name']+'` | `'+'.'.join(map(str,e['path']))+(' (base: '+'.'.join(map(str,e['base_path']))+')' if 'base_path' in e else '')+'` | '+str(e['default'])+(' (base: '+str(e['base_default'])+')' if 'base_default'in e else '')+' | '+e['unit']+' | '+e['description']+' |')
  doc+=['','Not exposed on this record: '+', '.join('`'+x+'`' for x in omitted[g['kind']+'/'+g['name']])+'. See exclusion policy below.']
 doc+=['','## Dependencies and exclusions','','- Range changes raise embedded beam delivery length limits when they would otherwise truncate the configured range. Explicit delivery length overrides take precedence. Increasing a turret range raises an insufficient explicit preparation radius unless it is also configured. Shared projectile/ammo ranges are separate controls and never silently rewritten by a gun setting. Artillery targeting uses its shared gun; manual range coefficients belong to each artillery entity.','- Reversed min/max ranges are clamped with a log. Fire initial lifetime is clamped to its maximum if either changes. Impossible fluid-turret state overrides forced by the engine are omitted. Exponential projectile turning requires nonzero acceleration; otherwise that toggle is kept disabled and logged. The dependency repairs are listed in the runtime-free data-stage code.','- Graphics, sound, sprite/particle geometry, identifiers, references to other prototypes, collision masks, equipment grid/shape references and recipe/technology definitions are excluded. These cannot be meaningful independent numeric controls without changing resource structure. Omitted fields above are an audit inventory, not a claim that every numeric field is impossible.','- Inherited optional fields without a finite documented default, union-valued structures without a single independent numeric interpretation, and purely visual animation speeds are not fabricated. Native state-transition speeds are exposed only when the matching animation exists. The fluid turret always requires fuel before attacking, so the engine-forced start-state flag is omitted. Mech armor flight cannot be disabled independently of its collision/drawing boxes and is omitted; other armor flight toggles require space travel. Capsule warmup is excluded because nonzero warmup is invalid for capsule actions.','- Artillery and discharge remotes contain identifiers but no independent attack parameters. Their behavior is configured on artillery entities/gun and discharge equipment. Food use-on-self capsules are included for combat healing/buff research; spoilage and agricultural production are outside scope.','- Player character melee stats, enemy units/spawners/worms, hostile acid/demolisher effects not reachable from player combat resources, transport movement engines, crafting and general power generation equipment are outside this player-weapon/defense catalog. Shared player effects may still have other consumers; inspect the complete native reference graph before experiments.','- Shared resources are explicitly labeled. No per-weapon cloning of ammunition or projectiles is performed; modifying a shared ammo/beam/fire/sticker affects all its consumers, potentially including enemies or environmental fires. Weapon-local coefficients and embedded actions stay local.','- Startup settings apply to existing and newly placed entities. Inventory shrinkage can lose items; extreme ranges, radii, repeat counts and branching can exhaust memory/CPU. The million-tile spatial input guard is not a safety guarantee.','- The original gun-turret field-specific exclusions and conversions are retained. Default settings never materialize optional fields or normalize native data.','']
 (ROOT/'PARAMETERS.md').write_text('\n'.join(doc))
 print(f'{len(entries)} additional settings; {len(groups)} records; {sum(not e["expansion"] and not e.get("feature") for e in entries)+51} base / {len(entries)+51} Space Age total')

if __name__=='__main__':main()
