import pyautogui
import time
import pydirectinput

class Macros:
    # Initializing Object
    def __init__(self):
        self.tasks = self.get_tasks()

    def get_tasks(self):
        tasks = {
            "gc_speed_up": self.gc_speed_up,
            "gc_slow_down": self.gc_slow_down
        }
        return tasks
    
    def gc_speed_up(self):
        print("Speeding up")
        pydirectinput.keyDown('shift')
        for x in range(5):
            pydirectinput.keyDown('=')
            pydirectinput.keyUp('=')
        pydirectinput.keyUp('shift')

    def gc_slow_down(self):
        print("Slowing up")
        pydirectinput.keyDown('shift')
        for x in range(5):
            pydirectinput.keyDown('-')
            pydirectinput.keyUp('-')
        pydirectinput.keyUp('shift')
