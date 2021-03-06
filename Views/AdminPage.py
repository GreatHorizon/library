import tkinter as tk
from tkinter import *
from Controllers.AdminPageController import AdminPageController


class AdminPage(tk.Frame):

    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = AdminPageController(master, self._model, self)
        
        
        label1 = tk.Label(self, text="Admin page")
        label1.config(font=("Courier", 18))
        label1.pack(pady=20,padx=20)

        studentDebtsBtn = Button(self, text="Student Debts",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenStudentDebtsPage())
        studentDebtsBtn.place(relx=0.4, rely=0.15, relwidth=0.2,relheight=0.1)

        returnBookBtn = Button(self, text="Return Book",bg='#d1ccc0', fg='black',
                command=lambda:self._controller.OpenReturnBookPage())
        returnBookBtn.place(relx=0.4, rely=0.25, relwidth=0.2,relheight=0.1)

        issueBookBtn = Button(self, text="Issue Book",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenBookIssuePage())
        issueBookBtn.place(relx=0.4, rely=0.35, relwidth=0.2,relheight=0.1)

        addBookBtn = Button(self, text="Add Book",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenAddBookPage())
        addBookBtn.place(relx=0.4, rely=0.45, relwidth=0.2,relheight=0.1)

        deleteBookBtn = Button(self, text="Delete book",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenDeleteBookPage())
        deleteBookBtn.place(relx=0.4, rely=0.55, relwidth=0.2,relheight=0.1)

        regStudBtn = Button(self, text="Register student",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenStudentRegistrationPage())
        regStudBtn.place(relx=0.4, rely=0.65, relwidth=0.2,relheight=0.1)

        editBookBtn = Button(self, text="Edit book",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenEditBookPage())
        editBookBtn.place(relx=0.4, rely=0.75, relwidth=0.2,relheight=0.1)

        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToAdminAuthorizationPage())
        button.place(relx=0.4, rely=0.85, relwidth=0.2,relheight=0.1)

    def Flex(self):
        pass

