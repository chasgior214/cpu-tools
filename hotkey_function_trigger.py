import time
import pyautogui
import keyboard

def wait_for_keypress(key):
    
    print(f"Waiting for '{key}' key press...")
    keyboard.wait(key)
    
    print(f"'{key}' key pressed! Performing action...")
    
    pyautogui.hotkey(['win','d'])
    time.sleep(0.2)
    pyautogui.hotkey(['win','6'])

if __name__ == "__main__":
    wait_for_keypress('`')