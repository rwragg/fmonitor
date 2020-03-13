# Simple enough, just import everything from tkinter.
from tkinter import *
from ui import *


class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        super().__init__(master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Visual Grep")
        self.master.option_add('*tearOff', False)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menubar = MenuBar(self.master)


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")

    # creation of an instance
    app = Window(root)

    # mainloop
    root.mainloop()