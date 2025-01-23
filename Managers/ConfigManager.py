from subprocess import call
import platform
class ConfigManager():
    def __init__(self, config_path):
        self.config_path = config_path
        
    def open_config(self):
        if platform.system() == "Windows":
            call(f"notepad {self.config_path}")
        else:
            return "Os not supported"


    