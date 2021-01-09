import tkinter as tk
from tkinter import *
from CustomWidets.ComboboxAutocomplete import Combobox_Autocomplete
from Controllers.StudentDebtsController import StudentDebtsController
from tkinter import ttk
from Utils.SortingUtil import SortDateColumn, SortNumericColumn, SortStringColumn

class StudentDebtsPage(tk.Frame):
    
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._controller = StudentDebtsController(master, model, self)
        
        label1 = tk.Label(self, text="Student debts page")
        label1.config(font=("Courier", 14))
        label1.pack(pady=20,padx=20)

        label2 = tk.Label(self, text="Select student by id")
        label2.place(relx = 0.25, rely = 0.15, relheight = 0.08)
        self.userSelect = Combobox_Autocomplete(self, searchCallback=self._controller.GetStudentsInfo,
                                                    callbackOnSelection=self._controller.GetStudentDebtsAndShowTable)
        self.userSelect.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        self.userSelect.focus()

        self.tableFrame = Frame(self)
        self.tableFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        self.userInfoFrame = Frame(self)
        self.userInfoFrame.place(relx=0.1,rely=0.225,relwidth=0.8,relheight=0.05)

        self.tree = ttk.Treeview(self.tableFrame)
        self.tree["columns"]=("one","two","three", "four", "five")
        self.tree.column('#0', width=0, minwidth=140, stretch=False)
        self.tree.column("one", width=140, minwidth=140, stretch=True)
        self.tree.column("two", width=140, minwidth=140, stretch=True)
        self.tree.column("three", width=140, minwidth=140)
        self.tree.column("four", width=140, minwidth=140, stretch=True)
        self.tree.column("five", width=140, minwidth=140, stretch=True)
        self.tree.place_forget()

        self.tree.heading('#0', text="Index",anchor=tk.W)
        self.tree.heading("one",text="Author name",anchor=tk.W, command=lambda:SortStringColumn(self.tree, "one"))
        self.tree.heading("two", text="Book name",anchor=tk.W, command=lambda:SortStringColumn(self.tree, "two"))
        self.tree.heading("three", text="Id copy",anchor=tk.W, command=lambda:SortNumericColumn(self.tree, "three"))
        self.tree.heading("four", text="Start",anchor=tk.W, command=lambda:SortDateColumn(self.tree, "four"))
        self.tree.heading("five", text="End",anchor=tk.W, command=lambda:SortDateColumn(self.tree, "five"))

        sx = tk.Scrollbar(self.tableFrame, orient='horizontal', command=self.tree.xview)
        sy = tk.Scrollbar(self.tableFrame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        self.tree.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')

        self.message = Label(self, text='', fg='red')
        self.message.place(relx = 0.35, rely = 0.82, relheight = 0.05)

        self.noDataLabel = tk.Label(self.tableFrame, background="white",text="No issues found. Select user first.")
        self.noDataLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        button = tk.Button(self, text="Return selected books",
                command=lambda: self._controller.ReturnBooks(self.GetCopiesIdFromTable()))
        button.place(relx=0.4, rely=0.88, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.88, relheight = 0.1)


    def FillTable(self, val):
        for i in range(len(val)):
            self.tree.insert('', 'end', iid=i, text = i,
            values=(val[i][0], val[i][1], val[i][2], val[i][3], val[i][4]))

    def GetCopiesIdFromTable(self):
        selectedIndexes =self.tree.selection()
        res = []
        for it in range(len(selectedIndexes)):
            res.append(self.tree.item(it)['values'][1])
        return res

  
    def HideNoDataLabel(self):
        self.noDataLabel.place_forget()

    def ShowNoDataLabelWithText(self, text):
        self.noDataLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.noDataLabel.config(text=text)

    def ClearTable(self):
        self.tree.delete(*self.tree.get_children())

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def ShowUserInfo(self, name, surname, phone, email):
        self.userInfoFrame = Frame(self)
        self.userInfoFrame.place(relx=0.1,rely=0.225,relwidth=0.8,relheight=0.05)

        self.userName = tk.Label(self.userInfoFrame, text="Name: " + name)
        self.userName.place(relx=0,rely=0.225)
        self.userSurname = tk.Label(self.userInfoFrame, text="Surname: " + surname)
        self.userSurname.place(relx=0.25,rely=0.225)
        self.userPhone = tk.Label(self.userInfoFrame, text="Phone: " + phone)
        self.userPhone.place(relx=0.5, rely=0.225)  
        self.userEmail = tk.Label(self.userInfoFrame, text="Email: " + email)
        self.userEmail.place(relx=0.75, rely=0.225)  

    def HideUserInfo(self):
        self.userInfoFrame.place_forget()
    