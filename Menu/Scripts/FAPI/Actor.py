import pyautogui
import time
import math
import copy

pyautogui.PAUSE = 0.03

class Actor:
    def __init__(self, macros):
        self.macros = macros

    # Primary functions
    def start_macro(self, task_name, info = None):
        self.macros.tasks[task_name](info)

    # Utility functions
    def select(self, point):
        pyautogui.click(point[0], point[1])
    
    def is_color_match(self, color1, color2):
        threshold = 30
        return self.color_distance(color1, color2) < threshold

    def color_distance(self, color1, color2):
        return math.sqrt(sum([(x - y) ** 2 for x, y in zip(color1, color2)]))