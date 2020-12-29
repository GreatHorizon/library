import tkinter as tk
from tkinter import *
from tkinter import messagebox
import psycopg2
from Database.database import *
from Controllers.StudentAuthorizationController import StudentAuthorizationController

class StudentAuthorizationPage(tk.Frame):

    def __init__(self, parent, window, model):
        tk.Frame.__init__(self, parent)
        self._model = model
        self._controller = StudentAuthorizationController(window, self._model, self)
        self._model.Register(self)

        label = tk.Label(self, text="Student authorization page")
        label.pack(pady=10,padx=10)


        lb1 = Label(self,text="Student ID", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        self.studentIdField = Entry(self, width = 30)
        self.studentIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="Password", fg='black')
        lb2.place(relx = 0.25, rely = 0.3, relheight = 0.08)

        self.passwordField = Entry(self, width = 30, show='*')
        self.passwordField.place(relx = 0.35, rely = 0.3, relwidth = 0.3, relheight = 0.08)

        self.error = Label(self, text='', fg='red')
        self.error.place(relx = 0.35, rely = 0.39, relheight = 0.05)

        button = tk.Button(self, text="Sign in as student",
                            command=lambda: self._controller.SignInStudent(self.studentIdField.get(), self.passwordField.get()))
        button.place(relx=0.4, rely=0.45, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToStartPage())
        button.place(relx = 0.35, rely = 0.45, relheight = 0.1)

    def Notify(self):
        if (self._model._isAuthorizated):
            self._controller.SendData(id=self._model._userId)
            self._controller.OpenStudentPage()
            self.ClearErrorLabel()
        else:
            self.error.config(text=self._model._message)
        self.ClearFields()

    def ClearFields(self):
        self.studentIdField.delete(0, len(self.studentIdField.get()))
        self.passwordField.delete(0, len(self.passwordField.get()))
    def ClearErrorLabel(self):
        self.error.config(text='') 