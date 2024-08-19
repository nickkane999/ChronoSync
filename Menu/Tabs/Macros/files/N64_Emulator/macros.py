import pyautogui
import time
import pydirectinput

class Macros:
    # Initializing Object
    def __init__(self):
        self.tasks = self.get_tasks()

    def get_tasks(self):
        tasks = {
            "n64_speed_up": self.n64_speed_up,
            "n64_slow_down": self.n64_slow_down,
            "n64_button_mash_a": self.n64_button_mash_a,
            "n64_button_mash_ab": self.n64_button_mash_ab,
            "n64_button_mash_left": self.n64_button_mash_left,
        }
        return tasks
    
    def n64_speed_up(self):
        for x in range(5):
            pyautogui.press('f11')

    def n64_slow_down(self):
        pyautogui.press('f10')
        for x in range(8):
            print("Slowing down the game...")
            pyautogui.press('f10')
            time.sleep(0.2)

    def n64_button_mash_a(self):
        pydirectinput.PAUSE=0.01
        for x in range(40):
            pydirectinput.press("w")

    def n64_button_mash_ab(self):
        pydirectinput.PAUSE=0.01
        for x in range(40):
            pydirectinput.keyDown('w')
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('w')
            pydirectinput.keyUp('e')
        
    def n64_button_mash_left(self):
        pydirectinput.PAUSE=0.01
        for x in range(40):
            pydirectinput.press("left")