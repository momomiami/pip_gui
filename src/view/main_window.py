from tkinter import *
from tkinter import ttk
from src.view.main_menu_frame import Main_menu_frame
from src.view.menu_bar import Menu_bar

class MainWindow(Tk):
    window_title = "**Pip GUI**"

    def __init__(self, cont_ref):
        Tk.__init__(self)
        self.cont_ref = cont_ref
        self.option_add('*tearOff', FALSE)
        self.title(self.window_title)

        self.create_main_menu_frame()

        self.mainloop()

    def reset_windows_widgets(self):
        for child in self.winfo_children():
            child.destroy()

    def create_main_menu_frame(self):
        self.reset_windows_widgets()
        Main_menu_frame(self)
        Menu_bar(self)