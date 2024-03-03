search_keywords_urls = {
    'wrd':'https://en.wiktionary.org/wiki/',
    'wik':'https://en.m.wikipedia.org/wiki/',
    'yt':'https://www.youtube.com/results?search_query=',
    'map':'https://www.google.com/maps/search/',
    'amz':'https://www.amazon.ca/s?k=',
    'lyr':'https://genius.com/search?q=',
    'ef':'https://www.wordreference.com/enfr/',
    'fe':'https://www.wordreference.com/fren/',
    'eg':'https://www.wordreference.com/engr/',
    'ge':'https://www.wordreference.com/gren/',
    'εα':'https://www.wordreference.com/gren/',
    'goog':'https://www.google.com/search?q=',
    'red': 'https://www.reddit.com/search/?q=',
    'gh':'https://github.com/search?q=',
    'lt':'https://lyricstranslate.com/en/site-search?query=',
}

def custom_search(input_text): # move this to its own file. move the search_keywords_urls with it, and then import it here
    first_space_index = input_text.find(' ')
    where_to_search = input_text[:first_space_index]
    what_to_search = input_text[first_space_index+1:]

    if where_to_search not in search_keywords_urls:
        where_to_search = 'goog'
        what_to_search = input_text

    space_separators = {
        'yt': '+',
        'map':'%20',
        'amz':'+',
        'ef':'%20',
        'fe':'%20',
        'eg':'%20',
        'ge':'%20',
        'εα':'%20',
        'goog':'+',
        'red':'+',
        'gh':'+',
        'lt':'+',
    }
    space_separator = space_separators.get(where_to_search)
    if not space_separator: space_separator = '_'
    formatted_search_term = what_to_search.replace(' ', space_separator)
    # check which actually need a space separator. I think some can just have a space in the URL be automatically converted to %20

    if where_to_search == 'red':
        formatted_search_term = formatted_search_term + '&include_over_18=1'

    url = search_keywords_urls.get(where_to_search) + formatted_search_term

    return url


def utilize_command(input_text, OS='Windows'):
    if input_text[:input_text.find(' ')] in search_keywords_urls:
        # perform custom search
        url = custom_search(input_text)
        import webbrowser
        webbrowser.open(url)
    elif input_text == 'cgpt':
        import webbrowser
        webbrowser.open('https://chat.openai.com/') # can't use custom search to feed it a prompt
    elif input_text.startswith('cgpt '):
        import webbrowser
        webbrowser.open('https://chat.openai.com/') # can't use custom search to feed it a prompt
        # wait for page to load
        import time
        time.sleep(2)
        import keyboard
        keyboard.write(input_text[5:])
        keyboard.press_and_release('enter')
    elif input_text == 'term':
        # open terminal
        import subprocess
        if OS == 'Windows':
            subprocess.Popen(['powershell.exe'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        elif OS == 'Linux':
            subprocess.Popen('gnome-terminal')
    elif input_text == 'py':
        # open terminal with python
        import subprocess
        if OS == 'Windows':
            subprocess.Popen(['powershell.exe', '-Command', 'python'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        elif OS == 'Linux':
            subprocess.Popen('python3') # needs to be checked when called from controller
    elif input_text.startswith('py '):
        # run one line of Python code (the input) in a new REPL, and have it import a few libraries before running that line (just NumPy?)
        pass
    elif input_text.startswith('gpt4 '):
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
    elif input_text.startswith('gpt3.5 '):
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
    elif input_text == 'txtr':
        import text_replacement
        text_replacement.enable_text_replacement()
    elif input_text == 'txtroff': # doesn't work yet, currently need to hit esc to stop it
        import text_replacement
        text_replacement.disable_text_replacement()
    else:
        print("Command not recognized")
        return
if __name__ == "__main__":
    input_text = input("Enter command: ")
    utilize_command(input_text)


# ideas for actions:
if 0:
    """implemented"""
    # custom search
    # open terminal with PowerShell
    # open terminal with Python
    # GPT 4, 3.5 API access (add way more functionality, like conversations instead of just one answer)
    # text replacement like on phone (add better way to disable it)
    # Linux support. Note currently just Ubuntu, and it also needs more work (controller among other things)
    """unimplemented"""
    # something to quickly paste certain text (current date, personal Zoom room link, etc.)
    # clipboard history (not existent on Linux). Maybe for more than just text
    # run one line of Python code (the input), and have it import a few libraries before running that line (just NumPy?)
    # autoclicker
    # text prediction in any text box
    # open a specific program/file/folder/website
    # computer search?
    # toggle computer settings?
    # force close currently open program?
    # open a GUI to enter more complex commands/give an overview of enabled features/history of commands used?
    # set up work environment (open specific programs, open specific files, open specific websites, move things to certain parts of the screen, etc.)
    # set custom hotkey function triggers (basically make Excel macros for the whole computer)
    # other pyautogui things
    # always on top windows/other inspiration from WindowsPowerToys?

    # maybe bring in Pythonista files and develop them here too. Easier than on the phone