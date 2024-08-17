import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from Menu.Tabs.Timer.timer_data_manager import TimerDataManager
from Menu.Tabs.Timer.timer_ui import TimerUI

class TimerController:
    def __init__(self, notebook):
        # Create Frame for Timer tab
        # Create TimerDataManager and TimerUI dependent class instances
        # Create dictionary to store timer threads
        self.frame = ttk.Frame(notebook, width=400, height=300)
        self.data_manager = TimerDataManager()
        self.ui = TimerUI(self.frame, self)
        self.timer_threads = {}

        # Load current values and create timer sections
        data = self.data_manager.load_current_values()
        #print(f"Loaded current values: {data}")
        self.ui.create_timer_sections(data)

    def format_time(self, minutes):
        total_seconds = minutes * 60
        hours, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours}h {mins}m {secs}s"

    def refresh_timer(self, title, row):
        self.stop_single_timer(title)
        data = self.data_manager.load_current_values(title)
        category = next(iter(data))
        formatted_data = data[category][title]
        print("data, key, and formatted_data: ", data, category, formatted_data)
        self.ui.create_timer_section(title, row, formatted_data)

    def refresh_timers(self):
        self.stop_all_timers()
        self.data_manager.load_current_values()
        self.ui.create_timer_sections(self.data_manager.get_current_values())

    def start_timer(self, title, data):
        if title in self.timer_threads and self.timer_threads[title] is not None:
            print(f"Timer for '{title}' is already running.")
            return
        values = self.data_manager.get_current_values()
        category = data["category"]
        print(f"Values: {values} Category: {category} Title: {title}")

        minutes = int(values[category][title].get("time", "0"))

        stop_event = threading.Event()
        self.timer_threads[title] = stop_event

        def countdown():
            total_seconds = minutes * 60
            while total_seconds > 0 and not stop_event.is_set():
                hours, remainder = divmod(total_seconds, 3600)
                mins, secs = divmod(remainder, 60)
                time_str = f"{hours}h {mins}m {secs}s"
                self.ui.timer_labels[title].config(text=time_str)
                time.sleep(1)
                total_seconds -= 1

            if not stop_event.is_set():
                # Timer finished
                self.ui.timer_labels[title].config(text="0h 0m 0s")
                messagebox.showinfo("Timer Finished", f"{title} has finished")

        # Start the countdown in a new thread
        timer_thread = threading.Thread(target=countdown)
        timer_thread.start()

    def stop_all_timers(self):
        for title, stop_event in self.timer_threads.items():
            print(f"Stopping timer for '{title}' with stop_event: {stop_event}")
            if stop_event is not None:
                stop_event.set()
        self.timer_threads.clear()

    def stop_single_timer(self, stopped_title):
        if stopped_title in self.timer_threads:
            stop_event = self.timer_threads[stopped_title]
            if stop_event is not None:
                stop_event.set()
                del self.timer_threads[stopped_title]