from tkinter import *
from tkinter import ttk


class Searchframe(ttk.Frame):

    def __init__(self, rootwindow):
        ttk.Frame.__init__(self, rootwindow)
        self.root_window = rootwindow
        self.color_label = "light grey"
        self.font = '14'
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        self.create_label()
        self.create_entry()
        self.create_btn()

    def create_label(self):
        self.label_query = ttk.Label(self, text="Search query: ", font=self.font, background=self.color_label)
        self.label_query.grid(column=0, row=0)

    def create_entry(self):
        self.entry_query = ttk.Entry(self)
        self.entry_query.grid(column=1, row=0)

    def create_btn(self):
        self.btn_search = ttk.Button(self, text="Search PyPI", command=self.execute_search)
        self.btn_search.grid(column=2, row=0)

    def reset_window(self):
        for child in self.winfo_children():
            child.destroy()

        self.create_label()
        self.create_entry()
        self.create_btn()

    def execute_search(self):
        search_response = self.root_window.cont_ref.search_pck(self.entry_query.get())
        self.reset_window()
        if search_response is not None:
            self.create_list_box(search_response)
        else:
            self.create_label_error_search()

    def create_label_error_search(self):
        self.label_error = ttk.Label(self, text="There seems to be an error querying information...", font=self.font,
                                     background=self.color_label)
        self.label_error.grid(column=0, row=1)

    def create_list_box(self, search_response):
        self.listboxSearch = Listbox(self, selectmode="single", width=50, height=15)
        self.listboxSearch.grid(column=0, row=2)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.listboxSearch.yview)
        self.scrollbar.grid(column=1, row=2, sticky=(N, S))
        self.scrollbar2 = ttk.Scrollbar(self, orient="horizontal", command=self.listboxSearch.xview)
        self.scrollbar2.grid(column=0, row=3, sticky=(W, E))
        self.listboxSearch.configure(yscrollcommand=self.scrollbar.set, selectmode="single")
        self.listboxSearch.configure(xscrollcommand=self.scrollbar2.set, selectmode="single")
        for k,v in search_response.items():
            self.listboxSearch.insert(END, k+v)
