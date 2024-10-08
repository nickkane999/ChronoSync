import tkinter as tk
from tkinter import ttk
import json
import os

class Data:
    def __init__(self, notebook, file_helper):
        # Create a frame for the Data tab
        # Add JSON file to data
        self.frame = ttk.Frame(notebook, width=400, height=300)
        self.file_helper = file_helper
        self.json_file = self.file_helper.files["tracked_info.json"]

        # Load the tracked info from the JSON file
        # Create input sections for each item in tracked_info
        self.tracked_info = self.load_tracked_info()
        for i, title in enumerate(self.tracked_info.keys()):
            self.create_input_section(title, i)

        # Create a label to display save status
        self.status_label = ttk.Label(self.frame, text="")
        self.status_label.grid(row=len(self.tracked_info), column=0, columnspan=4, pady=10)

    def load_tracked_info(self):
        try:
            with open(self.json_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file is not found, return an empty dictionary
            return {}

    def create_input_section(self, title, row):
        # Title label
        label = ttk.Label(self.frame, text=title)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

        # Get the current value for this title
        current_value = self.tracked_info.get(title, {}).get("time", "None")

        # Display current value label
        current_value_label = ttk.Label(self.frame, text=f"Current value: {current_value}")
        current_value_label.grid(row=row, column=1, padx=10, pady=5, sticky="w")

        # Variable to store the new input
        variable = tk.StringVar(value=current_value)

        # Input box
        entry = ttk.Entry(self.frame, textvariable=variable)
        entry.grid(row=row, column=2, padx=10, pady=5)

        # Save button
        save_button = ttk.Button(self.frame, text="Save", command=lambda: self.save_data(title, variable.get(), current_value_label))
        save_button.grid(row=row, column=3, padx=10, pady=5)

    def save_data(self, title, value, label_to_update):
        # Update the tracked_info with the new value
        if title in self.tracked_info:
            self.tracked_info[title]["time"] = value

        # Save the content to the JSON file
        with open(self.json_file, "w") as file:
            json.dump(self.tracked_info, file, indent=4)

        # Update the current value label
        label_to_update.config(text=f"Current value: {value}")

        # Update the status label
        self.status_label.config(text=f"The content for {title} has been saved.")