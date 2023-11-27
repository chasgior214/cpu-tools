import time
import pyautogui
import keyboard

def wait_for_keypress(key):
    
    print(f"Waiting for '{key}' key press...")
    keyboard.wait(key)
    
    print(f"'{key}' key pressed! Performing action...")
    action_to_perform()

def action_to_perform():
    pyautogui.hotkey(['win','d'])
    time.sleep(0.4)
    pyautogui.hotkey(['win','e'])

# make another script that performs an action when a combination of keys is pressed
def wait_for_keypress_combo(keys):
    
    print(f"Waiting for '{keys}' key press...")
    keyboard.wait(keys)
    
    print(f"'{keys}' key pressed! Performing action...")
    action_to_perform()

# call action_to_perform when a combination of keys is pressed
if __name__ == "__main__":
    # wait_for_keypress('`')
    wait_for_keypress_combo('ctrl+numlock')

# ideas for hotkeys:
"""
ctrl+numlock
ctrl+alt+numlock

"""
# ideas for actions:
"""
my custom searcher → import from what's currently on phone, build from there
open terminal with python
"""