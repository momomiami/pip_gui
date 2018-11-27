from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class PckInfoFrame(ttk.Frame):
    def __init__(self, root_window, pck_name):
        ttk.Frame.__init__(self, root_window)
        self.root_window = root_window
        self.pck = self.root_window.cont_ref.get_pck_info(pck_name)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.color_label1 = "light grey"
        self.color_label2 = "white"
        self.font = '14'
        self.displayInfo()
        self.uninstall_btn()

    def displayInfo(self):
        ttk.Label(self, text="Package name:", font=self.font, background=self.color_label1).grid(column=0, row=0,
                                                                                                 sticky=W)
        ttk.Label(self, text=self.pck.name, font=self.font, background=self.color_label2).grid(column=1, row=0,
                                                                                               sticky=W)

        ttk.Label(self, text="Version:", font=self.font, background=self.color_label1).grid(column=0, row=1, sticky=W)
        ttk.Label(self, text=self.pck.version, font=self.font, background=self.color_label2).grid(column=1, row=1,
                                                                                                  sticky=W)

        ttk.Label(self, text="Package summary:", font=self.font, background=self.color_label1).grid(column=0, row=2,
                                                                                                    sticky=W)
        ttk.Label(self, text=self.pck.summary, font=self.font, background=self.color_label2).grid(column=1, row=2,
                                                                                                  sticky=W)

        ttk.Label(self, text="Home page:", font=self.font, background=self.color_label1).grid(column=0, row=3, sticky=W)
        ttk.Label(self, text=self.pck.home_page, font=self.font, background=self.color_label2).grid(column=1, row=3,
                                                                                                    sticky=W)

        ttk.Label(self, text="Author:", font=self.font, background=self.color_label1).grid(column=0, row=4, sticky=W)
        ttk.Label(self, text=self.pck.author, font=self.font, background=self.color_label2).grid(column=1, row=4,
                                                                                                 sticky=W)

        ttk.Label(self, text="Author email:", font=self.font, background=self.color_label1).grid(column=0, row=5,
                                                                                                 sticky=W)
        ttk.Label(self, text=self.pck.author_email, font=self.font, background=self.color_label2).grid(column=1, row=5,
                                                                                                       sticky=W)

        ttk.Label(self, text="License type:", font=self.font, background=self.color_label1).grid(column=0, row=6,
                                                                                                 sticky=W)
        ttk.Label(self, text=self.pck.license_type, font=self.font, background=self.color_label2).grid(column=1, row=6,
                                                                                                       sticky=W)

        ttk.Label(self, text="Package location:", font=self.font, background=self.color_label1).grid(column=0, row=7,
                                                                                                     sticky=W)
        ttk.Label(self, text=self.pck.location, font=self.font, background=self.color_label2).grid(column=1, row=7,
                                                                                                   sticky=W)

        ttk.Label(self, text="Package(s) required:", font=self.font, background=self.color_label1).grid(column=0, row=8,
                                                                                                        sticky=W)
        req_list_box = Listbox(self, selectmode="single", width=0, height=5)
        req_list_box.grid(column=1, row=8, sticky=E)
        scrollbar1 = ttk.Scrollbar(self, orient="vertical", command=req_list_box.yview)
        scrollbar1.grid(column=2, row=8, sticky=(N, S))
        req_list_box.configure(yscrollcommand=scrollbar1.set, selectmode="single")

        for pck_name in self.pck.require_list:
            req_list_box.insert(END, pck_name)
        if self.pck.require_list[0] == '':
            req_list_box.destroy()
            scrollbar1.destroy()
            ttk.Label(self, text="No Package required", font=self.font, background=self.color_label2).grid(column=1,
                                                                                                           row=8,
                                                                                                           sticky=W)

        ttk.Label(self, text="Package(s) which required " + self.pck.name, font=self.font,
                  background=self.color_label1).grid(column=0, row=9,
                                                     sticky=W)
        req_list_by_box = Listbox(self, selectmode="single", width=0, height=5)
        req_list_by_box.grid(column=1, row=9, sticky=E)
        scrollbar2 = ttk.Scrollbar(self, orient="vertical", command=req_list_by_box.yview)
        scrollbar2.grid(column=2, row=9, sticky=(N, S))
        req_list_by_box.configure(yscrollcommand=scrollbar2.set, selectmode="single")

        for pck_name in self.pck.require_by_list:
            req_list_by_box.insert(END, pck_name)
        if self.pck.require_by_list[0] == '':
            req_list_by_box.destroy()
            scrollbar2.destroy()
            ttk.Label(self, text="No Package required by " + self.pck.name, font=self.font,
                      background=self.color_label2) \
                .grid(column=1, row=9, sticky=W)

        ttk.Label(self, text="Installed files:", font=self.font, background=self.color_label1).grid(column=0, row=10,
                                                                                                    sticky=W)
        files_installed = Listbox(self, selectmode="single", width=0, height=5)
        files_installed.grid(column=1, row=10, sticky=E)
        scrollbar3 = ttk.Scrollbar(self, orient="vertical", command=files_installed.yview)
        scrollbar3.grid(column=2, row=10, sticky=(N, S))
        files_installed.configure(yscrollcommand=scrollbar3.set, selectmode="single")

        for pck_name in self.pck.pck_files:
            files_installed.insert(END, pck_name)

    def uninstall_btn(self):
        btn = ttk.Button(self, text="Uninstall " + self.pck.name, command=self.confirmation_prompt)
        btn.grid(column=3, row=0)

    def confirmation_prompt(self):
        user_input = messagebox.askyesno(message='Are you sure you want to uninstall ' + self.pck.name, icon='warning',
                                         title='Uninstall ' + self.pck.name)
        if user_input:
            self.root_window.cont_ref.uninstall_pck(self.pck.name)
            messagebox.showinfo(message=self.pck.name+' has been successfully uninstalled')
            self.root_window.create_main_menu_frame()
