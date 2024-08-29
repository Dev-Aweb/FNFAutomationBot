"""

"""

# Modules and Packages
import pyautogui
import time
from pynput.keyboard import Controller
import tkinter as tk
from tkinter import ttk, messagebox
import themed_tk
import keyboard
from configparser import ConfigParser

keyboard_controller = Controller()

# Main function for key pressing.
def press_key(position: tuple[int, int],
              color: tuple[float, float, float],
              key: str,
              ):
    while True:
        color_pos = pyautogui.pixel(position[0], position[1])
        print(position, color, color_pos)
        if color_pos == color:
            print('yes')
            keyboard_controller.press(key)
            while True:
                release_color_pos = pyautogui.pixel(position[0], position[1]+100)
                if release_color_pos != color:
                    time.sleep(0.1)
                    keyboard_controller.release(key)
                    break

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


class App:

    def __init__(self):
        # Window Setting
        self.root = tk.Tk()
        self.root.geometry('450x510')
        self.root.title('FNF Automation Bot')
        self.root.wm_minsize(450, 510)
        self.root.wm_maxsize(450, 510)
        self.root.wm_iconbitmap('icon.ico')

        # Variables
        self.on = False
        self.settings = {
            'left': 's',
            'down': 'd',
            'up': 'j',
            'right': 'k',
            'on/off': 'f1',
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
        self.settings['on/off'] = self.save.get('Controls', 'on/off')
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

        # Controls
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
        self.create_control_row(self.controls_frame, "On/Off", 'on/off', 6)

        # Settings
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

        self.start_button = self.Button('Turn On', self.root, self.theme, font=('', 16), command=self.start)
        self.start_button.place(x=175, y=460)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        try:
            for process in self.processes:
                if process.is_alive():
                    process.terminate()
                    process.join()
        except AttributeError:
            pass

        self.save.set('Controls', 'left', self.settings['left'])
        self.save.set('Controls', 'down', self.settings['down'])
        self.save.set('Controls', 'up', self.settings['up'])
        self.save.set('Controls', 'right', self.settings['right'])
        self.save.set('Controls', 'on/off', self.settings['on/off'])
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

        self.root.destroy()
        quit()

    def start(self):
        if self.on:
            self.start_button.config(text='Turn On')
            for process in self.processes:
                if process.is_alive():
                    process.terminate()
                    process.join()

            self.on = False
            return
        self.on = True
        self.start_button.config(text='Turn Off')

        for row in self.settings_rows:
            self.settings[row[0]] = row[1].get()

        left_pos = separate(self.settings.get('left_pos'), True)
        down_pos = separate(self.settings.get('down_pos'), True)
        up_pos = separate(self.settings.get('up_pos'), True)
        right_pos = separate(self.settings.get('right_pos'), True)

        left_color = separate(self.settings.get('left_color'), True)
        down_color = separate(self.settings.get('down_color'), True)
        up_color = separate(self.settings.get('up_color'), True)
        right_color = separate(self.settings.get('right_color'), True)

        print(f'left position: {left_pos}')
        print(f'down position: {down_pos}')
        print(f'up position: {up_pos}')
        print(f'right position: {right_pos}')
        print(f'left color: {left_color}')
        print(f'down color: {down_color}')
        print(f'up color: {up_color}')
        print(f'right color: {right_color}')

        import multiprocessing

        self.processes = [
            multiprocessing.Process(target=press_key, args=((left_pos[0], left_pos[1]), (left_color[0], left_color[1], left_color[2]), self.settings.get('left'))),
            multiprocessing.Process(target=press_key, args=((down_pos[0], down_pos[1]), (down_color[0], down_color[1], down_color[2]), self.settings.get('down'))),
            multiprocessing.Process(target=press_key, args=((up_pos[0], up_pos[1]), (up_color[0], up_color[1], up_color[2]), self.settings.get('up'))),
            multiprocessing.Process(target=press_key, args=((right_pos[0], right_pos[1]), (right_color[0], right_color[1], right_color[2]), self.settings.get('right'))),
        ]

        for process in self.processes:
            process.start()

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

if __name__ == "__main__":
    App()





