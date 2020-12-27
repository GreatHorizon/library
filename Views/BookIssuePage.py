import tkinter as tk
from tkinter import *
from CustomWidets.ComboboxAutocomplete import Combobox_Autocomplete 
from Controllers.BookIssueController import BookIssueController
from tkcalendar import *

class BookIssuePage(tk.Frame):
    def __init__(self, parent, window, model):
        tk.Frame.__init__(self, parent)
        self._model = model
        self._controller = BookIssueController(window, self._model, self)

        label1 = tk.Label(self, text="Book issue")
        label1.pack(pady=20, padx=10)  

        self.create_widgets()
        
    def create_widgets(self):
        label1 = tk.Label(self, text="Select student by id")
        label1.place(relx = 0.25, rely = 0.15, relheight = 0.08)
        userSelect = Combobox_Autocomplete(self, self._controller.GetStudentsId(), highlightthickness=1)
        userSelect.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        userSelect.focus()

        label2 = tk.Label(self, text="Select author")
        label2.place(relx = 0.25, rely = 0.25, relheight = 0.08)
        authorSelect = Combobox_Autocomplete(self, self._controller.GetAuthors(), highlightthickness=1)
        authorSelect.place(relx = 0.38, rely = 0.265, relheight = 0.05, relwidth = 0.25)
        authorSelect.focus()

        label3 = tk.Label(self, text="Select book")
        label3.place(relx = 0.25, rely = 0.35, relheight = 0.08)
        bookSelect = Combobox_Autocomplete(self, self._controller.GetStudentsId(), highlightthickness=1)
        bookSelect.place(relx = 0.38, rely = 0.365, relheight = 0.05, relwidth = 0.25)
        bookSelect.focus()

        label4 = tk.Label(self, text="Select book copy")
        label4.place(relx = 0.25, rely = 0.45, relheight = 0.08)
        copySelect = Combobox_Autocomplete(self, self._controller.GetStudentsId(), highlightthickness=1)
        copySelect.place(relx = 0.38, rely = 0.465, relheight = 0.05, relwidth = 0.25)
        copySelect.focus()

        label4 = tk.Label(self, text="Select book copy")
        label4.place(relx = 0.25, rely = 0.45, relheight = 0.08)
        copySelect = Combobox_Autocomplete(self, self._controller.GetStudentsId(), highlightthickness=1)
        copySelect.place(relx = 0.38, rely = 0.465, relheight = 0.05, relwidth = 0.25)
        copySelect.focus()


        label4 = tk.Label(self, text="Issue start date")
        label4.place(relx = 0.25, rely = 0.54, relheight = 0.08)
        self.startDate = DateEntry(self, date_pattern='dd-mm-y')
        self.startDate.drop_down()
        self.startDate.place(relx = 0.38, rely = 0.55, relheight = 0.05, relwidth = 0.25)


        label4 = tk.Label(self, text="Issue end date")
        label4.place(relx = 0.25, rely = 0.64, relheight = 0.08)
        self.endDate = DateEntry(self, date_pattern='dd-mm-y')
        self.endDate.drop_down()
        self.endDate.place(relx = 0.38, rely = 0.65, relheight = 0.05, relwidth = 0.25)


        button = tk.Button(self, text="Create issue",
            command=lambda:print('hi'))
        button.place(relx=0.4, rely=0.8, relwidth=0.23, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.8, relheight = 0.1)


