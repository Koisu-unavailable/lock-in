class Window_base():
    def __init__(self, title, root):
        self.title = title
        self.root = root
        if title:
            self.root.title