from Menu.Tabs.Macros.files.FAPI.Library.macros import Macros as Macros_Library

class Macros:
    def __init__(self):
        self.macros = Macros_Library()
        macros = self.macros
        self.tasks = {
            "maintenance_loop": macros.maintenance_loop,
            "play_wack": macros.play_wack,
            "main_loop": macros.main_loop,
        }
