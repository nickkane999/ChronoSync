import os

class FileHelper:
    def __init__(self):
        self.files = {
            "tracked_info.json": self.find_base_directory_with_file("tracked_info.json")
        }

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