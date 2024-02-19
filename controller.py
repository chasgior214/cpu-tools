import time
import pyautogui
import keyboard
import tkinter as tk

import hotkey_function_trigger as hft
import custom_search

def command_mode():
    hft.wait_for_keypress_combo('numlock+ctrl')
    # open an input box to enter a command
    root = tk.Tk()
    root.title("Enter command")
    root.geometry("300x100")
    entry = tk.Entry(root)
    entry.pack()
    entry.focus_set()

    def on_submit(event=None):
        command = entry.get()
        root.quit()
        root.destroy()
        custom_search.run_search(command)
        
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()
    root.bind('<Return>', on_submit)
    # bring the window to the front
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-disabled', False)
    time.sleep(0.1)
    pyautogui.hotkey(['shift', 'alt','tab'])
    time.sleep(0.1)
    root.mainloop()


def to_desktop():
    pyautogui.hotkey(['win','d'])


if __name__ == "__main__":
    command_mode()