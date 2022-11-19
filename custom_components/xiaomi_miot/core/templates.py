CUSTOM_TEMPLATES = {
    # https://iot.mi.com/new/doc/embedded-development/ble/object-definition#%E7%89%99%E5%88%B7%E4%BA%8B%E4%BB%B6
    'ble_toothbrush_events': "{%- set dat = props.get('event.16') | default('{}',true) | from_json %}"
                             "{%- set tim = dat.timestamp | default(0,true) | timestamp_local %}"
                             "{%- set val = dat.get('value',[]).0 | default('0000') %}"
                             "{%- set typ = val[0:2] | int(0,16) %}"
                             "{%- set num = val[2:4] | int(0,16) %}"
                             "{{ {"
                             "'event': 'start',"
                             "'counter': num,"
                             "'timestamp': tim,"
                             "} if typ == 0 else {"
                             "'event': 'finish',"
                             "'score': num,"
                             "'timestamp': tim,"
                             "} }}",
    # https://iot.mi.com/new/doc/embedded-development/ble/object-definition#%E9%94%81%E4%BA%8B%E4%BB%B6
    'ble_lock_events': "{%- set mark_data = props.get('event.6') | default('{}',true) | from_json %}"
                       "{%- set mark = mark_data.get('value',[]).0 | default('') %}"
                       "{%- set door_data = props.get('event.7') | default('{}',true) | from_json %}"
                       "{%- set door = (door_data.get('value',[]).0 | default(''))[:2] | int(-1,16) %}"
                       "{%- set fang_data = props.get('event.8') | default('{}',true) | from_json %}"
                       "{%- set fang = (fang_data.get('value',[]).0 | default(''))[:2] | int(-1,16) %}"
                       "{%- set lock_data = props.get('event.11') | default('{}',true) | from_json %}"
                       "{%- set lock = lock_data.get('value',[]).0 | default('') %}"
                       "{%- set lock_action = lock[:2] | int(-1,16) % 16 %}"
                       "{%- set lock_method = lock[:2] | int(-1,16) // 16 %}"
                       "{%- set lock_key = lock[2:10] %}"
                       "{%- set lock_fault = lock_key if lock_key[:4] == 'c0de' else None %}"
                       "{%- set key_id = (0).from_bytes((0).to_bytes(0,'little').fromhex(lock_key),'little') %}"
                       "{%- set key_types = {'00000000':'admin','ffffffff':'unknown','deadbeef':'invalid'} %}"
                       "{%- set key_results = ['success','fail','timeout','blurry','less','dry','wet'] %}"
                       "{%- set door_states = ['open','close','close_timeout','knock','breaking','stuck'] %}"
                       "{%- set lock_actions = ['outside_unlock','lock','anti_lock_on','anti_lock_off',"
                       "'inside_unlock','lock_inside','child_lock_on','child_lock_off'] %}"
                       "{%- set lock_methods = ['bluetooth','password','biological','key','turntable','nfc',"
                       "'one-time password','two-step verification','coercion','homekit','manual','automatic'] %}"
                       "{{ {"
                       "'fingerprint_id': key_types[mark[:8]] | default(mark[:8]),"
                       "'fingerprint_result': key_results[mark[8:10] | int(-1,16)] | default('unknown'),"
                       "'door_state': door_states[door] | default('unknown'),"
                       "'armed_state': true if fang > 0 else false,"
                       "'lock_action': lock_actions[lock_action] | default('unknown'),"
                       "'lock_method': lock_methods[lock_method] | default('unknown'),"
                       "'lock_key': key_types[lock_key] | default(lock_key),"
                       "'lock_key_id': key_id,"
                       "'lock_fault': lock_fault | default('none',true),"
                       "'lock_data': lock,"
                       "'timestamp': lock_data.timestamp | default(0,true) | timestamp_local,"
                       "} }}",
    # https://iot.mi.com/new/doc/embedded-development/ble/object-definition#%E7%83%9F%E9%9B%BE%E5%B1%9E%E6%80%A7
    'ble_sensor_smoke': "{%- set val = props.get('prop.4117','00') | int(0,16) %}"
                        "{{ {"
                        "'smoke_status': val == 1,"
                        "} }}",
    'chuangmi_plug_v3_power_cost': "{%- set val = (result.0 | default({})).get('value',{}) %}"
                                   "{%- set day = now().day %}"
                                   "{{ {"
                                   "'today': val.pc | default(0),"
                                   "'today_duration': val.pc_time | default(0),"
                                   "'month': result[:day] | sum(attribute='value.pc'),"
                                   "'month_duration': result[:day] | sum(attribute='value.pc_time'),"
                                   "} }}",
    'lock_event_7_template':  "{%- set val = (result.0 | default({})).get('value','[-1]') %}"
                              "{%- set val = (val | from_json).0 | string %}"
                              "{%- set evt = val[:2] | int(-1,16) %}"
                              "{%- set els = ['open','close','close_timeout',"
                              "'knock','breaking','stuck','unknown'] %}"
                              "{{ {"
                              "'door_event': evt,"
                              "'door_state': els[evt] | default('unknown'),"
                              "} }}",
    'lock_event_11_template': "{%- set val = (result.0 | default({})).get('value','[-1]') %}"
                              "{%- set val = (val | from_json).0 | string %}"
                              "{%- set evt = val[:2] | int(-1,16) % 16 %}"
                              "{%- set how = val[:2] | int(-1,16) // 16 %}"
                              "{%- set key = (0).from_bytes((0).to_bytes(0,'little')"
                              ".fromhex(val[2:10]), 'little') %}"
                              "{%- set els = ['outside_unlock','lock','anti_lock_on','anti_lock_off',"
                              "'inside_unlock','lock_inside','child_lock_on','child_lock_off','unknown'] %}"
                              "{%- set mls = ['bluetooth','password','biological','key','turntable',"
                              "'nfc','one-time password','two-step verification','coercion','homekit',"
                              "'manual','automatic','unknown'] %}"
                              "{{ {"
                              "'lock_event': evt,"
                              "'lock_state': els[evt] | default('unknown'),"
                              "'method_id': how,"
                              "'method': mls[how] | default('unknown'),"
                              "'key_id': key,"
                              "} }}",
    'lumi_acpartner_electric_power': "{%- set val = props.get('prop.load_power') or props.get('prop.ac_power',0) %}"
                                     "{{ {"
                                     "'electric_power': val | default(0,true) | round(2),"
                                     "} }}",
    'lumi_acpartner_miio_status': "{%- set model = results[0] | default('') %}"
                                  "{%- set state = results[1] | default('') %}"
                                  "{{ {"
                                  "'power': state[2:3] | int(0) == 1,"
                                  "'mode': [3,1,0,2,4][state[3:4] | int(2)],"
                                  "'fan_level': [1,2,3,0][state[4:5] | int(3)],"
                                  "'vertical_swing': state[5:6] in ['0','C'],"
                                  "'target_temperature': state[6:8] | int(0,16),"
                                  "'load_power': results[2] | default(0) | float | round(2),"
                                  "} }}",
    'micloud_statistics_power_cost': "{%- set dat = namespace(today=0,month=0) %}"
                                     "{%- set tim = now() %}"
                                     "{%- set stm = tim - timedelta(minutes=tim.minute,seconds=tim.second) %}"
                                     "{%- set tod = stm - timedelta(hours=tim.hour) %}"
                                     "{%- set stm = tod - timedelta(days=tim.day-1) %}"
                                     "{%- set tod = tod | as_timestamp | int(0) %}"
                                     "{%- set stm = stm | as_timestamp | int(0) %}"
                                     "{%- for d in (result or []) %}"
                                     "{%-   set t = d.time | default(0) | int(0) %}"
                                     "{%-   if t >= stm %}"
                                     "{%-     set v = (d.value | default('[]') | string | from_json) or [] %}"
                                     "{%-     set n = v[0] | default(0) %}"
                                     "{%-     if t >= tod %}"
                                     "{%-       set dat.today = n %}"
                                     "{%-     endif %}"
                                     "{%-     set dat.month = dat.month + n %}"
                                     "{%-   endif %}"
                                     "{%- endfor %}"
                                     "{{ {"
                                     "'power_cost_today': dat.today | round(3),"
                                     "'power_cost_month': dat.month | round(3),"
                                     "} }}",
    'midr_rv_mirror_cloud_props': "{%- set sta = props.get('prop.Status',0) | int %}"
                                  "{%- set pos = props.get('prop.Position','{}') | from_json %}"
                                  "{%- set tim = pos.get('up_time_stamp',0) | int %}"
                                  "{{ {"
                                  "'prop.status': sta,"
                                  "'prop.position': pos,"
                                  "'prop.update_at': (tim / 1000) | timestamp_local,"
                                  "} }}",
    'mxiang_cateye_cloud_props': "{{ {"
                                 "'battery_level':     props.get('prop.battery_level','0')     | from_json | int,"
                                 "'is_can_open_video': props.get('prop.is_can_open_video','0') | from_json | int,"
                                 "} }}",
    'mxiang_cateye_human_visit_details': "{%- set val = (result.0 | default({})).get('value','{}') %}"
                                         "{%- set val = val | from_json %}"
                                         "{{ {"
                                         "'motion_video_time': val.get('visitTime',0) | timestamp_local,"
                                         "'motion_video_type': val.get('action'),"
                                         "'motion_video_latest': val,"
                                         "'_entity_attrs': True,"
                                         "} }}",
    'yeelink_bhf_light_v2_fan_levels': "{%- set val = ('00000' ~ value)[-5:] %}"
                                       "{%- set mds = {"
                                       "'drying_cloth': val[0],"
                                       "'coolwind': val[1],"
                                       "'drying': val[2],"
                                       "'venting': val[3],"
                                       "'warmwind': val[4],"
                                       "} %}"
                                       "{{ [1,2,3][mds[props.bh_mode] | default(0) | int(0)] | default(3) }}",
    'yeelink_bhf_light_v5_fan_levels': "{%- set val = ('000' ~ value)[-3:] %}"
                                       "{%- set mds = {"
                                       "'warmwind': val[0],"
                                       "'coolwind': val[1],"
                                       "'venting': val[2],"
                                       "} %}"
                                       "{{ [1,1,3,3][mds[props.bh_mode] | default(0) | int(0)] | default(1) }}",
    'yeelink_bhf_light_v5_miio_props': "{%- set val = ('000' ~ props.fan_speed_idx)[-3:] %}"
                                       "{{ {"
                                       "'warmwind_gear': val[0],"
                                       "'coolwind_gear': val[1],"
                                       "'venting_gear': val[2],"
                                       "} }}",
    'zimi_powerstrip_v2_power_cost': "{%- set val = (result.0 | default({})).get('value','[0]') %}"
                                     "{%- set day = now().day %}"
                                     "{%- set vls = (val | from_json)[0-day:] %}"
                                     "{%- set dat = namespace(today=0,month=0) %}"
                                     "{%- for v in vls %}"
                                     "{%-   set v = (v | string).split(',') %}"
                                     "{%-   if v[0] | default(0) | int(0) > 86400 %}"
                                     "{%-     set dat.today = v[1] | default(0) | round(3) %}"
                                     "{%-     set dat.month = dat.month + dat.today %}"
                                     "{%-   endif %}"
                                     "{%- endfor %}"
                                     "{{ {"
                                     "'today': dat.today,"
                                     "'month': dat.month | round(3),"
                                     "} }}",
}
