from . import window_base
import tkinter as tk
from . import element
class Block_window(window_base.Window_base):
    def __init__(self, root: tk.Tk,  title : str = None):
        super().__init__(root=root)
        self.elements["block_button"] = element.Element(
            tk.Button(root, text="Start block"),
            1,
            1
        )