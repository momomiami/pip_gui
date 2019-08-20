from tkinter import *
from tkinter import ttk


class MainMenuFrame(ttk.Frame):

    def __init__(self, root_window):
        ttk.Frame.__init__(self, root_window)
        self.root_window = root_window
        self.color_label = "light grey"
        self.font = '14'
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.create_label()
        self.create_button()
        self.create_combobox()

    def create_label(self):
        self.l_pipVersion = ttk.Label(self, text="Pip version: " + self.root_window.cont_ref.version, font=self.font,
                                      background=self.color_label)
        self.l_pipVersion.grid(column=0, row=0)
        self.l_operation = ttk.Label(self, text="Pip command: ", font=self.font, background=self.color_label)
        self.l_operation.grid(column=0, row=1)
        self.l_option = ttk.Label(self, text="Command options: ", font=self.font, background=self.color_label)

    def create_button(self):
        self.btn_action = ttk.Button(self, text="Submit", command=self.change_frame)
        self.btn_action.grid(column=2, row=1)

    def change_frame(self):
        if self.cb_operation.get() == "List":
            if self.cb_option.get() != "":
                self.root_window.create_pck_list_frame(self.cb_option.get())
            else:
                self.root_window.create_pck_list_frame("None")
        elif self.cb_operation.get() == "Search":
            self.root_window.create_search_frame()

    def create_combobox(self):
        self.cb_operation = ttk.Combobox(self, values=['List', 'Search'], state="readonly", font=self.font)
        self.cb_operation.grid(column=1, row=1)
        self.cb_operation.bind('<<ComboboxSelected>>', self.display_cbb_option)

    def display_cbb_option(self, *args):
        self.l_option.grid(column=0, row=2)
        if self.cb_operation.get() == "List":
            self.cb_option = ttk.Combobox(self, values=["None"] + list(self.root_window.cont_ref.get_option(
                self.cb_operation.get()).keys()), state="readonly", font=self.font)
            self.cb_option.grid(column=1, row=2)
        elif self.cb_operation.get() == "Search":
            self.cb_option = ttk.Combobox(self, values=["None"], state="readonly", font=self.font)
            self.cb_option.grid(column=1, row=2)
