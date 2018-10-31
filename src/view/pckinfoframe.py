from tkinter import *
from tkinter import ttk


class PckInfoFrame(ttk.Frame):
    def __init__(self, root_window, pck_name):
        ttk.Frame.__init__(self, root_window)
        self.root_window = root_window
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.color_label = "light grey"
        self.font = '14'
        self.create_label(pck_name)

    def create_label(self, pck_name):
        pck = self.root_window.cont_ref.get_pck_info(pck_name)
        pck_str_info = "Package name: " + pck.name + "\nVersion: " + pck.version + "\nSummary: " + pck.summary
        pck_str_info += "\nHome page: " + pck.home_page + "\nAuthor: " + pck.author
        pck_str_info += "\nAuthor email: " + pck.author_email + "\nLicense type: " + pck.license_type
        pck_str_info += "\nPackage location" + pck.location + "\nPackage requirement:\n \n"
        for obj in pck.require_list:
            pck_str_info += obj + "\n"
        pck_str_info += "\nRequired by:\n\n"
        for obj in pck.require_list:
            pck_str_info += obj + "\n"
        ttk.Label(self, text=pck_str_info, font=self.font, background=self.color_label).grid(column=0, row=0)
