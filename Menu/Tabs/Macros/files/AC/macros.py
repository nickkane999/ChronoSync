import pyautogui
import time

class Macros:
    def __init__(self):
        self.info = self.get_info()
        #self.macros = Macros()
        self.tasks = {
            "collect_research": self.collect_research,
            "do_daily_quest": self.do_daily_quest,
        }

    def get_info(self):
        info = {
            "points": {
                "tabs": {
                    "potatoes": (610, 50),
                    "land": (810, 50),
                    "ore": (1070, 50),
                    "weapons": (1350, 50),
                    "medicine": (1600, 50),
                },
                "buttons": {
                    "collect_research": (1680, 970),
                    "run_industries": (150, 570),
                    "collect_daily": (960, 890),
                },
                "check_daily_point": (390, 800),
            },
            "colors": {
                "active_daily": (129, 32, 40),
                "inactive_daily": (211, 52, 66),
            }
        }
        return info
    
    def collect_research(self):
        print("Collecting dailies")
        tabs = self.info["points"]["tabs"]
        collect_research_button = self.info["points"]["buttons"]["collect_research"]

        # For each tab, click on the tab then the "collect_daily" button
        for tab in tabs:
            pyautogui.click(*tabs[tab])
            time.sleep(0.5)
            pyautogui.click(*collect_research_button)
            time.sleep(0.5)
    
    def do_daily_quest(self):
        print("Doing daily quest")
        collect_count = 0 
        while collect_count < 15:
            self.collect_chest()
            collect_count += 1
            print (f"Collected {collect_count} chests")

    def collect_chest(self):
        chest_collected = False
        check_daily_point = self.info["points"]["check_daily_point"]
        buttons = self.info["points"]["buttons"]
        while not chest_collected:
            x = 0
            while x < 10:
                pyautogui.click(*buttons["run_industries"])
                x += 1
            if pyautogui.pixel(*check_daily_point) == self.info["colors"]["active_daily"]:
                pyautogui.click(*buttons["collect_daily"])
                chest_collected = True
                time.sleep(4)
                pyautogui.click(*buttons["run_industries"])
                time.sleep(0.3)
    