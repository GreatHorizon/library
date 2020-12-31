import tkinter as tk
from tkinter import *
from Controllers.BookSearchController import  

class BookSearchPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = BookSearchController(master, self._model, self)
        self._model.Register(self)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        if (self._model._isChanged):
            self.ClearFields()
            self.SetMessageLabel(self._model._message, 'green')
        else:
            self.SetMessageLabel(self._model._message, 'red')

    def ClearFields(self):
        self.oldPassField.delete(0, len(self.oldPassField.get()))
        self.newPassField.delete(0, len(self.newPassField.get()))
        self.confirmPassField.delete(0, len(self.confirmPassField.get()))
    
    def ClearMessageLabel(self):
        self.message.config(text='')
