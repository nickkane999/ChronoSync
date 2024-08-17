import tkinter as tk
from tkinter import ttk, messagebox

class TimerUI:
    def __init__(self, frame, controller):
        self.frame = frame
        self.controller = controller
        self.timer_labels = {}

    def create_timer_sections(self, current_values):
        # Remove existing timer sections and buttons
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Create timer sections for each item within each category in the JSON file
        row_position = 0
        for category, items in current_values.items():
            category_label = ttk.Label(self.frame, text=category, font=("Arial", 12, "bold"))
            category_label.grid(row=row_position, column=0, columnspan=4, padx=10, pady=5, sticky="w")
            row_position += 1

            for title, data in items.items():
                print(f"Creating timer section for '{title}' at row '{row_position}' with data: '{data}'")
                self.create_timer_section(title, row_position, data)
                row_position += 1

        refresh_button = ttk.Button(self.frame, text="Refresh Timers", command=self.controller.refresh_timers)
        refresh_button.grid(row=row_position, column=0, columnspan=4, pady=10)

    def create_timer_section(self, title, row, data):
        label = ttk.Label(self.frame, text=title)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

        countdown_minutes = int(data.get("time", "0"))
        countdown_label = ttk.Label(self.frame, text=self.controller.format_time(countdown_minutes))
        countdown_label.grid(row=row, column=3, padx=10, pady=5, sticky="w")
        self.timer_labels[title] = countdown_label

        start_button = ttk.Button(self.frame, text="Start timer", command=lambda t=title: self.controller.start_timer(t, data))
        start_button.grid(row=row, column=1, padx=10, pady=5)

        refresh_button = ttk.Button(self.frame, text="Refresh timer", command=lambda t=title: self.controller.refresh_timer(t, row))
        refresh_button.grid(row=row, column=2, padx=10, pady=5)

    def update_timer_label(self, title, text):
        if title in self.timer_labels:
            self.timer_labels[title].config(text=text)
