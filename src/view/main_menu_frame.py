from tkinter import *
from tkinter import ttk


class Main_menu_frame(ttk.Frame):

    def __init__(self, root_window):
        Frame.__init__(self, root_window)
        self.root_window = root_window
        self.font = 'Helvetica 14'

        self.grid(column=0, row=0, sticky=(N, W, E, S))

        self.create_label()
        self.create_button()
        self.create_combobox()

    def create_label(self):
        self.l_pipVersion = ttk.Label(self, text="Pip version: " + self.root_window.cont_ref.version, font=self.font)
        self.l_pipVersion.grid(column=0, row=0)
        self.l_operation = ttk.Label(self, text="Pip command: ", font=self.font)
        self.l_operation.grid(column=0, row=1)
        self.l_option = ttk.Label(self, text="Command options: ", font=self.font)

    def create_button(self):
        self.btn_action = ttk.Button(self, text="Submit")
        self.btn_action.grid(column=2, row=1)

    def create_combobox(self):
        self.cb_operation = ttk.Combobox(self, values=['List'], state="readonly", font=self.font)
        self.cb_operation.grid(column=1, row=1)
        self.cb_operation.bind('<<ComboboxSelected>>', self.display_cbb_option)

    def display_cbb_option(self,*args):
        self.l_option.grid(column = 0, row = 2)
        if(self.cb_operation.get() == "List"):
            self.cb_option = ttk.Combobox(self,
                                          values = ["None"] + self.root_window.cont_ref
                                          .get_option(self.cb_operation.get())
                                          , state="readonly")
            self.cb_option.grid(column=1, row=2)

