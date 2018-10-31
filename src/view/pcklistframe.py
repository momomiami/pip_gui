from tkinter import *
from tkinter import ttk


class PckListFrame(ttk.Frame):

    def __init__(self, root_window, option):
        ttk.Frame.__init__(self, root_window)
        self.root_window = root_window
        self.color_label = "light grey"
        self.font = '14'
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.create_label(option)
        self.create_button()
        self.create_list_box(option)

    def create_label(self, option):
        if option == "None":
            ttk.Label(self, text="List of installed packages:", font=self.font).grid(column=0, row=0)
        else:
            ttk.Label(self, text=self.root_window.cont_ref.get_option("List")[option], font=self.font)\
                .grid(column=0, row=0)

    def create_list_box(self, option):
        self.listboxPck = Listbox(self, selectmode="single", width=0, height=15)
        self.listboxPck.grid(column=0, row=1)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.listboxPck.yview)
        self.scrollbar.grid(column=1, row=1, sticky=(N, S))
        self.listboxPck.configure(yscrollcommand=self.scrollbar.set, selectmode="single")
        list_pck_name = self.root_window.cont_ref.get_pck_list_name(option)
        for pck_name in list_pck_name:
            self.listboxPck.insert(END, pck_name)
        if not list_pck_name:
            self.listboxPck.config(height=0)

    def create_button(self):
        self.btn_pck_detail = ttk.Button(self, text="Check details", command=self.change_frame)
        self.btn_pck_detail.grid(column=2, row=1)

    def change_frame(self):
        self.root_window.create_pck_detail_frame(self.listboxPck.get(self.listboxPck.curselection()[0]))
