from windows.menu_window import MenuWindow
from windows.graph_window import GraphInterface
from windows.change_data_window import ChangeDataInterface

class WindowManager:
    def __init__(self, current_file:str):
        self.current_window = None
        self.current_file = current_file

    def show_window(self, window_class, **kwargs):
        if self.current_window and not window_class.is_over:
            self.close_current_window()
        self.current_window = window_class(self, **kwargs)        # Создаётся объект класса окна
        self.current_window.run()

    def close_current_window(self):
        self.current_window.root.destroy()
        self.current_window = None

    def show_menu_win(self):
        self.show_window(MenuWindow)

    def show_graph_win(self):
        self.show_window(GraphInterface)

    def show_change_data_win(self):
        self.show_window(ChangeDataInterface)

i = WindowManager("data.csv")
i.show_menu_win()