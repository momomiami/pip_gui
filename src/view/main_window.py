from tkinter import *
from src.view.mainmenuframe import MainMenuFrame
from src.view.menubar import MenuBar
from src.view.pcklistframe import PckListFrame
from src.view.pckinfoframe import PckInfoFrame
from src.view.searchframe import Searchframe


class MainWindow(Tk):
    window_title = "**Pip GUI**"

    def __init__(self, cont_ref):
        Tk.__init__(self)
        self.resizable(False, False)
        self.cont_ref = cont_ref
        self.option_add('*tearOff', FALSE)
        self.title(self.window_title)
        self.create_main_menu_frame()
        self.mainloop()

    def reset_windows_widgets(self):
        for child in self.winfo_children():
            child.destroy()

    def create_pck_detail_frame(self, pck_name):
        self.reset_windows_widgets()
        MenuBar(self)
        PckInfoFrame(self, pck_name)

    def create_pck_list_frame(self, option):
        self.reset_windows_widgets()
        MenuBar(self)
        PckListFrame(self, option)

    def create_main_menu_frame(self):
        self.reset_windows_widgets()
        MainMenuFrame(self)
        MenuBar(self)

    def create_search_frame(self):
        self.reset_windows_widgets()
        MenuBar(self)
        Searchframe(self)
