from Window import *

from Calculator import *


def main():
    window = make_window()
    display = make_display(window)
    label = make_label(window)
    buttons = make_buttons(window)
    calculator = Calculator(window, label, display, buttons)
    calculator.start()





if __name__ == "__main__":
    main()

    