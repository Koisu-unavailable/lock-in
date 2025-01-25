import PIL.Image
from . import ConfigManager
# import pyautogui
# import win32gui
# import win32con
# import pystray
import PIL
class BlockManager():
    def __init__(self,config: ConfigManager.Config):
        self.config = config

    # def minimize_all_windows(self):
    #     def enum_handler(hwnd, lParam):
    #         if win32gui.IsWindowVisible(hwnd):
    #             win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    #     win32gui.EnumWindows(enum_handler, None)

    # def restore_all_windows(self):
    #     def enum_handler(hwnd, lParam):
    #         if win32gui.IsWindowVisible(hwnd):
    #             win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    #     win32gui.EnumWindows(enum_handler, None)

    def _block_windows(self):
        pass



s = BlockManager(None)
s._block_windows()
