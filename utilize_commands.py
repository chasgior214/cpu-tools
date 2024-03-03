from web_custom_search import search_keywords_urls, custom_search

def utilize_command(input_text, OS='Windows'):
    if input_text[:input_text.find(' ')] in search_keywords_urls: # OS status: W good, L good
        # perform custom search
        url = custom_search(input_text)
        import webbrowser
        webbrowser.open(url)
    elif input_text == 'cgpt': # OS status: W good, L good
        import webbrowser
        webbrowser.open('https://chat.openai.com/') # can't use custom search to feed it a prompt
    elif input_text.startswith('cgpt '): # OS status: W good, L check (don't think Keyboard will work)
        import webbrowser
        webbrowser.open('https://chat.openai.com/') # can't use custom search to feed it a prompt
        # wait for page to load
        import time
        time.sleep(2)
        import keyboard
        keyboard.write(input_text[5:])
        keyboard.press_and_release('enter')
    elif input_text == 'term': # OS status: W good, L good
        # open terminal
        import subprocess
        if OS == 'Windows':
            subprocess.Popen(['powershell.exe'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        elif OS == 'Linux':
            subprocess.Popen('gnome-terminal')
    elif input_text == 'py': # OS status: W good, L needs to be checked when called from controller
        # open terminal with python
        import subprocess
        if OS == 'Windows':
            subprocess.Popen(['powershell.exe', '-Command', 'python'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        elif OS == 'Linux':
            subprocess.Popen('python3')
    elif input_text.startswith('py '): # OS status: not yet implemented in either
        # run one line of Python code (the input) in a new REPL, and have it import a few libraries before running that line (just NumPy?)
        pass
    elif input_text.startswith('gpt4 '): # OS status: W good, L not implemented
        # GPT 4 API access
        import OpenAI_API
        response = OpenAI_API.open_chat(input_text[5:], model='gpt4')
        # display response in a window
        import tkinter as tk
        root = tk.Tk()
        root.title("GPT-4 response")
        root.geometry("800x300")
        # split response into multiple labels if it's too long
        response = str(response)
        response = '\n'.join([response[i:i+100] for i in range(0, len(response), 50)])
        label = tk.Label(root, text=response)
        label.pack()
        root.mainloop()
    elif input_text.startswith('gpt3.5 '): # OS status: W good, L not implemented
        # GPT 3.5 API access
        import OpenAI_API
        response = OpenAI_API.open_chat(input_text[7:], model='gpt3.5')
        # display response in a window
        import tkinter as tk
        root = tk.Tk()
        root.title("GPT-3.5 response")
        root.geometry("800x300")
        # split response into multiple labels if it's too long
        response = str(response)
        response = '\n'.join([response[i:i+100] for i in range(0, len(response), 50)])
        label = tk.Label(root, text=response)
        label.pack()
        root.mainloop()
    elif input_text == 'txtr': # OS status: W good, L not implemented
        import text_replacement
        text_replacement.enable_text_replacement()
    elif input_text == 'txtroff': # OS status: doesn't work yet in either, currently need to hit esc to stop it
        # also nice to have this so that I can run new commands with text_replacement still enabled
        import text_replacement
        text_replacement.disable_text_replacement()
    elif input_text.startswith('@'): # OS status: W good except Zoomroom, L not implemented
        import get_text_snippets
        snippet = get_text_snippets.commands_for_snippets[input_text]()
        import time
        time.sleep(0.2)
        import keyboard
        keyboard.write(snippet)
    else:
        print("Command not recognized")
        return
if __name__ == "__main__":
    input_text = input("Enter command: ")
    utilize_command(input_text)


# ideas for actions:
if 0:
    """implemented"""
    # custom web search
        # can add the following, but need to be done by opening new tab and using Keyboard or another module instead of just via url:
            # 'history': '@history',
            # 'tabs': '@tabs',
            # 'favs': '@favorites', #'@bookmarks' in Chrome
    # open terminal
    # open terminal with Python
    # GPT 4, 3.5 API access (add way more functionality, like conversations instead of just one answer, ability to highlight and copy text, etc.)
    # text replacement like on phone (add better way to disable it)
    # quickly paste certain text (current date, personal Zoom room link, etc.)
    # Linux support. Note currently just Ubuntu, and it also needs more work (controller among other things)

    """unimplemented"""
    # run one line of Python code (the input), and have it import a few libraries before running that line (just NumPy?) - good as a dedicated calculator
    # text prediction in any text box

    # open a GUI to enter more complex commands/provide information on status of what the tool(s) are doing:
        # clipboard history (not existent on Linux). Maybe for more than just text
        # autoclicker
        # readout of cursor position
        # display overview of enabled features
        # display history of commands used
    
    # open a specific program/file/folder/website
    # computer search?
    # toggle computer settings
    # force close currently open program
    # set up work environment(s) (open specific programs, open specific files, open specific websites, move things to certain parts of the screen, etc.)
    # set custom hotkey function triggers (basically make Excel macros for the whole computer)
    # other pyautogui things
    # always on top windows/other inspiration from WindowsPowerToys?

    # maybe bring in Pythonista files and develop them here too. Easier than on the phone