import tkinter as tk
from tkinter import *
from Controllers.StudentPageController import StudentPageController
import sys
import os
sys.path.append(os.path.abspath('images'))

class StudentPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = StudentPageController(master, self._model, self)

        label1 = tk.Label(self, text="Student Page")
        label1.pack(pady=20, padx=20)

        searchBookBtn = Button(self, text="Search book", bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenBookSearchPage())
        searchBookBtn.place(relx=0.4, rely=0.45, relwidth=0.2,relheight=0.1)

        showIssuanceBtn = Button(self, text="My issuance", bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenStudentIssuanceList())
        showIssuanceBtn.place(relx=0.4, rely=0.55, relwidth=0.2,relheight=0.1)

        changePassBtn = Button(self, text="Change password", bg='#d1ccc0', fg='black',
        command=lambda:self._controller.OpenChangePasswordPage())
        changePassBtn.place(relx=0.4, rely=0.65, relwidth=0.2,relheight=0.1)

        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToStudentAuthorizationPage())
        button.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)

    def recieve_data(self, **data):
        self._controller.SaveData(data['id'])