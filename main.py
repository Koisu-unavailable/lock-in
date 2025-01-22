import tkinter as tk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("Lock in") # Todo: Change name
        self.root.iconbitmap("assets\ICO-TO-BE-REPLACED.ico")
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()