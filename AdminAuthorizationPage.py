import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Database.database import *
from Errors.AuthorizationErrors import LoginError, PasswordError, LoginFormatError
# import sys
# import os
# sys.path.append(os.path.abspath('Errors'))
# from AuthorizationErrors import *
from AdminPage import AdminPage

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
        lb2.place(relx = 0.25, rely = 0.3, relheight = 0.08)

        passwordField = Entry(self, width = 30, show='*')
        passwordField.place(relx = 0.35, rely = 0.3, relwidth = 0.3, relheight = 0.08)

        button = tk.Button(self, text="Sing in as admin",
                            command=lambda: self.SignInAdmin(adminIdField.get(), passwordField.get(), controller))
        button.place(relx=0.4, rely=0.45, relwidth=0.25, relheight=0.1)

        from StartPage import StartPage
        button = tk.Button(self, text="<<",
                            command=lambda: controller.show_frame(StartPage))
        button.place(relx = 0.35, rely = 0.45, relheight = 0.1)

    def VerifyLogin(self, id):
        if str.isdigit(id) or id == "":
            return True
        else:
            return False
    def SignInAdmin(self, id, password, controller):
        db = DatabaseManager()
        try:
            db.VerifyAdmin(id, password)
            controller.show_frame(AdminPage)
        except (PasswordError, LoginError) as e:
            print(e)
            error = Label(self, text=e, fg='red')
            error.place(relx = 0.35, rely = 0.39, relheight = 0.05,  anchor="e")
        except LoginFormatError as e:
            error = Label(self, text=e, fg='red')
            error.place(relx = 0.25, rely = 0.30, relheight = 0.05)


        
