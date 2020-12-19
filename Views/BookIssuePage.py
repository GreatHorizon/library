import tkinter as tk
from tkinter import *

from Controllers.BookIssueController import BookIssueController

class BookIssuePage(tk.Frame):
    def __init__(self, parent, window, model):
        tk.Frame.__init__(self, parent)
        self._model = model
        self._controller = BookIssueController(window, self._model, self)

        label1 = tk.Label(self, text="book issue")
        label1.pack(pady=20, padx=20)  

        self.create_widgets()
        
    def create_widgets(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT,fill="y")

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self, textvariable=self.search_var, width=13)
        self.entry.pack()
        self.lbox = Listbox(self, width=45, height=5)
        self.lbox.pack(side=LEFT, fill="both", expand=True)
        scrollbar.config(command=self.lbox.yview)
        self.lbox.config(yscrollcommand=scrollbar.set)
        #self.lbox.bind('<Double-1>', print(self.lbox.get())) 
        #self.entry.grid(row=0, column=0, padx=10, pady=3)
        #self.lbox.grid(row=1, column=0, padx=10, pady=3)
        self.entry.pack()
        self.lbox.pack()

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self, *args):
        search_term = self.search_var.get()

        # Just a generic list to populate the listbox
        lbox_list = ['Adam(123)', 'Lucy', 'Barry', 'Bob',
                    'James', 'Frank', 'Susan(8)', 'Amanda', 'Christie']

        self.lbox.delete(0, END)

        for item in lbox_list:
                if search_term.lower() in item.lower():
                    self.lbox.insert(END, item)