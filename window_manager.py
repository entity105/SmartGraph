from windows.menu_window import MenuWindow
from windows.graph_window import GraphInterface
from windows.change_data_window import ChangeDataInterface
from windows.setting_file_window import SettingFileInterface
from windows.edit_file_win import EditFileInterface

class WindowManager:
    def __init__(self):
        self.current_window = None
        self.current_file = self.load_file_path()
        # self.window_stack = []
        self.graph_win = None

    @staticmethod
    def load_file_path():
        try:
            with open("dist.__last_file.txt", "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    def show_window(self, window_class, **kwargs):
        if self.current_window and not window_class.is_over:
            self.close_current_window()
        self.current_window = window_class(self, **kwargs)        # Создаётся объект класса окна
        if isinstance(self.current_window, GraphInterface):
            self.graph_win = self.current_window
        self.current_window.run()
        # self.window_stack.append(window_class)

    def close_current_window(self):
        self.current_window.root.destroy()
        self.current_window = None
        # self.window_stack.pop()

    def show_menu_win(self):
        self.show_window(MenuWindow)

    def show_graph_win(self):
        self.show_window(GraphInterface)

    def show_change_data_win(self):
        self.show_window(ChangeDataInterface)

    def show_file_setting_win(self):
        self.show_window(SettingFileInterface)

    def show_edit_file_win(self):
        self.show_window(EditFileInterface)