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
        self.MakeEditCopyOfBookTab()

    def MakeEditCopyOfBookTab(self):
        label = tk.Label(self.tab2, text="Edit copy of book page")
        label.pack(pady=10, padx=10)

        label2 = tk.Label(self.tab2, text="Select author")
        label2.place(relx = 0.25, rely = 0.155, relheight = 0.08)

        self.authorSelectTab2 = Combobox_Autocomplete(self.tab2, searchCallback=self._controller.GetAuthors,
                                callbackOnSelection=self._controller.EnableBooksListTab2)
        self.authorSelectTab2.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        self.authorSelectTab2.focus()

        label3 = tk.Label(self.tab2, text="Select book")
        label3.place(relx = 0.25, rely = 0.255, relheight = 0.08)
        self.nTab2 = tk.StringVar() 
        self.bookSelectTab2 = ttk.Combobox(self.tab2, width = 27, textvariable = self.nTab2, state='disabled')
        self.bookSelectTab2.bind("<<ComboboxSelected>>", self._controller.EnableCopiesListTab2)
        self.bookSelectTab2.place(relx = 0.38, rely = 0.265, relheight = 0.05, relwidth = 0.25)

        label4 = tk.Label(self.tab2, text="Select book copy")
        label4.place(relx = 0.25, rely = 0.355, relheight = 0.08)
        self.nTab2 = tk.StringVar() 
        self.copySelectTab2 = ttk.Combobox(self.tab2, width = 27, textvariable = self.nTab2, state='disabled')
        self.copySelectTab2.bind("<<ComboboxSelected>>", self._controller.GetCopyInfo)
        self.copySelectTab2.place(relx = 0.38, rely = 0.365, relheight = 0.05, relwidth = 0.25)


        label4 = tk.Label(self.tab2, text="New pages count")
        label4.place(relx = 0.25, rely = 0.445, relheight = 0.08)
        
        self.newPagesCountEntry = Entry(self.tab2, width = 27, state='disable')
        self.newPagesCountEntry.place(relx = 0.38, rely = 0.465, relheight = 0.05, relwidth = 0.25)

        label5 = tk.Label(self.tab2, text="New publisher new")
        label5.place(relx = 0.25, rely = 0.545, relheight = 0.08)
        self.newPublisherNameEntry = Entry(self.tab2, width = 27, state='disable')
        self.newPublisherNameEntry.place(relx = 0.38, rely = 0.565, relheight = 0.05, relwidth = 0.25)

        self.messageTab2 = Label(self.tab2, text='', fg='red')
        self.messageTab2.place(relx = 0.38, rely = 0.625, relheight = 0.05)
        
        backButton = tk.Button(self.tab2, text="Edit book copy",
                            command=lambda:self._controller.EditBookCopy(self.nTab2.get(), self.newPagesCountEntry.get(), self.newPublisherNameEntry.get()))
        backButton.place(relx=0.435, rely=0.7, relwidth=0.2, relheight=0.1)

        backButton = tk.Button(self.tab2, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        backButton.place(relx = 0.38, rely = 0.7, relheight = 0.1)


    def MakeEditBookTab(self):
        label = tk.Label(self.tab1, text="Edit book page")
        label.pack(pady=10, padx=10)

        label2 = tk.Label(self.tab1, text="Select author")
        label2.place(relx = 0.25, rely = 0.155, relheight = 0.08)

        self.authorSelectTab1 = Combobox_Autocomplete(self.tab1, searchCallback= self._controller.GetAuthors,
                                            callbackOnSelection=self._controller.EnableBooksListTab1)
        self.authorSelectTab1.place(relx = 0.38, rely = 0.165, relheight = 0.05, relwidth = 0.25)
        self.authorSelectTab1.focus()

        label3 = tk.Label(self.tab1, text="Select book")
        label3.place(relx = 0.25, rely = 0.255, relheight = 0.08)
        self.nTab1 = tk.StringVar() 
        self.bookSelectTab1 = ttk.Combobox(self.tab1, width = 27, textvariable = self.nTab1, state='disabled')
        self.bookSelectTab1.bind("<<ComboboxSelected>>", lambda bookName: self._controller.EnableNewNamesFieldsWithValues(self.authorSelectTab1.get_value(), self.nTab1.get()))
        self.bookSelectTab1.place(relx = 0.38, rely = 0.265, relheight = 0.05, relwidth = 0.25)

        label4 = tk.Label(self.tab1, text="New author name")
        label4.place(relx = 0.25, rely = 0.345, relheight = 0.08)
        
        self.newAuthorNameEntry = Entry(self.tab1, width = 27, state='disable')
        self.newAuthorNameEntry.place(relx = 0.38, rely = 0.365, relheight = 0.05, relwidth = 0.25)

        label5 = tk.Label(self.tab1, text="New book name")
        label5.place(relx = 0.25, rely = 0.445, relheight = 0.08)
        self.newBookNameEntry = Entry(self.tab1, width = 27, state='disable')
        self.newBookNameEntry.place(relx = 0.38, rely = 0.455, relheight = 0.05, relwidth = 0.25)

        self.messageTab1 = Label(self.tab1, text='', fg='red')
        self.messageTab1.place(relx = 0.38, rely = 0.525, relheight = 0.05)

        editBookTab1 = tk.Button(self.tab1, text="Edit book",
                            command=lambda:self._controller.EditBook(self.newAuthorNameEntry.get(), self.authorSelectTab1.get_value(), self.newBookNameEntry.get(), self.nTab1.get()))
        editBookTab1.place(relx=0.435, rely=0.6, relwidth=0.2, relheight=0.1)

        backButton = tk.Button(self.tab1, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        backButton.place(relx = 0.38, rely = 0.6, relheight = 0.1)

    def SetMessageLabelTab1(self, message, color):
        self.messageTab1.config(text=message, fg=color)

    def DisableBooksListTab1(self):
        self.bookSelectTab1.set('')
        self.bookSelectTab1.configure(state='disable', values=[])

    def DisableFieldsTab1(self):
        self.newBookNameEntry.config(state='disable')
        self.newAuthorNameEntry.config(state='disable')

    def EnableBooksListAndFillValuesTab1(self, values):
        self.bookSelectTab1.configure(state='readonly', values=values)
     
    def EnableNewBookNameEntryWithTextTab1(self, text):
        self.newBookNameEntry.delete(0, tk.END)
        self.newBookNameEntry.config(state='normal')
        self.newBookNameEntry.insert(0, text)

    def EnableNewAuthorNameEntryWithTextTab1(self, text):
        self.newAuthorNameEntry.delete(0, tk.END)
        self.newAuthorNameEntry.config(state='normal')
        self.newAuthorNameEntry.insert(0, text)

    def ClearEntryFieldsTab1(self):
        self.newAuthorNameEntry.delete(0, tk.END)
        self.newBookNameEntry.delete(0, tk.END)

    def ClearAllFieldsTab1(self):
        self.newAuthorNameEntry.delete(0, tk.END)
        self.newBookNameEntry.delete(0, tk.END)
        self.DisableBooksListTab1()
        self.authorSelectTab1.set_value('')

    def SetMessageLabelTab2(self, message, color):
        self.messageTab2.config(text=message, fg=color)

    def DisableBooksListTab2(self):
        self.bookSelectTab2.set('')
        self.bookSelectTab2.configure(state='disable', values=[])

    def EnableBooksListAndFillValuesTab2(self, values):
        self.bookSelectTab2.configure(state='readonly', values=values)

    def EnableCopiesListAndFillValuesTab2(self, values):
        self.copySelectTab2.config(state='readonly', values=values)

    def DisableCopiesListTab2(self):
        self.copySelectTab2.set('')
        self.copySelectTab2.config(state='disable', values=[])


    def ClearEntryFieldsTab2(self):
        self.newPagesCountEntry.delete(0, tk.END)
        self.newPublisherNameEntry.delete(0, tk.END)


    def EnableNewPagesEntryTab2(self, text):
        self.newPagesCountEntry.delete(0, tk.END)
        self.newPagesCountEntry.config(state='normal')
        self.newPagesCountEntry.insert(0, text)

    def EnableNewPublisherNameEntryTab2(self, text):
        self.newPublisherNameEntry.delete(0, tk.END)
        self.newPublisherNameEntry.config(state='normal')
        self.newPublisherNameEntry.insert(0, text)

    def DisableFieldsTab1(self):
        self.newPagesCountEntry.config(state='disable')
        self.newPublisherNameEntry.config(state='disable')

    def ClearAllFieldsTab2(self):
        self.newPagesCountEntry.delete(0, tk.END)
        self.newPublisherNameEntry.delete(0, tk.END)
        self.DisableBooksListTab2()
        self.authorSelectTab2.set_value('')
        self.DisableCopiesListTab2()

