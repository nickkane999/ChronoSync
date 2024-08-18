import json
import os

class TimerDataManager:
    def __init__(self, file_helper):
        self.file_helper = file_helper
        self.json_file =  self.file_helper.files["tracked_info.json"]
        self.current_values = {}

    def load_current_values(self, key=None):
        self.current_values = {}
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
                if key:
                    category = data.get(key, {}).get("category", "Uncategorized")
                    if category not in self.current_values:
                        self.current_values[category] = {}
                    self.current_values[category][key] = data.get(key, {})
                    print(self.current_values)
                else:
                    for title, info in data.items():
                        category = info.get("category", "Uncategorized")
                        if category not in self.current_values:
                            self.current_values[category] = {}
                        self.current_values[category][title] = info
        except FileNotFoundError:
            pass
        return self.current_values
    
    def get_current_values(self):
        return self.current_values
    
    def get_category(self, data, key):
        return data.get(key, {}).get("category", "Uncategorized")