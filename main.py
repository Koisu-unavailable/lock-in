import tkinter as tk

import pystray
from Managers.BlockManager import BlockManager
import windows
import windows.block
import logging
import PIL
import threading
import os
import time
class App():
    def __init__(self):
        self.threads : dict[str, threading.Thread] = {}
        logging.getLogger().setLevel(logging.DEBUG)
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("Lock in") # Todo: Change name
        self.root.iconbitmap("assets\\ICO-TO-BE-REPLACED.ico")
        self.default_window = windows.block.Block_window(root=self.root)
        self.blocking = True
    def run(self):
        icon = pystray.Icon("Lock-in", PIL.Image.open("assets\\ICO-TO-BE-REPLACED.ico"))
        icon.menu = pystray.Menu(
            pystray.MenuItem("Stop Block", self.quit_test_block),
            pystray.MenuItem("test", lambda: logging.DEBUG("ICO TEST BUTTON"))
        )
        self.default_window.load()
        self.threads["icon"] = threading.Thread(target=icon.run)
        self.threads["block"] = threading.Thread(target=self._test_daemon)
        for thread in self.threads.values():
            if app.threads["block"] == thread:
                thread.daemon = True
                thread.name = "block"
            else:
                thread.name = "icon"
            thread.start()
        self.root.mainloop()
    def _test_daemon(self):
        while self.blocking:
            print("test")
    def quit_test_block(self):
        self.blocking = False
        


if __name__ == '__main__':
    app = App()
            
    
    app.run()
