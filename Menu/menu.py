import tkinter as tk
from tkinter import ttk
from Menu.Tabs.data import Data
from Menu.Tabs.timers import Timers

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabbed Interface with Classes")

        # Create a notebook (tabs container)
        self.notebook = ttk.Notebook(self.root)

        # Create instances of Data and Timers
        self.data_tab = Data(self.notebook)
        self.timers_tab = Timers(self.notebook)

        # Add the frames to the notebook
        self.notebook.add(self.data_tab.frame, text="Data")
        self.notebook.add(self.timers_tab.frame, text="Timers")

        # Pack the notebook to make it visible
        self.notebook.pack(expand=True, fill="both")