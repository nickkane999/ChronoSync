import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import json
import os

class Timers:
    def __init__(self, notebook):
        # Create a frame for the Timers tab
        # Dictionary to store timer labels, threads, and buttons
        # And load the JSON file
        self.frame = ttk.Frame(notebook, width=400, height=300)
        self.timer_labels = {}
        self.timer_threads = {}
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.json_file = os.path.join(parent_dir, "tracked_info.json")

        # Create timer sections for each category in the JSON file
        self.create_timer_sections()

    def create_timer_sections(self):
        # Remove existing timer sections and buttons
        # Reload current values
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.load_current_values()

        # Create timer sections for each item within each category in the JSON file
        row_position = 0
        for category, items in self.current_values.items():
            category_label = ttk.Label(self.frame, text=category, font=("Arial", 12, "bold"))
            category_label.grid(row=row_position, column=0, columnspan=4, padx=10, pady=5, sticky="w")
            row_position += 1

            # Add timer for each title item in the category
            for title, data in items.items():
                self.create_timer_section(title, row_position, data)
                row_position += 1

        # Add the Refresh Timers button
        refresh_button = ttk.Button(self.frame, text="Refresh Timers", command=self.refresh_timers)
        refresh_button.grid(row=row_position, column=0, columnspan=4, pady=10)

    def create_timer_section(self, title, row, data):
        print(f"Creating timer section for '{title}' at row {row}")
        # Title label
        label = ttk.Label(self.frame, text=title)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

        # Countdown value label
        # Store the label for use in the timer thread
        countdown_minutes = int(data.get("time", "0"))
        countdown_label = ttk.Label(self.frame, text=self.format_time(countdown_minutes))
        countdown_label.grid(row=row, column=3, padx=10, pady=5, sticky="w")
        self.timer_labels[title] = countdown_label

        # Create and store the Start timer button and Refresh timer button
        start_button = ttk.Button(self.frame, text="Start timer", command=lambda t=title: self.start_timer(t, data))
        start_button.grid(row=row, column=1, padx=10, pady=5)
        refresh_button = ttk.Button(self.frame, text="Refresh timer", command=lambda t=title: self.refresh_timer(t, row))
        refresh_button.grid(row=row, column=2, padx=10, pady=5)

    def format_time(self, minutes):
        # Convert minutes to hours, minutes, and seconds
        total_seconds = minutes * 60
        hours, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours}h {mins}m {secs}s"

    def load_current_values(self, key=None):
        if not key:
            self.current_values = {}
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
                if key:
                    category = data.get(key, {}).get("category", "Uncategorized")
                    self.current_values[category][key] = data.get(key, {})
                else:
                    for title, info in data.items():
                        category = info.get("category", "Uncategorized")
                        if category not in self.current_values:
                            self.current_values[category] = {}
                        self.current_values[category][title] = info
        except FileNotFoundError:
            pass
        return category

    def refresh_timer(self, title, row):
        # Stop the timer for the selected title
        # Reload the current value for this title
        # Recreate the timer section with updated values
        print(f"Refreshing timer for '{title}' at row {row}")
        self.stop_single_timer(title)
        category = self.load_current_values(title)
        data = self.current_values[category][title]
        self.create_timer_section(title, row, data)

    def refresh_timers(self):
        # Stop all active timers
        # Load current countdown values from the JSON file
        # Recreate timer sections with updated values
        self.stop_all_timers()
        self.load_current_values()
        self.create_timer_sections()

    def start_timer(self, title, data):
        # Check if there is already an active timer thread for this title
        if title in self.timer_threads and self.timer_threads[title] is not None:
            print(f"Timer for '{title}' is already running.")
            return  # Exit the method to prevent starting a new timer thread


        # Get the countdown minutes for the selected title
        minutes = int(self.current_values.get(data.get("category", {}), {}).get(title, {}).get("time", "0"))

        # Define a flag to stop the timer
        stop_event = threading.Event()
        self.timer_threads[title] = stop_event

        def countdown():
            total_seconds = minutes * 60
            while total_seconds > 0 and not stop_event.is_set():
                hours, remainder = divmod(total_seconds, 3600)
                mins, secs = divmod(remainder, 60)
                time_str = f"{hours}h {mins}m {secs}s"
                self.timer_labels[title].config(text=time_str)
                time.sleep(1)
                total_seconds -= 1

            if not stop_event.is_set():
                # Timer finished
                self.timer_labels[title].config(text="0h 0m 0s")
                messagebox.showinfo("Timer Finished", f"{title} has finished")

        # Start the countdown in a new thread
        timer_thread = threading.Thread(target=countdown)
        timer_thread.start()

    def stop_all_timers(self):
        # Signal all timer threads to stop
        for title, stop_event in self.timer_threads.items():
            print(f"Stopping timer for '{title}' with stop_event: {stop_event}")
            if stop_event is not None:
                stop_event.set()
        self.timer_threads.clear()

    def stop_single_timer(self, stopped_title):
        # Signal the specific timer thread to stop
        if stopped_title in self.timer_threads:
            stop_event = self.timer_threads[stopped_title]
            if stop_event is not None:
                stop_event.set()
                del self.timer_threads[stopped_title]
