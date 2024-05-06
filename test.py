from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height, title="Window"):
        self.root = tk.Tk()
        self.root.title(title)
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.__root = Tk()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def main():
        win = Window(800, 600)
        win.wait_for_close()


