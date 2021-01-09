import tkinter as tk
from tkinter import *
from Controllers.EditBookController import EditBookController
from CustomWidets.ComboboxAutocomplete import Combobox_Autocomplete
from tkinter import ttk 

class EditBookPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = EditBookController(master, self._model, self)

        tabControl = ttk.Notebook(self) 
  
        self.tab1 = ttk.Frame(tabControl) 
        self.tab2 = ttk.Frame(tabControl) 

        tabControl.add(self.tab1, text ='Edit book') 
        tabControl.add(self.tab2, text ='Edit copy of book') 
        tabControl.pack(expand = 1, fill ="both") 

        self.MakeEditBookTab()


    def MakeEditBookTab(self):
        label = tk.Label(self.tab1, text="Edit book page")
        label.pack(pady=10, padx=10)

        label2 = tk.Label(self.tab1, text="Select author")
        label2.place(relx = 0.25, rely = 0.155, relheight = 0.08)

        self.authorSelect = Combobox_Autocomplete(self.tab1, searchCallback=self._controller.GetAuthors,
                                            callbackOnSelection=self._controller.EnableBooksList)
        self.authorSelect.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        self.authorSelect.focus()

        label3 = tk.Label(self.tab1, text="Select book")
        label3.place(relx = 0.25, rely = 0.255, relheight = 0.08)
        self.n1 = tk.StringVar() 
        self.bookSelect = ttk.Combobox(self.tab1, width = 27, textvariable = self.n1, state='disabled')
        self.bookSelect.bind("<<ComboboxSelected>>", lambda bookName: self._controller.EnableNewNamesFieldsWithValues(self.authorSelect.get_value(), self.n1.get()))
        self.bookSelect.place(relx = 0.38, rely = 0.265, relheight = 0.05, relwidth = 0.25)

        label4 = tk.Label(self.tab1, text="New author name")
        label4.place(relx = 0.25, rely = 0.345, relheight = 0.08)
        
        self.newAuthorNameEntry = Entry(self.tab1, width = 27, state='disable')
        self.newAuthorNameEntry.place(relx = 0.38, rely = 0.365, relheight = 0.05, relwidth = 0.25)

        label4 = tk.Label(self.tab1, text="New book name")
        label4.place(relx = 0.25, rely = 0.445, relheight = 0.08)
        self.newBookNameEntry = Entry(self, width = 27, state='disable')
        self.newBookNameEntry.place(relx = 0.38, rely = 0.485, relheight = 0.05, relwidth = 0.25)

        self.message = Label(self.tab1, text='', fg='red')
        self.message.place(relx = 0.38, rely = 0.525, relheight = 0.05)

        backButton = tk.Button(self.tab1, text="Edit book",
                            command=lambda:self._controller.EditBook(self.newAuthorNameEntry.get(), self.authorSelect.get_value(), self.newBookNameEntry.get(), self.n1.get()))
        backButton.place(relx=0.435, rely=0.6, relwidth=0.2, relheight=0.1)

        backButton = tk.Button(self.tab1, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        backButton.place(relx = 0.38, rely = 0.6, relheight = 0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def DisableBooksList(self):
        self.bookSelect.set('')
        self.bookSelect.configure(state='disable', values=[])

    def DisableFields(self):
        self.newBookNameEntry.config(state='disable')
        self.newAuthorNameEntry.config(state='disable')

    def EnableBooksListAndFillValues(self, values):
        self.bookSelect.configure(state='readonly', values=values)
     
    def EnableNewBookNameEntryWithText(self, text):
        self.newBookNameEntry.delete(0, tk.END)
        self.newBookNameEntry.config(state='normal')
        self.newBookNameEntry.insert(0, text)

    def EnableNewAuthorNameEntryWithText(self, text):
        self.newAuthorNameEntry.delete(0, tk.END)
        self.newAuthorNameEntry.config(state='normal')
        self.newAuthorNameEntry.insert(0, text)

    def ClearEntryFields(self):
        self.newAuthorNameEntry.delete(0, tk.END)
        self.newBookNameEntry.delete(0, tk.END)

    def ClearAllFields(self):
        self.newAuthorNameEntry.delete(0, tk.END)
        self.newBookNameEntry.delete(0, tk.END)
        self.DisableBooksList()
        self.authorSelect.set_value('')

