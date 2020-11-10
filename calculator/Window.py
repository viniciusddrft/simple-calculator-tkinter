import tkinter as tk
from typing import List

def make_window() -> tk.Tk:
    window = tk.Tk()
    window.title('___Calculator___')
    window.config(padx=10, pady=10, background='#333')
    window.resizable(False, False)

    return window

def make_label(window) -> tk.Label:
    label = tk.Label(window,
        text = '',
        anchor='e',
        justify='right',
        background='#333'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def make_display(window) -> tk.Entry:
    display = tk.Entry(window)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Ani',40,'bold'),
        justify = 'right',
        bd=1,
        relief = 'flat',
        highlightthickness=1,
        highlightcolor='#333',
        background='#333'
    )
    display.bind('<Control-a>', display_control_a)
    return display


def display_control_a(event=None):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_buttons(window) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7','8','9','+','c'],
        ['4','5','6','-','/'],
        ['1','2','3','*','^'],
        ['0','.','(',')','='],
    ]

    buttons: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(window, text=col_value)
            btn.grid(row=row_index, column=col_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Ani', 15, 'normal'),
                pady=40, width=1, background='#333', bd = 0,fg='#fff',
                cursor='hand2' , highlightthickness=0,
                highlightcolor='#ccc', activebackground='#555',
                highlightbackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
