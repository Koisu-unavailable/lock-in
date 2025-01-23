from typing import NamedTuple
import tkinter as tk

class Element(NamedTuple):
    widget : tk.Widget
    row : int
    column : int