import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkwidgets import Table
import psycopg2
from datetime import *

from Controllers.StudentIssuancePageController import StudentIssuancePageController
from Utils.SortingUtil import SortNumericColumn, SortStringColumn, SortDateColumn

class StudentIssuancePage(tk.Frame):

    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = StudentIssuancePageController(master, self._model, self)
        self._model.Register(self)

        label1 = tk.Label(self, text="My issuance")
        label1.config(font=("Courier", 18))
        label1.pack(pady=20,padx=20)

        self.tableFrame = Frame(self)
        self.tableFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        self.tree = ttk.Treeview(self.tableFrame)
        self.tree["columns"]=("one","two","three", "four", "five")

        self.tree.column('#0', width=0, minwidth=140, stretch=False)
        self.tree.column('one', width=140, minwidth=140, stretch=True)
        self.tree.column('two', width=140, minwidth=140, stretch=True)
        self.tree.column('three', width=140, minwidth=140)
        self.tree.column('four', width=140, minwidth=140, stretch=True)
        self.tree.column('five', width=140, minwidth=140, stretch=True)

        self.tree.heading('#0', text="Index",anchor=tk.W)
        self.tree.heading('one',text="Author name",anchor=tk.W, command=lambda:SortStringColumn(self.tree, "one"))
        self.tree.heading('two', text="Book name",anchor=tk.W, command=lambda:SortStringColumn(self.tree, "two"))
        self.tree.heading('three', text="Сopy ID",anchor=tk.W, command=lambda:SortNumericColumn(self.tree, "three"))
        self.tree.heading('four', text="Start",anchor=tk.W, command=lambda:SortDateColumn(self.tree, "four"))
        self.tree.heading('five', text="End",anchor=tk.W, command=lambda:SortDateColumn(self.tree, "five"))

        sx = tk.Scrollbar(self.tableFrame, orient='horizontal', command=self.tree.xview)
        sy = tk.Scrollbar(self.tableFrame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        self.noDataLabel = tk.Label(self.tableFrame, background="white",text="")

        self.tree.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')

        self._controller.GetStudentIssuance()

        button = tk.Button(self, text="Back",
            command=lambda:self._controller.BackToStudentPage())
        button.place(relx=0.4, rely=0.80, relwidth=0.25, relheight=0.1)
            
    def updateView(self) :
        self._controller.GetStudentIssuance(self.id)

    def recieve_data(self, **data):
        self.id = data['id']

    def FillTable(self, val):
        for i in range(len(val)):
            self.tree.insert('', 'end', iid=i, text = i,
            values=(val[i][0], val[i][1], val[i][2], str(val[i][3]), str(val[i][4])))

    def HideNoDataLabel(self):
        self.noDataLabel.place_forget()

    def ShowNoDataLabelWithText(self, text):
        self.noDataLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.noDataLabel.config(text=text)