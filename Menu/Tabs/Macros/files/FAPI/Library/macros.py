import pyautogui
import time
from Menu.Tabs.Macros.files.FAPI.Library.WackPotato import WackPotato

class Macros:
    # Initializing Object
    def __init__(self):
        self.tasks = self.get_tasks()
        self.info = self.get_info()
        self.wack_potato = WackPotato()
        self.conditions = {
            "swap_equipment": False
        }

    def get_tasks(self):
        tasks = {
            "maintenance_loop": self.maintenance_loop,
            "play_wack": self.play_wack,
            "main_loop": self.main_loop,
        }
        return tasks
    
    def get_info(self):
        info = {
            "send_10_gems": (0, 0),
            "bomb_all_waves": (0, 0),
        }
        return info

    def maintenance_loop(self, info):
        info = {
            "sample_point": [200, 200],
            "menu": {
                "plant": [680, 990],
                "worm": [780, 990],
                "bag": [300, 990],
            },
            "plants": {
                "points": [[210, 180], [560, 180], [850, 180], [1170, 180], [210, 370], [560, 370], [850, 370], [1170, 370], [210, 550], [560, 550], [850, 550], [1170, 550]],
            },
            "bag": {
                "recycle": [1780, 830],
            },
            "worm": {
                "input_percent": {
                    "1": [1500, 780],
                    "2": [1500, 780],
                },
                "menu": {
                    "1": [770, 890],
                    "2": [900, 890],
                    "3": [1020, 890],
                    "4": [1130, 890],
                },
                "buttons": {
                    "1": [1200, 190],
                    "2": [1200, 380],
                    "3": [1200, 550],
                    "4": [1200, 720],
                },
            },
        }

        # Plant maintenance
        pyautogui.click(*info["sample_point"])
        time.sleep(0.1)
        pyautogui.click(*info["menu"]["plant"])
        time.sleep(0.25)
        for x in info["plants"]["points"]:
            pyautogui.click(*x)
            time.sleep(0.1)
            pyautogui.click(*x)
            time.sleep(0.1)

        time.sleep(0.25)
        # Equipment maintenance
        pyautogui.click(*info["menu"]["bag"])
        time.sleep(0.25)
        pyautogui.click(*info["bag"]["recycle"])
        time.sleep(0.1)
        pyautogui.click(*info["bag"]["recycle"])

        time.sleep(0.25)
        # worm maintenance
        pyautogui.click(*info["menu"]["worm"])
        time.sleep(0.25)
        pyautogui.click(*info["worm"]["input_percent"]["2"])
        time.sleep(0.25)
        pyautogui.click(*info["worm"]["menu"]["1"])
        time.sleep(0.1)
        pyautogui.click(*info["worm"]["buttons"]["1"])
        time.sleep(0.1)
        pyautogui.click(*info["worm"]["buttons"]["2"])

        time.sleep(0.4)
        home_button = [110, 980]
        pyautogui.click(*home_button)


    def play_wack(self, info = None):
        if self.conditions["swap_equipment"]:
            self.swap_equipment()
        point = [1365, 72]
        pyautogui.click(*point)
        time.sleep(0.3)
        self.wack_potato.play()

        point = [300, 990]
        pyautogui.click(*point)
        time.sleep(0.3)
        if self.conditions["swap_equipment"]:
            self.swap_equipment()

    def main_loop(self, info):
        while True:
            self.play_wack()
            for x in range(12):
                self.maintenance_loop(info)
                time.sleep(21)