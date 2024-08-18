import tkinter as tk
from tkinter import ttk
from Menu.Util.file_helper import FileHelper
from Menu.Tabs.Data.data import Data
from Menu.Tabs.Timer.timer_controller import TimerController
from Menu.Tabs.Macros.macro_controller import MacroController  # Import the new MacroController class

class Menu:
    def __init__(self, root):
        # Create a UI with tabs
        self.root = root
        self.root.title("Tabbed Interface with Classes")
        self.notebook = ttk.Notebook(self.root)
        file_helper = FileHelper()

        # Create instances of Data, TimerController, and MacroController
        self.data_tab = Data(self.notebook, file_helper)
        self.timers_tab = TimerController(self.notebook, file_helper)
        self.macros_tab = MacroController(self.notebook, file_helper)  # Instantiate MacroController

        # Add the frames to the notebook
        self.notebook.add(self.data_tab.frame, text="Data")
        self.notebook.add(self.timers_tab.frame, text="Timers")
        self.notebook.add(self.macros_tab.frame, text="Macros")  # Add MacroController tab
        self.notebook.pack(expand=True, fill="both")