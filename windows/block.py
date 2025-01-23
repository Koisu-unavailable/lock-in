from . import window_base
import tkinter as tk
from . import TKelement
class Block_window(window_base.Window_base):
    def __init__(self, root: tk.Tk,  title : str = None):
        super().__init__(root=root)
        self.elements["block_button"] = TKelement.TkElement(
            tk.Button(root, text="Start block", command=self.start_block),
            1,
            1
        )
    def start_block(self):
        self.unload()