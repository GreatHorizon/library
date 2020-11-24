import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime, date, time, timezone
from RegisterNewUser import *
from AdminAuthorizationPage import AdminAuthorizationPage
from StudentAuthorizationPage import StudentAuthorizationPage
from StartPage import StartPage
from AdminPage import AdminPage

import psycopg2

class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("library")

        tk.Tk.geometry(self,'900x400') 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage
                , StudentAuthorizationPage
                , AdminAuthorizationPage
                , AdminPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


app = Window()
app.mainloop()