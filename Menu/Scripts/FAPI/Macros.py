import pyautogui
import time
import math
import pydirectinput
import random
from Menu.Scripts.FAPI.WackPotato import WackPotato
from pynput.keyboard import Key, Controller

class Macros:
    # Initializing Object
    def __init__(self):
        self.tasks = self.get_tasks()
        self.info = self.get_info()
        self.keyboard = Controller()
        self.wack_potato = WackPotato()
        self.conditions = {
            "swap_equipment": False
        }

    def get_tasks(self):
        tasks = {
            "maintenance_loop": self.maintenance_loop,
            "get_point": self.get_point,
            "play_wack": self.play_wack,
            "main_loop": self.main_loop,
            "action_check": self.action_check,
            "check_point": self.check_point,
            "testing": self.testing,
        }
        return tasks
    
    def get_info(self):
        info = {
            "increase_mana_pool": {
                "check_point": (1589, 236),
                "active_color": (255, 254, 248),
            },
            "upgrade_gems": {
                "gem_point1": (1485, 300),
                "gem_point2": (1545, 300),
                "gem_point3": (1600, 300),
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
            "send_10_gems": (0, 0),
            "bomb_all_waves": (0, 0),
        }
        return info

    # Increase mana pool
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

    def swap_equipment(self):
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

        points = {
            "head": [770, 780],
            "body": [850, 780],
            "feet": [960, 780],
            "shield": [1040, 780],
            "gloves": [1160, 780],
            "weapon": [1250, 780],
        }

        pyautogui.click(*info["menu"]["bag"])
        time.sleep(0.25)
        pyautogui.click(*info["bag"]["recycle"])
        time.sleep(0.1)
        pyautogui.click(*info["bag"]["recycle"])
        time.sleep(0.1)

        for item, point in points.items():
            pyautogui.click(point[0], point[1])
            time.sleep(0.1)
            pyautogui.click(point[0], point[1])
            time.sleep(0.1)

        time.sleep(0.1)
        pyautogui.click(*info["menu"]["bag"])
        time.sleep(0.1)

    def main_loop(self, info):
        while True:
            self.play_wack()
            for x in range(12):
                self.maintenance_loop(info)
                time.sleep(21)

    def jump_attack_big(self):
        # big jump 1
        for x in range(5):
            pyautogui.keyDown('space')
            time.sleep(0.12)
            pyautogui.keyUp('space')
            pyautogui.press('space')
            time.sleep(0.15)
            pyautogui.press('space')
            time.sleep(0.07)
            pyautogui.press('space')
            time.sleep(0.07)
            pyautogui.press('space')
            time.sleep(0.07)
            pyautogui.press('space')
            time.sleep(0.07)
            pyautogui.press('space')

            pydirectinput.keyDown('shift')
            pydirectinput.keyUp('shift')
            time.sleep(0.05)

        # Big jump 2
        """
        pyautogui.keyDown('space')
        time.sleep(0.15)
        pyautogui.keyUp('space')
        pyautogui.press('space')
        time.sleep(0.3)
        pyautogui.press('space')
        pyautogui.press('space')
        time.sleep(0.05)
        pyautogui.press('space')
        time.sleep(0.05)
        pyautogui.press('space')
        time.sleep(0.05)
        pyautogui.press('space')
        """


    def jump_attack_small(self):
        # higher lvl
        pyautogui.press('space')
        time.sleep(0.11)
        pyautogui.press('space')
        time.sleep(0.15)
        pyautogui.press('space')
        time.sleep(0.08)
        pyautogui.press('space')

        pydirectinput.keyDown('shift')
        pydirectinput.keyUp('shift')
        #time.sleep(1.7)

        # lvl 300
        """
        pyautogui.press('space')
        time.sleep(0.07)
        pyautogui.press('space')
        time.sleep(0.07)
        pyautogui.press('space')
        time.sleep(0.07)
        pyautogui.press('space')
        time.sleep(0.11)
        pyautogui.press('space')
        
        """
        
        # low level
        """
        pyautogui.press('space')
        time.sleep(0.3)
        pyautogui.press('space')
        """

        """
        pyautogui.press('space')
        time.sleep(0.05)
        pyautogui.press('space')
        time.sleep(0.05)
        pyautogui.press('space')

        pydirectinput.keyDown('shift')
        pydirectinput.keyUp('shift')
        """
        
    def action_check(self):
        threshhold = 30

        # Check for block to jump
        regular_block = (255, 174, 120)
        portal_block = (141, 99, 215)
        block_point = [195, 410]
        block_check_1 = self.color_distance(regular_block, pyautogui.pixel(*block_point)) < threshhold
        #print(pyautogui.pixel(*block_point))
        #print("Regular block active: " + str(block_check_1))
        block_check_2 = self.color_distance(portal_block, pyautogui.pixel(*block_point)) < threshhold
        #print("Portal block active: " + str(block_check_2))
        if block_check_1 or block_check_2: 
            pydirectinput.keyDown('space')
            pydirectinput.keyUp('space')

        # Check for chest_pick
        chest_pick_1 = (208, 193, 114)
        chest_pick_2 = (221, 215, 204)
        chest_pick_point_1 = [930, 1075]
        chest_pick_point_2 = [930, 0]
        chest_pick_check_1 = self.color_distance(chest_pick_1, pyautogui.pixel(*chest_pick_point_1)) < threshhold
        chest_pick_check_2 = self.color_distance(chest_pick_2, pyautogui.pixel(*chest_pick_point_2)) < threshhold
        #print("Chest pick 1 active: " + str(chest_pick_check_1))
        #print("Chest pick 2 active: " + str(chest_pick_check_2))
        if chest_pick_check_1 and chest_pick_check_2:
            self.clear_chest_pick()

        # Check for bonus stage
        bonus_stage = (0, 168, 0)
        bonus_stage_done = (180, 0, 0)
        bonus_stage_point = [1200, 780]
        bonus_stage_done_point = [1165, 810]
        #point = pyautogui.position()
        print(pyautogui.pixel(*bonus_stage_point))
        if self.color_distance(bonus_stage, pyautogui.pixel(*bonus_stage_point)) < threshhold + 30:
            self.play_bonus_stage()
        if self.color_distance(bonus_stage_done, pyautogui.pixel(*bonus_stage_done_point)) < threshhold:
            pyautogui.click(*bonus_stage_done_point)
        

    def clear_chest_pick(self):
        pyautogui.click(100, 0)
        chest_pick_done = (180, 0, 0)
        chest_pick_done_point = [1090, 980]
        chest_save = (255, 235, 4)
        find_save = True 
        threshold = 30

        in_progress = True
        while in_progress:
            chest_pick_done = (180, 0, 0)
            chest_pick_done_point = [1090, 980]
            print(pyautogui.pixel(*chest_pick_done_point))
            chest_pick_done_check = self.color_distance(chest_pick_done, pyautogui.pixel(*chest_pick_done_point)) < threshold
            if chest_pick_done_check:
                in_progress = False
            else:
                base_point = [362, 439]
                x_increment = 143
                y_increment = 143
                time.sleep(5)
                pyautogui.click(base_point[0], base_point[1])
                time.sleep(5)
                pyautogui.click(base_point[0], base_point[1] + y_increment)
                for i in range(2):
                    if i != 0:
                        find_save = False
                    for x in range(10):
                        for y in range(3):
                            is_valid_save = find_save and self.color_distance(chest_save, pyautogui.pixel(base_point[0] + x * x_increment, base_point[1] + y * y_increment)) < threshold
                            doesnt_need_save = not find_save
                            pyautogui.moveTo(base_point[0] - 20 + x * x_increment, base_point[1] + y * y_increment)
                            time.sleep(0.2)
                            if is_valid_save or doesnt_need_save:
                                pyautogui.click(base_point[0] + x * x_increment, base_point[1] + y * y_increment)
                                time.sleep(5)
                                chest_pick_done_check = self.color_distance(chest_pick_done, pyautogui.pixel(*chest_pick_done_point)) < threshold
                                if chest_pick_done_check:
                                    in_progress = False
                                    break
                        if chest_pick_done_check:
                            in_progress = False
                            break

        print("Chest pick cleared")
        pyautogui.click(*chest_pick_done_point)

    def play_bonus_stage(self):
        print("Playing bonus stage")
        start_x, start_y = 690, 890
        end_x, end_y = 1330, 890
        for x in range(3):
            pydirectinput.moveTo(start_x, start_y + (x - 1) *50)
            pydirectinput.mouseDown()
            pydirectinput.moveTo(end_x, end_y, duration=2)  # duration is in seconds
            pydirectinput.mouseUp()
        bonus_stage_point = [710, 890]
        pyautogui.click(*bonus_stage_point)

    def get_point(self, info):
        x = 0
        while x < 100:
            time.sleep(1)
            print(pyautogui.position())
            x += 1

    def check_point(self, info):
        point = pyautogui.position()
        print(point)
        print(pyautogui.pixel(*point))

    def testing(self, info):
        pyautogui.click(140, 100)
        time.sleep(0.5)
        pyautogui.click(470, 930)
        time.sleep(0.5)
        pyautogui.click(500, 220)
        time.sleep(0.5)
        pyautogui.click(800, 930)
        time.sleep(0.5)
        pyautogui.click(1000, 20)

    # utility functions
    def is_color_match(self, color1, color2):
        threshold = 30
        return self.color_distance(color1, color2) < threshold

    def color_distance(self, color1, color2):
        return math.sqrt(sum([(x - y) ** 2 for x, y in zip(color1, color2)]))    