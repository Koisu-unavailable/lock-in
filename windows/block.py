from . import window_base
import tkinter as tk
from . import TKelement
from Managers import ConfigManager
import logging
class Block_window(window_base.Window_base):
    def __init__(self, root: tk.Tk,  title : str = None):
        super().__init__(root=root)
        self.config = ConfigManager.ConfigManager("./config.txt")
        self.elements["block_button"] = TKelement.TkElement(
            tk.Button(root, text="Start block"),
            1,
            1
        )
        self.elements["open_config"] = TKelement.TkElement(
            tk.Button(root, text="Open config", command=self.open_config),
            1,
            2
        )
        self.elements["load_config"] = TKelement.TkElement(
            tk.Button(root,text="Load config", command=self.load_config),
            1,
            3
        )
    def open_config(self):
        logging.log(logging.DEBUG, "Opening config")
        self.config.open_config()
    def load_config(self):
        self.config.read_config()
        