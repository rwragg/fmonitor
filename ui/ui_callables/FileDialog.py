from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class FileDialog(object):
    def __init__(self):
        print("constructing")

    def __call__(self):
        name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file.")

        return name
        # Using try in case user types in unknown file or closes without choosing a file.
        # try:
        #     with open(name, 'r') as UseFile:
        #         print(UseFile.read())
        # except:
        #     print("No file exists")
