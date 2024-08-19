import pyautogui
import time
import math
import pydirectinput

class Macros:
    # Initializing Object
    def __init__(self):
        self.tasks = self.get_tasks()
        self.info = self.get_info()

    def get_tasks(self):
        tasks = {
            "increase_mana_pool": self.increase_mana_pool,
            "upgrade_gems": self.upgrade_gems,
            "duplicate_gems": self.duplicate_gems,
            "send_5_gems": self.send_5_gems,
            "send_gem_inventory": self.send_gem_inventory,
            "gem_upgrade_exploit": self.gem_upgrade_exploit,
            "gem_upgrade_exploit_small": self.gem_upgrade_exploit_small,
        }
        return tasks
    
    def get_info(self):
        info = {
            "increase_mana_pool": {
                "check_point": (1589, 236),
                "active_color": (255, 254, 248),
            },
            "send_5_gems":  {
                "next_wave_point": (321, 174),
                "gem_points": {
                    "gem1": (1485, 819),
                    "gem2": (1485, 773),
                    "gem3": (1485, 744),
                    "gem4": (1485, 683),
                    "gem5": (1485, 630),
                    "gem6": (1485, 587),
                    "gem7": (1485, 532),
                    "gem8": (1485, 493),
                    "gem9": (1485, 453),
                    "gem10": (1485, 386),
                    "gem11": (1485, 345),
                    "gem12": (1485, 300),
                }
            },
        }
        return info

    # Increase mana pool
    def increase_mana_pool(self):
        check_point = self.info["increase_mana_pool"]["check_point"]
        valid_color = self.info["increase_mana_pool"]["active_color"]

        x = 0
        print("Valid color: ", valid_color)
        print("Check point: ", check_point)
        while x < 100:
            time.sleep(0.2)
            current_color = pyautogui.pixel(*check_point)
            print("current color: ", current_color)
            
            if self.is_good_color(valid_color, current_color):
                print("Got the right color")
                pyautogui.click(*check_point)
                pyautogui.press('m')

        print("Increasing mana pool")

    def color_distance(self, color1, color2):
        return math.sqrt(sum([(x - y) ** 2 for x, y in zip(color1, color2)]))

    def is_good_color(self, valid_color, current_color):
        return self.color_distance(valid_color, current_color) < 30

    # Upgrade gems
    def upgrade_gems(self):
        for x in range(200):
            pyautogui.press('u')
            time.sleep(0.05)

    # Duplicate gems
    def duplicate_gems(self):
        for x in range(100):
            pyautogui.press('d')
            time.sleep(0.05)

    # Send 5 gems
    def send_5_gems(self, gem_type = "gem9"):
        next_wave_point = self.info["send_5_gems"]["next_wave_point"]
        created_gem_point = self.info["send_5_gems"]["gem_points"][gem_type]

        if gem_type != "gem1":
            pyautogui.click(70, 1000)
            pydirectinput.PAUSE=0.05
            time.sleep(1)

            print("Creating gems")
            pyautogui.press("7")
            pydirectinput.keyDown('ctrl')
            pyautogui.click(*created_gem_point)
            pydirectinput.keyUp('ctrl')
            time.sleep(0.3)


        print("Sending 5 gems")
        pydirectinput.keyDown('shift')
        pyautogui.press('b')
        pydirectinput.keyUp('shift')
        for x in range(5):
            pydirectinput.keyDown('shift')
            pyautogui.click(*next_wave_point)
            pydirectinput.keyUp('shift')
            
    def send_gem_inventory(self):
        print("Sending gem inventory")
        next_wave_point = self.info["send_5_gems"]["next_wave_point"]
        pydirectinput.keyDown('shift')
        pyautogui.press('b')
        pydirectinput.keyUp('shift')
        for x in range(36):
            pydirectinput.keyDown('shift')
            pyautogui.click(*next_wave_point)
            pydirectinput.keyUp('shift')

    def gem_upgrade_exploit(self):
        for x in range(100):
            pyautogui.press('b')
            pyautogui.press('u')

    def gem_upgrade_exploit_small(self):
        for x in range(20):
            pyautogui.press('b')
            pyautogui.press('u')

    '''
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
    '''
