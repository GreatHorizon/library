import tkinter as tk
from tkinter import *

from Controllers.StartPageController import StartPageController

class StartPage(tk.Frame):
    
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._controller = StartPageController(master, model, self)
        
        label1 = tk.Label(self, text="Start Page")
        label1.pack(pady=20,padx=20)

        label2 = tk.Label(self, text="Connect as:")
        label2.pack(pady=40,padx=40)

        button = tk.Button(self, text="Admin",
                            command=lambda:self._controller.openAdminAuthorizationPage())
        button.place(relx = 0.25, rely = 0.55, relheight = 0.08)

        button2 = tk.Button(self, text="Student",
                            command=lambda:self._controller.openStudentAuthorizationPage())
        button2.place(relx = 0.75, rely = 0.55, relheight = 0.08)
        
