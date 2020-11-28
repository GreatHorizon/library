# import sys
# import os
# sys.path.append(os.path.abspath('Views'))
from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.StudentAuthorizationPage import StudentAuthorizationPage


class StartPageController:
    def __init__(self, window, model, view):
        self._view = view
        self._window = window
        self._model = model

    def openAdminAuthorizationPage(self):
        self._window.show_frame(AdminAuthorizationPage)
    
    def openStudentAuthorizationPage(self):
        self._window.show_frame(StudentAuthorizationPage)