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
        self.tableFrame = Frame(self,bg='black')

        label = tk.Label(self, text="Search")
        label.config(font=("Courier", 14))
        label.pack(pady=10, padx=10)

        issuanceList = []
        self.tableFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        label1 = tk.Label(self, text="Search by")
        label1.place(relx = 0.30, rely = 0.09, relheight = 0.08)
        self.bookSelect = ttk.Combobox(self, width = 27, values=["Book name", "Author"], state='readonly')
        self.bookSelect.bind("<<ComboboxSelected>>", self.SearchStrategySelectedCallback)
        self.bookSelect.place(relx = 0.38, rely = 0.10, relheight = 0.05, relwidth = 0.25)

        self.searchSelect = Combobox_Autocomplete(self, searchCallback=self._controller.GetSelectValues,
                                            callbackOnSelection=self.ShowSearchResult)
        self.searchSelect.place(relx = 0.38, rely = 0.20, relheight = 0.05, relwidth = 0.25)
        self.searchSelect.focus()

        self.tableFrame = Frame(self)
        self.tableFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        self.tree = ttk.Treeview(self.tableFrame)
        self.tree["columns"]=("one","two","three", "four")
        self.tree.column("#0", width=140, minwidth=140, stretch=True)
        self.tree.column("one", width=140, minwidth=140, stretch=True)
        self.tree.column("two", width=140, minwidth=140)
        self.tree.column("three", width=140, minwidth=140, stretch=True)
        self.tree.column("four", width=140, minwidth=140, stretch=True)

        self.tree.heading("#0",text="Author name",anchor=tk.W)
        self.tree.heading("one", text="Book name",anchor=tk.W, command=lambda:sortStringColumn(self.tree, "one"))
        self.tree.heading("two", text="Available copy count",anchor=tk.W, command=lambda:sortNumericColumn(self.tree, "two"))
        self.tree.heading("three", text="Page count",anchor=tk.W, command=lambda:sortNumericColumn(self.tree, "three"))
        self.tree.heading("four", text="Publisher",anchor=tk.W, command=lambda:sortStringColumn(self.tree, "four"))

        sx = tk.Scrollbar(self.tableFrame, orient='horizontal', command=self.tree.xview)
        sy = tk.Scrollbar(self.tableFrame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        self.tree.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')

        self.noBooksLabel = tk.Label(self.tableFrame, background='white', text="No books found. Try search first.")
        self.noBooksLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        button = tk.Button(self, text="<<",
            command=lambda:self._controller.BackToStudentPage())
        button.place(relx=0.4, rely=0.85, relwidth=0.25, relheight=0.1)


    def HideNoBooksLabel(self):
        self.noBooksLabel.place_forget()

    def ShowNoBooksLabelWithText(self, text):
        self.noBooksLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.noBooksLabel.config(text=text)

    def SearchStrategySelectedCallback(self, event):
        self._controller.SetSearchStrategy(event)

    def ShowSearchResult(self, event) :
        self._controller.SearchBooks(event)

    def FillTable(self, val):
        for i in range(len(val)):
            self.tree.insert('', 'end', iid=i, text = val[i][2],
            values=(val[i][1], val[i][3], int(val[i][4]), val[i][5]))

    def ClearTable(self):
        self.tree.delete(*self.tree.get_children())


def sortStringColumn(tv, col, reverse=True):
    l = [(tv.set(k, col), int(k)) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda:sortStringColumn(tv, col, not reverse))



def sortNumericColumn(tv, col, reverse=True):
    l = [(int(tv.set(k, col)), int(k)) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda:sortNumericColumn(tv, col, not reverse))