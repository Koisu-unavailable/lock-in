from . import window_base
import tkinter as tk
from . import TKelement
from Managers import ConfigManager
import logging
class Block_window(window_base.Window_base):
    def __init__(self, root: tk.Tk,  title : str = None):
        super().__init__(root=root)
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
    def open_config(self):
        logging.log(logging.DEBUG, "Opening config")
        s = ConfigManager.ConfigManager("./config.txt")
        s.open_config()