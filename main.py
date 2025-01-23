import tkinter as tk
import windows
import windows.block
import logging
class App():
    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("Lock in") # Todo: Change name
        self.root.iconbitmap("assets\\ICO-TO-BE-REPLACED.ico")
        print(self.root)
        self.default_window = windows.block.Block_window(root=self.root)
    def run(self):
        self.default_window.load()
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()