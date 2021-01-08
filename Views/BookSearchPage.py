import tkinter as tk
from tkinter import *
from Controllers.BookSearchController import BookSearchController
from CustomWidets.ComboboxAutocomplete import Combobox_Autocomplete
from ttkwidgets import Table
from tkinter import ttk

class BookSearchPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = BookSearchController(master, self._model, self)
        self._model.Register(self)
        labelFrame = Frame(self,bg='black')

        label = tk.Label(self, text="Search")
        label.config(font=("Courier", 14))
        label.pack(pady=10, padx=10)

        issuanceList = []
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        label1 = tk.Label(self, text="Search by")
        label1.place(relx = 0.30, rely = 0.1, relheight = 0.08)
        self.bookSelect = ttk.Combobox(self, width = 27, values=["Book name", "Author"])
        self.bookSelect.bind("<<ComboboxSelected>>", self.SearchStrategySelectedCallback)
        self.bookSelect.place(relx = 0.38, rely = 0.10, relheight = 0.05, relwidth = 0.25)

        self.searchSelect = Combobox_Autocomplete(self, searchCallback=self._controller.GetSelectValues,
                                            callbackOnSelection=self.ShowSearchResult)
        self.searchSelect.place(relx = 0.38, rely = 0.20, relheight = 0.05, relwidth = 0.25)
        self.searchSelect.focus()

        labelFrame = Frame(self)
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        self.tree = ttk.Treeview(labelFrame)
        self.tree["columns"]=("one","two","three", "four")
        self.tree.column("#0", width=140, minwidth=140, stretch=True)
        self.tree.column("one", width=140, minwidth=140, stretch=True)
        self.tree.column("two", width=140, minwidth=140)
        self.tree.column("three", width=140, minwidth=140, stretch=True)
        self.tree.column("four", width=140, minwidth=140, stretch=True)

        self.tree.heading("#0",text="Author name",anchor=tk.W)
        self.tree.heading("one", text="Book name",anchor=tk.W)
        self.tree.heading("two", text="Available copy count",anchor=tk.W)
        self.tree.heading("three", text="Page count",anchor=tk.W)
        self.tree.heading("four", text="Publisher",anchor=tk.W)

        sx = tk.Scrollbar(labelFrame, orient='horizontal', command=self.tree.xview)
        sy = tk.Scrollbar(labelFrame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        self.tree.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')

        button = tk.Button(self, text="Back",
            command=lambda:self._controller.BackToStudentPage())
        button.place(relx=0.4, rely=0.80, relwidth=0.25, relheight=0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        pass

    def SearchStrategySelectedCallback(self, event):
        self._controller.SetSearchStrategy(event)

    def ShowSearchResult(self, event) :
        self._controller.SearchBooks(event)

    def FillTable(self, val):
        for i in range(len(val)):
            self.tree.insert('', 'end', iid=i, text = val[i][2],
            values=(val[i][1], val[i][3], val[i][4], val[i][5]))

    def ClearTable(self):
        self.tree.delete(*self.tree.get_children())
