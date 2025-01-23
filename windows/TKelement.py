from typing import NamedTuple
import tkinter as tk

class TkElement(NamedTuple):
    widget : tk.Widget
    row : int
    column : int