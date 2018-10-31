from tkinter import *


class MenuBar(Menu):
    def __init__(self, root_window):
        Menu.__init__(self, root_window)
        menu_nav = Menu(self)
        self.add_cascade(menu=menu_nav, label='Nav')
        menu_nav.add_command(label='Main Menu', command=root_window.create_main_menu_frame)
        root_window.config(menu=self)
