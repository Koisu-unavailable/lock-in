import tkinter as tk

class Window_base():
    """
    Contains the base for a "window" (really just a set of elements).
    This is an ABSTRACT CLASS
    """
    def __init__(self, title : str, root : tk.Tk):
        self.title = title
        self.root = root
        if title:
            self.root.title(title)
        self.elements : dict[str, list[tk.Widget, int, int]] = {}
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
        for element in self.elements.values:
            element[0].grid(element[1], element[2])
    def unload(self):
        for widget in self.root.winfo_children():
            widget.destroy()