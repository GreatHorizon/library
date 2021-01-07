import tkinter as tk
from tkinter import *
from CustomWidets.ComboboxAutocomplete import Combobox_Autocomplete
from Controllers.StudentDebtsController import StudentDebtsController
from tkinter import ttk

class StudentDebtsPage(tk.Frame):
    
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._controller = StudentDebtsController(master, model, self)
        
        label1 = tk.Label(self, text="Student debts page")
        label1.pack(pady=20,padx=20)

        label2 = tk.Label(self, text="Select student by id")
        label2.place(relx = 0.25, rely = 0.15, relheight = 0.08)
        self.userSelect = Combobox_Autocomplete(self, searchCallback=self._controller.GetStudentsInfo,
                                                    callbackOnSelection=self._controller.GetStudentDebtsAndShowTable)
        self.userSelect.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        self.userSelect.focus()

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
        self.tree.heading("two", text="Id copy",anchor=tk.W)
        self.tree.heading("three", text="Start",anchor=tk.W)
        self.tree.heading("four", text="End",anchor=tk.W)


        sx = tk.Scrollbar(labelFrame, orient='horizontal', command=self.tree.xview)
        sy = tk.Scrollbar(labelFrame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        self.tree.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')

        self.message = Label(self, text='', fg='red')
        self.message.place(relx = 0.35, rely = 0.82, relheight = 0.05)

        button = tk.Button(self, text="Return selected books",
                command=lambda: self._controller.ReturnBooks(self.GetCopiesIdFromTable()))
        button.place(relx=0.4, rely=0.88, relwidth=0.25, relheight=0.1)
    
        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.88, relheight = 0.1)


    def FillTable(self, val):
        for i in range(len(val)):
            self.tree.insert('', 'end', iid=i, text = val[i][2],
            values=(val[i][1], val[i][0], val[i][3], val[i][4]))
            
    def ClearTable(self):
        self.tree.delete(*self.tree.get_children())

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)
