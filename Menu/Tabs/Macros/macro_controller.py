import tkinter as tk
from tkinter import ttk
import json
import os
import keyboard  # Import the keyboard module for key listening
from Menu.Scripts.FAPI import Macros as FAPI_Macros


class MacroController:
    def __init__(self, notebook, file_helper):
        self.file_helper = file_helper
        self.frame = ttk.Frame(notebook)
        self.macros = FAPI_Macros.Macros()  # Initialize FAPI_Macros instance

        # Access tasks directly from the FAPI_Macros instance
        self.tasks = self.macros.tasks

        self.files_dir = "Menu/Tabs/Macros/files"
        self.macro_dict = {}
        self.entries = {}
        self.macros_active = False  # Initialize the macros as inactive

        self.folder_var = tk.StringVar()
        self.create_folder_selector()
        self.create_toggle_button()
        self.start_key_listener()  # Start the key listener to handle macros

    def create_folder_selector(self):
        # Dropdown for Folder List
        folder_label = tk.Label(self.frame, text="Select Folder:")
        folder_label.grid(row=0, column=0)

        self.update_folder_list()

        folder_menu = tk.OptionMenu(self.frame, self.folder_var, *self.folders, command=self.change_folder)
        folder_menu.grid(row=0, column=1, columnspan=2)

    def update_folder_list(self):
        self.folders = [f.name for f in os.scandir(self.files_dir) if f.is_dir()]
        if self.folders:
            self.folder_var.set(self.folders[0])
        else:
            self.folder_var.set("")

    def change_folder(self, _):
        # Load macros from the selected folder's macros.json file
        self.load_macros()
        self.create_ui()

    def load_macros(self):
        folder = self.folder_var.get()
        macro_file = os.path.join(self.files_dir, folder, 'macros.json')
        try:
            with open(macro_file, 'r') as file:
                self.macro_dict = json.load(file)
        except FileNotFoundError:
            self.macro_dict = {}

    def save_macros(self):
        folder = self.folder_var.get()
        macro_file = os.path.join(self.files_dir, folder, 'macros.json')
        with open(macro_file, 'w') as file:
            json.dump(self.macro_dict, file, indent=4)

    def create_ui(self):
        # Clear previous entries
        for widget in self.frame.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.grid_forget()

        row = 1
        for key, command in self.macro_dict.items():
            key_label = tk.Label(self.frame, text=f"Key for {command}:")
            key_label.grid(row=row, column=0)

            key_entry = tk.Entry(self.frame)
            key_entry.insert(0, key)
            key_entry.grid(row=row, column=1)

            command_label = tk.Label(self.frame, text="Command:")
            command_label.grid(row=row, column=2)

            command_var = tk.StringVar(value=command)
            command_menu = tk.OptionMenu(self.frame, command_var, *self.tasks.keys())
            command_menu.grid(row=row, column=3)

            self.entries[key] = (key_entry, command_var)
            row += 1

        # Save Button
        self.save_button = tk.Button(self.frame, text="Save Macros", command=self.update_macros)
        self.save_button.grid(row=row, column=0, columnspan=4)

        # Status Label
        self.status_label = tk.Label(self.frame, text="")
        self.status_label.grid(row=row + 1, column=0, columnspan=4)

    def create_toggle_button(self):
        # Toggle button for enabling/disabling macros
        self.toggle_button = tk.Button(self.frame, text="Enable Macros", command=self.toggle_macros)
        self.toggle_button.grid(row=0, column=4)

    def toggle_macros(self):
        # Toggle the macro active state
        self.macros_active = not self.macros_active
        button_text = "Disable Macros" if self.macros_active else "Enable Macros"
        self.toggle_button.config(text=button_text)
        status = "active" if self.macros_active else "inactive"
        self.status_label.config(text=f"Macros are now {status}.")

    def update_macros(self):
        new_macro_dict = {}
        for old_key, (key_entry, command_var) in self.entries.items():
            new_key = key_entry.get()
            command_name = command_var.get()
            if new_key and command_name:
                new_macro_dict[new_key] = command_name
        self.macro_dict = new_macro_dict
        self.save_macros()
        self.status_label.config(text="Macros updated!")

    def start_key_listener(self):
        # Start listening for key events
        keyboard.on_press(self.process_key)

    def process_key(self, event):
        if not self.macros_active:
            return  # Do nothing if macros are disabled

        key = event.name
        if key in self.macro_dict:
            command_name = self.macro_dict[key]
            command_func = self.tasks.get(command_name)
            if command_func:
                command_func()

