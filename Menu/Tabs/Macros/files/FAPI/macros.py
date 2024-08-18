from Menu.Scripts.FAPI import Macros

class Macros:
    def __init__(self):
        self.macros = Macros()
        macros = self.macros
        self.tasks = {
            "maintenance_loop": macros.maintenance_loop,
            "get_point": macros.get_point,
            "play_wack": macros.play_wack,
            "main_loop": macros.main_loop,
            "action_check": macros.action_check,
            "check_point": macros.check_point,
            "testing": macros.testing,
        }
    