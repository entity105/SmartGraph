import tkinter as tk
import matplotlib.pyplot as plt

class BaseWindow:
    def __init__(self, manager, title="Окно", size="500x600"):
        self.manager = manager
        self.current_file = self.manager.current_file

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.root.protocol("WM_DELETE_WINDOW", self.close_win)
        self.setup()

    def setup(self):
        """Наполнение окна"""
        pass

    def close_win(self):
        """Действие при закрытии"""
        self.root.destroy()
        self.manager.current_window = None
        pass

    def exit_program(self):
        self.root.destroy()
        self.manager.current_window = None
        plt.close('all')

    def run(self):
        self.root.mainloop()
