import json
import os

class TimerDataManager:
    def __init__(self):        
        self.json_file =  self.find_base_directory_with_file("tracked_info.json")
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
    
    def find_base_directory_with_file(self, target_file):
        current_dir = os.path.abspath(__file__)
        
        while True:
            parent_dir = os.path.dirname(current_dir)
            
            if parent_dir == current_dir:  # Reached the root directory
                raise FileNotFoundError(f"{target_file} not found in any parent directory.")
            
            potential_file = os.path.join(parent_dir, target_file)
            
            if os.path.isfile(potential_file):
                return potential_file
            
            current_dir = parent_dir