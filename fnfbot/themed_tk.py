import tkinter as tk

def Button(
        text: str,
        frame: tk.Frame,
        theme: dict,
        font: tuple[str, int],
        command,
        pad: tuple[float, float] = (0, 0),
        *args
        ):
    return tk.Button(frame, text=text, border=0, background=theme.get('button_bg'), foreground=theme.get('button_fg'),
                     activebackground=theme.get('active_button_bg'), activeforeground=theme.get('active_button_fg'),
                     font=font, command=command, padx=pad[0], pady=pad[1])
