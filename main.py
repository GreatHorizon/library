import tkinter as tk
from tkinter import *
from datetime import datetime, date, time, timezone


from Views.StartPage import StartPage
from Models.StartPageModel import StartPageModel


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._frame = None
        self.title("library")

        tk.Tk.geometry(self,'900x400') 

        self.switch_frame(StartPage, StartPageModel)

    def switch_frame(self, frame_class, model, *data):
        self._model = model()
        if (len(data) != 0):
            print(data)
            self._model.Save(data) 
        new_frame = frame_class(self, self._model)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(side="top", fill="both", expand = True)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)


app = Window()
app.mainloop()