"""
Friday Night Funkin' Automation Bot By Aweb.
V.0.1.0

Welcome to the source code of FNF Automation Bot.
I'm Aweb, and I'll guide you to this source code
and make your job of modifying easier for you.

As an open_source software, you have full rights
to modify this code and make your own versions.
And as the developer, I support any person who
makes their own versions. We don't force you to
credit us, but it would be cool if you do.
You can submit your version in our discord server,
and we will promote it. We have a full category of
channels for mods created by the community. To
make sure our community is a part of the software.
We do rate and give feedback to every version
to level up the fun and the community.

Alright let's get started.
This software is made in python version 3.12
and uses tkinter library for UI,
pynput keyboard for key press simulation,
multiprocessing for running processes simultaneously,
pyautogui for color and position checking,
and configparser for saving data in a .ini file.
Here are documentations for each library:
tkinter: https://docs.python.org/3.12/library/tkinter.html
pynput:
multiprocessing:
pyautogui:
configparser:

That's all I'm ganna say for now, I did my best
in commenting this code to make sure you get
everything. You can create a support ticket
or get help for the community in our discord
server. The rest is now all up to you now,
GoOd LuCk!!
"""

# Modules and Packages:
import pyautogui
from pynput.keyboard import Controller
import tkinter as tk
from tkinter import ttk, messagebox
from configparser import ConfigParser
import multiprocessing

keyboard_controller = Controller()

# Main function for key pressing.
def press_key(position: tuple[int, int],
              color: tuple[float, float, float],
              key: str,
              ):
    while True:
        color_pos = pyautogui.pixel(position[0], position[1])
        if color_pos != color:
            continue
        keyboard_controller.press(key)
        while True:
            release_color_pos = pyautogui.pixel(position[0], position[1]+100)
            if release_color_pos == color:
                if pyautogui.pixel(position[0] + 30, position[1] + 100) != color:
                    continue
            keyboard_controller.release(key)
            break

# Function that help encoding entry variables to tuples.
def separate(value: str, number: bool = True):
    values = []
    times = 0
    for char in value:
        if char == ' ':
            continue

        if len(values) != times + 1:
            values.append(char)
            continue

        if char == ',':
            if number:
                values[times] = int(values[times])
            times += 1
            continue

        values[times] += char

    values[-1] = int(values[-1])

    return values


# Main class of the App:
class App:

    def __init__(self):
        # Window Setting
        self.root = tk.Tk()
        self.root.geometry('450x510')
        self.root.title('FNF Automation Bot')
        self.root.resizable(False, False)
        self.root.wm_iconbitmap('assets/icon.ico')

        # Variables
        self.on = False
        self.settings = {
            'left': 's',
            'down': 'd',
            'up': 'j',
            'right': 'k',
            'left_pos': '785, 252',
            'down_pos': '896, 252',
            'up_pos': '1012, 252',
            'right_pos': '1133, 252',
            'left_color': '194, 75, 153',
            'down_color': '0, 255, 255',
            'up_color': '18, 250, 5',
            'right_color': '249, 57, 63',
        }

        self.theme = {
            'bg': '#2F3133',
            'fg': '#ffffff',
            'button_bg': '#555555',
            'button_fg': '#ffffff',
            'active_button_bg': '#444444',
            'active_button_fg': '#ffffff',
        }
        self.savefile = 'save.ini'
        self.save = ConfigParser()
        self.save.read(self.savefile)

        self.settings['left'] = self.save.get('Controls', 'left')
        self.settings['down'] = self.save.get('Controls', 'down')
        self.settings['up'] = self.save.get('Controls', 'up')
        self.settings['right'] = self.save.get('Controls', 'right')
        self.settings['left_pos'] = self.save.get('Positions', 'left')
        self.settings['down_pos'] = self.save.get('Positions', 'down')
        self.settings['up_pos'] = self.save.get('Positions', 'up')
        self.settings['right_pos'] = self.save.get('Positions', 'right')
        self.settings['left_color'] = self.save.get('Colors', 'left')
        self.settings['down_color'] = self.save.get('Colors', 'down')
        self.settings['up_color'] = self.save.get('Colors', 'up')
        self.settings['right_color'] = self.save.get('Colors', 'right')

        # Window Elements
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[15, 4], font=('Arial', 16))

        self.main_frame = tk.LabelFrame(self.root, padx=5, pady=5)
        self.main_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.notebook = ttk.Notebook(self.main_frame, width=420)
        self.notebook.grid(row=0, column=0, sticky='nsew')

        self.main_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.main_tab, text='Main')

        self.controls_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.controls_tab, text='Controls')

        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text='Settings')

        self.credits_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.credits_tab, text='Credits')

        # Main Tab
        self.home_frame = tk.Frame(self.main_tab, padx=10, pady=10)
        self.home_frame.grid(row=0, column=0)

        self.main_title = tk.Label(self.home_frame, text='Friday Night Funkin\'\n'
                                                         'Automation Bot', font=('', 24), padx=55, pady=0)
        self.main_title.grid(row=0, column=0, columnspan=3)

        self.main_description = tk.Label(self.home_frame, text='The most accurate, easy to use, and the first and\n'
                                                               'only bot that can hold notes!\n'
                                                               '\n'
                                                               'A free and open_sourced bot that can automate note\n'
                                                               'presses in All FNF games.\n'
                                                               '\n'
                                                               'It can automate note presses accurately. Simply bind\n'
                                                               'your controls in the Controls tab, and the positions\n'
                                                               'of the notes where they should be pressed, it\'s \n'
                                                               'recommend to bind it to the center of the note and\n'
                                                               'then change your visual offset (+60 for fast songs,\n'
                                                               'you might wanna try different offsets for the best results)\n'
                                                               'in the settings. Color binds are set to default colors,\n'
                                                               'if you have custom colors, you might need to change that.\n'
                                                               '\n'
                                                               'For more details read the README.md file',
                                         font=('', 12), padx=0)
        self.main_description.grid(row=1, column=0, columnspan=3)

        # Controls Tab
        self.controls_frame = tk.Frame(self.controls_tab, padx=10, pady=10)
        self.controls_frame.grid(row=0, column=0)

        self.controls_title = tk.Label(self.controls_frame, text='Controls', font=('', 24), padx=130)
        self.controls_title.grid(row=0, column=0, columnspan=3, sticky='w')

        self.controls_label = tk.Label(self.controls_frame, text='Key binds:', font=('', 16), pady=8)
        self.controls_label.grid(row=1, column=0, columnspan=3, sticky='w')

        self.control_rows = []
        self.create_control_row(self.controls_frame, "Left", 'left', 2)
        self.create_control_row(self.controls_frame, "Down", 'down', 3)
        self.create_control_row(self.controls_frame, "Up", 'up', 4)
        self.create_control_row(self.controls_frame, "Right", 'right', 5)

        # Settings Tab
        self.settings_frame = tk.Frame(self.settings_tab, padx=10, pady=10)
        self.settings_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.settings_title = tk.Label(self.settings_frame, text='Settings', font=('', 24), padx=132)
        self.settings_title.grid(row=0, column=0, columnspan=3, sticky='w')

        self.controls_label = tk.Label(self.settings_frame, text='Detection Coordinate:', font=('', 16), pady=8)
        self.controls_label.grid(row=1, column=0, columnspan=3, sticky='w')

        self.settings_rows = []
        self.create_settings_row(self.settings_frame, 'Left:', 'left_pos', 2, False)
        self.create_settings_row(self.settings_frame, 'Down:', 'down_pos', 3, False)
        self.create_settings_row(self.settings_frame, 'Up:', 'up_pos', 4, False)
        self.create_settings_row(self.settings_frame, 'Right:', 'right_pos', 5, False)

        self.controls_label = tk.Label(self.settings_frame, text='Color:', font=('', 16), pady=8)
        self.controls_label.grid(row=6, column=0, columnspan=3, sticky='w')

        self.create_settings_row(self.settings_frame, 'Left:', 'left_color', 7, True)
        self.create_settings_row(self.settings_frame, 'Down:', 'down_color', 8, True)
        self.create_settings_row(self.settings_frame, 'Up:', 'up_color', 9, True)
        self.create_settings_row(self.settings_frame, 'Right:', 'right_color', 10, True)

        # Credits Tab
        self.credits_frame = tk.Frame(self.credits_tab, padx=10, pady=10)
        self.credits_frame.grid(row=0, column=0)

        self.credits_title = tk.Label(self.credits_frame, text='Credits', font=('', 24), padx=140, pady=15)
        self.credits_title.grid(row=0, column=0, columnspan=3)

        self.development_title = tk.Label(self.credits_frame, text='Development and Programming', font=('', 16))
        self.development_title.grid(row=1, column=0, columnspan=3)

        self.developer = tk.Label(self.credits_frame, text='Aweb (awebgamedev)', font=('', 12))
        self.developer.grid(row=2, column=0, columnspan=3)

        self.testing_title = tk.Label(self.credits_frame, text='Testing', font=('', 16))
        self.testing_title.grid(row=3, column=0, columnspan=3)

        self.testers = tk.Label(self.credits_frame, text='Aweb (awebgamedev)\n'
                                                         'Another Person', font=('', 12))
        self.testers.grid(row=4, column=0, columnspan=3)

        self.discord_button = self.Button('Join our Discord Server', self.credits_frame, self.theme, font=('', 16),
                                          command=self.discord, pad=(10, 0))
        self.discord_button.grid(row=5, column=0, columnspan=3, pady=5)

        self.support_button = self.Button('Support Us :>', self.credits_frame, self.theme, font=('', 16),
                                          command=self.support, pad=(10, 0))
        self.support_button.grid(row=6, column=0, columnspan=3, pady=5)

        self.support_button = self.Button('Get FNF', self.credits_frame, self.theme, font=('', 16),
                                          command=self.fnf, pad=(10, 0))
        self.support_button.grid(row=7, column=0, columnspan=3, pady=5)

        self.start_button = self.Button('Turn On', self.root, self.theme, font=('', 16), command=self.start)
        self.start_button.place(x=175, y=460)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # Call on_closing function when window gets closed
        self.root.mainloop()

    # Function that gets called when app is closed, used to make sure th app close smoothly.
    def on_closing(self):
        try:
            for process in self.processes:  # Terminate all running processes to insure everything close smoothly
                if process.is_alive():
                    process.terminate()
                    process.join()
        except AttributeError:
            pass

        # Save all Variables
        self.save.set('Controls', 'left', self.settings['left'])
        self.save.set('Controls', 'down', self.settings['down'])
        self.save.set('Controls', 'up', self.settings['up'])
        self.save.set('Controls', 'right', self.settings['right'])
        self.save.set('Positions', 'left', self.settings['left_pos'])
        self.save.set('Positions', 'down', self.settings['down_pos'])
        self.save.set('Positions', 'up', self.settings['up_pos'])
        self.save.set('Positions', 'right', self.settings['right_pos'])
        self.save.set('Colors', 'left', self.settings['left_color'])
        self.save.set('Colors', 'down', self.settings['down_color'])
        self.save.set('Colors', 'up', self.settings['up_color'])
        self.save.set('Colors', 'right', self.settings['right_color'])

        with open(self.savefile, 'w') as f:
            self.save.write(f)

        # Close the app
        self.root.destroy()
        quit()

    # Function that turns the bot on and off.
    def start(self):
        if self.on:
            # Turns off the bot and stops all processes.
            self.start_button.config(text='Turn On')
            for process in self.processes:
                if process.is_alive():
                    process.terminate()
                    process.join()

            self.on = False
            return

        # Turns on the bot
        self.on = True
        self.start_button.config(text='Turn Off')

        for row in self.settings_rows:  # Updates the settings dictionary
            self.settings[row[0]] = row[1].get()

        # Gets all variables needed for the bot
        left_pos = separate(self.settings.get('left_pos'), True)
        down_pos = separate(self.settings.get('down_pos'), True)
        up_pos = separate(self.settings.get('up_pos'), True)
        right_pos = separate(self.settings.get('right_pos'), True)

        left_color = separate(self.settings.get('left_color'), True)
        down_color = separate(self.settings.get('down_color'), True)
        up_color = separate(self.settings.get('up_color'), True)
        right_color = separate(self.settings.get('right_color'), True)

        """
        # Debugging lines
        print(f'left position: {left_pos}')
        print(f'down position: {down_pos}')
        print(f'up position: {up_pos}')
        print(f'right position: {right_pos}')
        print(f'left color: {left_color}')
        print(f'down color: {down_color}')
        print(f'up color: {up_color}')
        print(f'right color: {right_color}')
        """

        # Pass all variables needed and start all processes
        self.processes = [
            multiprocessing.Process(target=press_key, args=((left_pos[0], left_pos[1]), (left_color[0], left_color[1], left_color[2]), self.settings.get('left'))),
            multiprocessing.Process(target=press_key, args=((down_pos[0], down_pos[1]), (down_color[0], down_color[1], down_color[2]), self.settings.get('down'))),
            multiprocessing.Process(target=press_key, args=((up_pos[0], up_pos[1]), (up_color[0], up_color[1], up_color[2]), self.settings.get('up'))),
            multiprocessing.Process(target=press_key, args=((right_pos[0], right_pos[1]), (right_color[0], right_color[1], right_color[2]), self.settings.get('right'))),
        ]

        for process in self.processes:
            process.start()

    # All functions bellow this line are for UI.
    def create_control_row(self, parent, label_text, key, row):
        label = tk.Label(parent, text=label_text, font=('', 12))
        label.grid(row=row, column=0, sticky='w', pady=3)

        key_label = tk.Label(parent, text=self.settings.get(key), font=('', 12))
        key_label.grid(row=row, column=1, sticky='w', padx=125)
        self.control_rows.append([key, key_label])

        if self.save.has_option('Controls', key):
            self.control_rows[-1][1].config(text=self.save.get('Controls', key))

        bind_button = self.Button('Bind', parent, self.theme, ('', 12), lambda: self.bind(key), (20, 0))
        bind_button.grid(row=row, column=2, sticky='e', pady=10)

    def create_settings_row(self, parent, label_text, key, row, color:bool):
        label = tk.Label(parent, text=label_text, font=('', 12))
        label.grid(row=row, column=0, sticky='w', pady=3)

        entry_variable = tk.StringVar()

        entry_variable.set(self.settings.get(key))

        key_entry = tk.Entry(parent, textvariable=entry_variable, font=('', 12), width=11)
        key_entry.grid(row=row, column=1, sticky='w', padx=85)
        self.settings_rows.append([key, entry_variable, key_entry])

        if key[-1] == 's':
            if self.save.has_option('Positions', key[:-4]):
                print(self.save.get('Positions', key[:-4]))
                self.settings_rows[-1][1].set(self.save.get('Positions', key[:-4]))
        else:
            if self.save.has_option('Colors', key[:-6]):
                print(self.save.get('Colors', key[:-6]))
                self.settings_rows[-1][1].set(self.save.get('Colors', key[:-6]))

        bind_button = self.Button('Bind', parent, self.theme, ('', 9), lambda: self.bind_setting(key), (20, 0))
        bind_button.grid(row=row, column=2, sticky='e', pady=0)

    def Button(self,
               text: str,
               frame: tk.Frame | tk.LabelFrame | tk.Tk,
               theme: dict,
               font: tuple[str, int],
               command: any = None,
               pad: tuple[float, float] = (0, 0)):
        """frame, text=text, border=0, background=theme.get('button_bg'), foreground=theme.get('button_fg'),
        activebackground=theme.get('active_button_bg'), activeforeground=theme.get('active_button_fg'),
        font=font, command=command, padx=pad[0], pady=pad[1]"""

        return tk.Button(frame, text=text,
                         font=font, command=command, padx=pad[0], pady=pad[1])


    def bind(self, key: str):
        print(f"Rebinding key: {key}")

        self.bind_window = tk.Toplevel()
        self.bind_window.title("Key Bind")
        self.bind_window.geometry("200x100+960+540")
        self.bind_window.focus_set()

        label = tk.Label(self.bind_window, text="Press any key to rebind.\nClose the window to cancel.")
        label.pack(expand=True)

        self.bind_window.bind('<KeyPress>', lambda event: self.on_key_press(event, key))

        self.bind_window.grab_set()
        self.bind_window.wait_window()

    def on_key_press(self, event, key: str):
        pastkey = key
        self.settings[key] = event.keysym
        print(f"Key '{key}' bound to: {event.keysym}")

        for row in self.control_rows:
            row[1].config(text=self.settings[row[0]])
            if pastkey == row[0]:
                row[0] = key

        self.bind_window.destroy()

    def bind_setting(self, key:str):
        if key[-1] == 's':
            print(f"Rebinding position: {key}")

            self.bind_window = tk.Toplevel()
            self.bind_window.title("Position Bind")
            self.bind_window.geometry("200x100+960+540")
            self.bind_window.focus_set()

            label = tk.Label(self.bind_window, text="Hover your mouse on the center of the arrow and press enter to "
                                                    "bind.\nClose the window to cancel.")
            label.pack(expand=True)

            self.bind_window.bind('<Return>', lambda event: self.on_mouse_bind(key))

            self.bind_window.grab_set()
            self.bind_window.wait_window()
            return

        print(f"Rebinding color: {key}")

        self.bind_window = tk.Toplevel()
        self.bind_window.title("Color Bind")
        self.bind_window.geometry("200x100+960+540")
        self.bind_window.focus_set()

        label = tk.Label(self.bind_window, text="Hover your mouse on the color of the arrow and press enter to "
                                                "bind.\nClose the window to cancel.")
        label.pack(expand=True)

        self.bind_window.bind('<Return>', lambda event: self.on_mouse_bind(key))

        self.bind_window.grab_set()
        self.bind_window.wait_window()

    def on_mouse_bind(self, key):
        if key[-1] == 's':
            print(f'{pyautogui.position().x}, {pyautogui.position().y}')
            self.settings[key] = f'{pyautogui.position().x}, {pyautogui.position().y}'

            for row in self.settings_rows:
                if row[1].get() != self.settings[row[0]] and row[0] != key:
                    self.settings[row[0]] = row[1].get()
                    continue
                row[1].set(self.settings[row[0]])

            self.bind_window.destroy()
            return
        var = f'{pyautogui.pixel(int(pyautogui.position().x), int(pyautogui.position().y))}'
        new_var = ''
        for char in var:
            if char == '(' or char == ')':
                continue
            new_var += char
        var = new_var
        print(var)
        self.settings[key] = var

        for row in self.settings_rows:
            row[1].set(self.settings[row[0]])

        self.bind_window.destroy()

    def discord(self):
        print("discord")

    def support(self):
        print("support")

    def fnf(self):
        print("fnf")


# Calls the application class
if __name__ == "__main__":
    App()





