import tkinter as tk
from tkinter import *
import sys
import os
sys.path.append(os.path.abspath('Views'))
from Controllers.AdminAuthorizationController import AdminAuthorizationController

class AdminAuthorizationPage(tk.Frame):

    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = AdminAuthorizationController(master, self._model, self)
        self._model.Register(self)

        label = tk.Label(self, text="Admin authorization page")
        label.config(font=("Courier", 18))
        label.pack(pady=10, padx=10)

        lb1 = Label(self,text="Admin id", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        self.adminIdField = Entry(self, width = 30)
        self.adminIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="Password", fg='black')
        lb2.place(relx = 0.25, rely = 0.3, relheight = 0.08)

        self.passwordField = Entry(self, width = 30, show='*')
        self.passwordField.place(relx = 0.35, rely = 0.3, relwidth = 0.3, relheight = 0.08)

        self.error = Label(self, text='', fg='red')
        self.error.place(relx = 0.35, rely = 0.39, relheight = 0.05)

        button = tk.Button(self, text="Sing in as admin",
                            command=lambda:self._controller.SignInAdmin(self.adminIdField.get(), self.passwordField.get()))
        button.place(relx=0.4, rely=0.45, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToStartPage())
        button.place(relx = 0.35, rely = 0.45, relheight = 0.1)

    def Notify(self):
        if (self._model._isAuthorizated):
            self._controller.OpenAdminPage()
        else:
            self.error.config(text=self._model._message)

    def ClearFields(self):
        self.adminIdField.delete(0, len(self.adminIdField.get()))
        self.passwordField.delete(0, len(self.passwordField.get()))

    def ClearErrorLabel(self):
        self.error.config(text='')




        
