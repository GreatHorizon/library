import tkinter as tk
from tkinter import *

from Controllers.StudentDebtsController import StudentDebtsController

class StudentDebtsPage(tk.Frame):
    
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._controller = StudentDebtsController(master, model, self)
        
        label1 = tk.Label(self, text="Student debts page")
        label1.pack(pady=20,padx=20)



        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.85, relheight = 0.1)
