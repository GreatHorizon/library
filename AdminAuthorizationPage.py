import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Database.database import *

class AdminAuthorizationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Admin authorization page")
        label.pack(pady=10, padx=10)

        lb1 = Label(self,text="Admin id", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        adminIdField = Entry(self, width = 30)
        adminIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="Password", fg='black')
        lb2.place(relx = 0.25, rely = 0.25, relheight = 0.08)

        passwordField = Entry(self, width = 30)
        passwordField.place(relx = 0.35, rely = 0.25, relwidth = 0.3, relheight = 0.08)

        button = tk.Button(self, text="Go to page with student registration",
                            command=lambda: self.SignInAdmin(adminIdField.get(), passwordField.get(), controller))
        button.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1)

        from StartPage import StartPage
        button = tk.Button(self, text="Back to start page",
                            command=lambda: controller.show_frame(StartPage))
        button.place(relx = 0.42, rely = 0.5, relheight = 0.08)

    def SignInAdmin(self, id, password, controller):
        db = DatabaseManager()
        try:
            db.VerifyAdmin(id, password)
        except:
            print("error")
        
