from tkinter import *
from .ui_callables import *


class MenuBar(object):
    def __init__(self, master):
        self.__master = master

        self.__fdialog: FileDialog = FileDialog()
        self.fname: str = ""

        menu = Menu(self.__master)
        self.__master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Open", command=self.open_file)
        file.add_command(label="Exit", command=self.__master.quit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

    def open_file(self):
        self.fname = self.__fdialog()

    # region properties
    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname
    # endregion
