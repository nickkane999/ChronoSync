import multiprocessing
import time
import tkinter as tk
from tkinter import messagebox

class GameKeyListener:
    def __init__(self, actor):
        self.actor = actor

    def start_task(self, task_name, info=None):
        print("starting task: " + task_name)
        self.actor.start_macro(task_name, info)

    def start_task_periodic(self):
        self.task_thread1 = None 
        print("Starting periodic task")
        if not self.task_thread1:
            self.task_thread1 = multiprocessing.Process(target=self.actor.start_run, args=(True, 1))
            self.task_thread1.start()

    def start_residue_counter(self):
        print("Starting residue counter task")

    def exit_program(self):
        print("Exiting program early")
        self.task_thread1.terminate()
        self.task_thread1 = None
    
    def processKey(self, event):
        if event.name == '"':
            self.start_task("main_loop")
        elif event.name == "?":
            self.start_task("get_point")
        elif event.name == ">":
            self.start_task("play_wack")
        elif event.name == "<":
            self.start_task("maintenance_loop")
        elif event.name == "]":
            self.start_task("testing")
        elif event.name == ":":
            self.start_task("action_check")
        elif event.name == "|":
            self.start_task("check_point")
        elif event.name == '~':
            print("Triggering macro popup")
            self.show_popup(["Macro Confirmation", "Running macro for farmer against potatoes"], self.start_task_periodic)
            self.cycle_time1 = time.time()

    def main_loop(self):
        print("Main loop running...")

    def show_popup(self, message, function):
        print("showing popup")
        root = tk.Tk()
        result = messagebox.askokcancel(message[0], message[1])
        root.destroy()   # Destroy the root window after the message box is closed

        if result:
            function()
        else:
            print("Cancel button pressed")

    
