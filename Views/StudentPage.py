import tkinter as tk
from tkinter import *
from Controllers.StudentPageController import StudentPageController
import sys
import os
sys.path.append(os.path.abspath('images'))

class StudentPage(tk.Frame):
    def __init__(self, parent, window, model):
        tk.Frame.__init__(self, parent)
        self._model = model
        self._controller = StudentPageController(window, self._model, self)

        label1 = tk.Label(self, text="Student Page")
        label1.pack(pady=20, padx=20)  


        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToStudentAuthorizationPage())
        button.place(relx=0.4, rely=0.85, relwidth=0.2,relheight=0.1)