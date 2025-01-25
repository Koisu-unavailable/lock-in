from subprocess import call
import platform
import logging
from typing import NamedTuple
from . import errors
class ConfigManager():
    """This is a singleton. Please dont establish multiple instances of it
    """
    def __init__(self, config_path):
        self.config_path = config_path
        self.logger = logging.Logger("ConfigManager")
        self.logger.setLevel(logging.ERROR)
    def open_config(self):
        if platform.system() == "Windows":
            call(f"notepad {self.config_path}")
        else:
            return "Os not supported"
    def read_config(self):
        exes = []
        with open(self.config_path, 'r') as file:
            try:
                version = file.readline()
                version = int(version)
            except Exception:
                self.logger.error("MALFORMED CONFIG")
                raise errors.ConfigError("Something's wrong with your config")
            if version != 1:
                self.logger.error("CONFIG FILE VERSION NOT THE EQUAL. CONFIGURATION WON'T WORK")
                raise errors.ConfigError("Config version not the same")
            try:
                
                line = file.readline().removesuffix("\n")
                print(line)
                assert line == str("[EXES]")
                done = False
                while not done:
                    line = file.readline().removesuffix("\n")
                    print(line)
                    if not (line != "[APPS]"):
                        done = True
                    else:
                        exes.append(line)
                print(exes)
            except AssertionError:
                raise errors.ConfigError("Something's wrong with your config")
                

class Config(NamedTuple):
    exes : list[str]
    titles : list[str]
    urls : list[str]