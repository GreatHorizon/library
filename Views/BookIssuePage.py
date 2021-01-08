import tkinter as tk
from tkinter import *
from CustomWidets.ComboboxAutocomplete import Combobox_Autocomplete
from Controllers.BookIssueController import BookIssueController
from tkcalendar import *
from tkinter import ttk 

class BookIssuePage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = BookIssueController(master, self._model, self)

        label1 = tk.Label(self, text="Book issue")
        label1.config(font=("Courier", 14))
        label1.pack(pady=20, padx=10)  

        self.create_widgets()
        
    def create_widgets(self):
        label1 = tk.Label(self, text="Select student by id")
        label1.place(relx = 0.25, rely = 0.15, relheight = 0.08)
        self.userSelect = Combobox_Autocomplete(self, searchCallback=self._controller.GetStudentsInfo)
        self.userSelect.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        self.userSelect.focus()


        label2 = tk.Label(self, text="Select author")
        label2.place(relx = 0.25, rely = 0.25, relheight = 0.08)

        self.authorSelect = Combobox_Autocomplete(self, searchCallback=self._controller.GetAuthors,
                                            callbackOnSelection=self._controller.EnableBooksList)
        self.authorSelect.place(relx = 0.38, rely = 0.265, relheight = 0.05, relwidth = 0.25)
        self.authorSelect.focus()

        label3 = tk.Label(self, text="Select book")
        label3.place(relx = 0.25, rely = 0.35, relheight = 0.08)
        self.n1 = tk.StringVar() 
        self.bookSelect = ttk.Combobox(self, width = 27, textvariable = self.n1, state='disabled')
        self.bookSelect.bind("<<ComboboxSelected>>", self._controller.EnableCopiesList)
        self.bookSelect.place(relx = 0.38, rely = 0.365, relheight = 0.05, relwidth = 0.25)

        label4 = tk.Label(self, text="Select book copy")
        label4.place(relx = 0.25, rely = 0.45, relheight = 0.08)
        self.n2 = tk.StringVar() 
        self.copySelect = ttk.Combobox(self, width = 27, textvariable = self.n2, state='disabled')
        self.copySelect.place(relx = 0.38, rely = 0.465, relheight = 0.05, relwidth = 0.25)

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

        self.message = Label(self)
        self.message.place(relx = 0.38, rely = 0.72, relheight = 0.05)


        button = tk.Button(self, text="Create issue",
            command=lambda:self._controller.CreateIssue(self.userSelect.get_value(), self.authorSelect.get_value(),
                                                        self.bookSelect.get(), self.copySelect.get(),
                                                        self.startDate.get(), self.endDate.get()))
        button.place(relx=0.4, rely=0.8, relwidth=0.23, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.8, relheight = 0.1)


    def EnableBooksListAndFillValues(self, values):
        self.bookSelect.configure(state='readonly', values=values)

    def SetSuccessMessage(self, text):
        self.message.config(text=text, fg='green')

    def SetErrorMessage(self, text):
        self.message.config(text=text, fg='red')  
    
    def DisableBooksList(self):
        self.bookSelect.set('')
        self.bookSelect.configure(state='disable', values=[])

    def DisableCopiesList(self):
        self.copySelect.set('')
        self.copySelect.configure(state='disabled', values=[])
  
    def EnableCopiesListAndFillValues(self, values):
        self.copySelect.configure(state='readonly', values=values)

    def ClearMessageLabel(self):
        self.message.config(text='') 

    def ClearFields(self):
        self.userSelect.set_value('')
        self.authorSelect.set_value('')
        self.DisableBooksList()
        self.DisableCopiesList()

    





