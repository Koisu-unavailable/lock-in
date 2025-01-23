import tkinter as tk
from . import TKelement
class Window_base():
    """
    Contains the base for a "window" (really just a set of elements).
    This is an ABSTRACT CLASS
    """
    def __init__(self,root : tk.Tk, title : str = "" ):
        self.title = title
        self.root = root
        if not self.root:
            print(self.root)
            raise TypeError("Root should not be falsey")
        if title:
            self.root.title(title)
        self.elements : dict[str, TKelement.TkElement ] = {}
        # A dictionary that stores the name of an element as key. The value is a list containing the the actual widget, and the rows and columns of the grid
        # EXAMPLE:
        """
        {
            "testButton": [
                tk.Button(args),
                1,
                2
            ]
        }
        """

    def load(self):
        """Loads elements.
        P.S. This should only be called AFTER unloading elements."""
        for element in self.elements.values():
            element.widget.grid(row=element.row, column=element.column)
    def unload(self):
        for widget in self.root.winfo_children():
            widget.destroy()