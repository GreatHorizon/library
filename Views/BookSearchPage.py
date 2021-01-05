import tkinter as tk
from tkinter import *
from Controllers.BookSearchController import BookSearchController
from ttkwidgets import Table
from tkinter import ttk

class BookSearchPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = BookSearchController(master, self._model, self)
        self._model.Register(self)
        labelFrame = Frame(self,bg='black')

        issuanceList = []
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        label1 = tk.Label(self, text="Search by")
        label1.place(relx = 0.30, rely = 0.09, relheight = 0.08)
        self.bookSelect = ttk.Combobox(self, width = 27, values=["Book name", "Author"])

        # self.bookSelect.bind("<<ComboboxSelected>>", self._controller.EnableCopiesList)
        self.bookSelect.place(relx = 0.38, rely = 0.10, relheight = 0.05, relwidth = 0.25)

        columns = ["Author name", "Book name", "Id copy", "Start", "End"]
        table = Table(labelFrame, columns=columns, sortable=False, drag_cols=False, drag_rows=False)
        
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=140, stretch=True)

        for i in range(len(issuanceList)):
            table.insert('', 'end', iid=i,
                        values=(issuanceList[i][2], issuanceList[i][1], issuanceList[i][0], issuanceList[i][3], issuanceList[i][4]))

        # add scrollbars
        sx = tk.Scrollbar(labelFrame, orient='horizontal', command=table.xview)
        sy = tk.Scrollbar(labelFrame, orient='vertical', command=table.yview)
        table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        table.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')

        button = tk.Button(self, text="Back",
            command=lambda:self._controller.BackToStudentPage())
        button.place(relx=0.4, rely=0.80, relwidth=0.25, relheight=0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        pass

    # def ClearFields(self):
    #     self.oldPassField.delete(0, len(self.oldPassField.get()))
    #     self.newPassField.delete(0, len(self.newPassField.get()))
    #     self.confirmPassField.delete(0, len(self.confirmPassField.get()))
    
    # def ClearMessageLabel(self):
    #     self.message.config(text='')
