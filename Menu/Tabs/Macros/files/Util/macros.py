import pyautogui
import time
import keyboard

class Macros:
    def __init__(self):
        self.tasks = self.get_tasks()
        self.info = self.get_info()

    def get_tasks(self):
        tasks = {
            "get_point": self.get_point,
            "check_point": self.check_point,
            "testing": self.testing,
            "click_loop": self.click_loop,  # Add the click_loop task here
        }
        return tasks

    def get_info(self):
        info = {
            "send_10_gems": (0, 0),
            "bomb_all_waves": (0, 0),
        }
        return info

    def get_point(self):
        x = 0
        while x < 1:
            print(pyautogui.position())
            x += 1

    def check_point(self):
        point = pyautogui.position()
        print(point)
        print(pyautogui.pixel(*point))

    def testing(self):
        print("Testing")

    def click_loop(self):
        print("Starting click loop. Press F1 to stop.")
        time.sleep(0.3)
        while True:
            pyautogui.click()
            if keyboard.is_pressed('F1'):
                print("Stopping click loop.")
                break
