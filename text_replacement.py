text_replacement_dict = {
    'abt':'about',
    'alr':'already',
    'altho':'although',
    'amt':'amount',
    'anw':'anyway',
    'appt':'appointment',
    'atm':'at the moment',
    'b':'be',
    'bc':'because',
    'bday':'birthday',
    'brb':'be right back',
    'btw':'by the way',
    'bw':'between',
    'c':'see',
    'cad':'CAD',
    'def':'definitely',
    'dont':'don\'t',
    'dw':'don\'t worry',
    'dwbi':'don\'t worry about it',
    'esp':'especially',
    'fri':'Friday',
    'fs':'for sure',
    'fwd':'forward',
    'gl':'good luck',
    'gn':'good night',
    'goin':'going',
    'gonna':'going to',
    'hbu':'how about you',
    'idc':'I don\'t care',
    'idk':'I don\'t know',
    'idt':'I don\'t think',
    'idts':'I don\'t think so',
    'ig':'I guess',
    'ik':'I know',
    'im':'I\'m',
    'incl':'including',
    'ith':'I think',
    'ive':'I\'ve',
    'lmk':'let me know',
    'lp':'Little Prince',
    'lyk':'let you know',
    'mon':'Monday',
    'msg':'message',
    'n':'and',
    'nbd':'no big deal',
    'np':'no problem',
    'nth':'nothing',
    'nvm':'nevermind',
    'nw':'no worries',
    'ofc':'of course',
    'omw':'on my way',
    'perf':'perfect',
    'pls':'please',
    'pp':'Petit Prince',
    'ppl':'people',
    'pt':'point',
    'r':'are',
    'rly':'really',
    'rlly':'really',
    'rn':'right now',
    'rnt':'aren\'t',
    'rr':'Red Rising',
    'seriously':'',
    'sry':'sorry',
    'sth':'something',
    'tbf':'to be fair',
    'td':'today',
    'tgt':'together',
    'tgther':'together',
    'tho':'though',
    'thru':'through',
    'thurs':'Thursday',
    'tmrw':'tomorrow',
    'tn':'tonight',
    'tru':'true',
    'tty':'talk to you',
    'ttyl':'talk to you later',
    'tues':'Tuesday',
    'ty':'thank you',
    'u':'you',
    'ur':'you\'re',
    'uv':'you\'ve',
    'w':'with',
    'wbu':'what about you',
    'wdym':'what do you mean',
    'wdyt':'what do you think',
    'whatre':'what\'re',
    'whats':'what\'s',
    'wo':'without',
    'wtv':'whatever',
    'wyd':'what\'re you doing',
    'y':'why',
    'yk':'you know',
    'yw':'you\'re welcome',

    'εγκ':'Ἐγχειρίδιον',
    'επικ':'Ἐπίκτητος',
    'γγ':'γιαγιά',
    'γκπ':'γιαγιά and παππού',
    'πκγ':'παππού and γιαγιά',
    'ππ':'παππού',
    'θκθ':'θείος and θεία',
}

# check if the most recently typed word is in the text_replacement_dict

# log the past 10 keys pressed
# if the most recent key pressed is a space, then check if the word before the space is in the text_replacement_dict
# if it is, then replace it with the value in the text_replacement_dict

import keyboard
import time

last_20_keys = [' ' for i in range(20)]

def on_key_event(e):
    global last_20_keys
    if e.name == 'space':
        key_combo = ''.join(last_20_keys).split(' ')[-1]
        if key_combo in text_replacement_dict:
            for _ in range(len(key_combo)+1):
                keyboard.press_and_release('backspace')
            keyboard.write(text_replacement_dict[key_combo])
            keyboard.press_and_release('space')
            time.sleep(0.1)
        last_20_keys = last_20_keys[1:] + [' ']
    else:
        last_20_keys = last_20_keys[1:] + [e.name]
    return

def enable_text_replacement():
    keyboard.on_press(on_key_event)
    keyboard.wait('esc') # this will block the program until the escape key is pressed
    keyboard.unhook_all() # this will stop the program from listening to any more key events
    return

def disable_text_replacement(): # going to need to call this a different way. would rather be able to keep the program running if I hit escape (or any key, I only want it to end if I give it a command to)
    keyboard.unhook_all()
    return

keyboard.on_press(on_key_event)
keyboard.wait('esc') # this will block the program until the escape key is pressed
keyboard.unhook_all() # this will stop the program from listening to any more key events
