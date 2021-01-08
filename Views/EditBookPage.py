import tkinter as tk
from tkinter import *
from Controllers.EditBookController import EditBookController

class EditBookPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = EditBookController(master, self._model, self)

        label = tk.Label(self, text="Edit book page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.6, relheight = 0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)


