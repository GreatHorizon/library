import tkinter as tk
from tkinter import *
from tkinter import messagebox

class AdminAuthorizationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Admin authorization page")
        label.pack(pady=10, padx=10)

        lb1 = Label(self,text="Admin login", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        studentIdField = Entry(self, width = 30)
        studentIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="Password", fg='black')
        lb2.place(relx = 0.25, rely = 0.25, relheight = 0.08)

        passwordField = Entry(self, width = 30)
        passwordField.place(relx = 0.35, rely = 0.25, relwidth = 0.3, relheight = 0.08)

        from StartPage import StartPage
        button = tk.Button(self, text="Back to start page",
                            command=lambda: controller.show_frame(StartPage))
        button.place(relx = 0.42, rely = 0.5, relheight = 0.08)