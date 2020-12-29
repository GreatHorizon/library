import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkwidgets import Table
import psycopg2
# from Database.database import *
from Controllers.StudentIssuancePageController import StudentIssuancePageController

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class StudentIssuancePage(tk.Frame):

    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = StudentIssuancePageController(master, self._model, self)
        self._model.Register(self)
                
        issuanceList = self._controller.GetStudentIssuance()

        labelFrame = Frame(self,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

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
            
    # def Notify(self):
    #     if (self._model._isAuthorizated):
    #         self._controller.SendData(id=self._model._userId)
    #         self._controller.OpenStudentPage()
    #         self.ClearErrorLabel()
    #     else:
    #         self.error.config(text=self._model._message)
    #     self.ClearFields()

    # def ClearFields(self):
    #     self.studentIdField.delete(0, len(self.studentIdField.get()))
    #     self.passwordField.delete(0, len(self.passwordField.get()))

    # def ClearErrorLabel(self):
    #     self.error.config(text='') 

    def updateView(self) :
        self._controller.GetStudentIssuance(self.id)

    def recieve_data(self, **data):
        self.id = data['id']
