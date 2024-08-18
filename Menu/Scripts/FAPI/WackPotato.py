import pyautogui
import time
import math
pyautogui.PAUSE = 0.003


class WackPotato:
    def __init__(self):
        self.points = ""
        self.colors = {
            "inactive_brown": (195, 106, 33),
            "active1_green": (98, 178, 7),
            "active2_gold": (227, 169, 10),
            "bad_red": (217, 45, 13),
            "active_backpack": (200, 192, 19)
        }
        self.threshold = 30

    def color_distance(self, color1, color2):
        return math.sqrt(sum([(x - y) ** 2 for x, y in zip(color1, color2)]))

    def is_good_color(self, color):
        return self.color_distance(color, self.colors["active1_green"]) < 30 or self.color_distance(color, self.colors["active2_gold"]) < 30

    def is_bad_click_ok(self, color):
        return self.color_distance(color, self.colors["bad_red"]) < 30

    def play(self, Loop = False):
        wack_potato = {
            "head1": [350, 379],
            "head2": [481, 379],
            "head3": [613, 379],
            "head4": [746, 379],
            "head5": [877, 379],
            "head6": [350, 598],
            "head7": [481, 598],
            "head8": [613, 598],
            "head9": [746, 598],
            "head10": [877, 598],
            "head11": [350, 809],
            "head12": [481, 809],
            "head13": [613, 809],
            "head14": [746, 809],
            "head15": [877, 809]
        }
        if Loop:
            while True:
                self.playing_game(wack_potato)
        else:
            self.playing_game(wack_potato)

    def playing_game(self, wack_potato):
        count = 0
        start_time = time.time()
        click_time  = time.time()
        game_time = 65
        pyautogui.click(650, 1000)
        time.sleep(2)

        while time.time() - start_time < game_time:
            for point_name, point_position in wack_potato.items():
                point_color = pyautogui.pixel(*point_position)
                if self.is_good_color(point_color):
                    rest_time = time.time() - click_time
                    if rest_time < 0.07:
                        time.sleep(0.07 - rest_time)
                    pyautogui.click(point_position[0] + 12, point_position[1])
                    click_time = time.time()
                elif count > 0 and self.is_bad_click_ok(point_color):
                    count -= 1
                    rest_time = time.time() - click_time
                    if rest_time < 0.07:
                        time.sleep(0.07 - rest_time)
                    pyautogui.click(point_position[0] + 12, point_position[1])
                    click_time = time.time()
            time.sleep(0.001)
        time.sleep(2)
