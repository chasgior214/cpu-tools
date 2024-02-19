import time
import pyautogui
import keyboard

def wait_for_keypress(key, action_to_perform=None):
    
    print(f"Waiting for '{key}' key press...")
    keyboard.wait(key)
    
    print(f"'{key}' key pressed! Performing action...")
    if action_to_perform:
        action_to_perform()

def wait_for_keypress_combo(keys, action_to_perform=None):
    
    print(f"Waiting for '{keys}' key press...")
    keyboard.wait(keys)
    
    print(f"'{keys}' key pressed! Performing action...")
    if action_to_perform:
        action_to_perform()


# call action_to_perform when a combination of keys is pressed
if __name__ == "__main__":
    # wait_for_keypress('left ctrl')
    wait_for_keypress_combo('numlock+ctrl')
    # while True:
    #     print(keyboard.read_event())


# ideas for hotkeys:
"""
ctrl+numlock
ctrl+alt+numlock
ctrlleft+ctrlright # keyboard module calls it left ctrl and right ctrl
    would need to use keyboard.read_event() and make my own function to check if the combo is pressed

"""
# ideas for actions:
if 0:
    # custom search
    import custom_search
    # open terminal with python
    import subprocess
    subprocess.Popen(['powershell.exe'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    # text replacement like on phone
    import text_replacement
    # GPT 4 API access