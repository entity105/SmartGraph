import tkinter as tk
import os
from windows.base_window import BaseWindow

class MenuWindow(BaseWindow):
    is_over = False  # Поверх другого окна. По умолчанию - нет

    def __init__(self, manager, title="Главное меню", size="500x600"):
        super().__init__(manager, title, size)

    def setup(self):
        """Наполнение окна"""
        # Центральный фрейм
        center_frame = tk.Frame(self.root, bd=2, relief="groove", pady=20, padx=20)
        center_frame.place(relx=0.5, rely=0.4, anchor="center")

        base_setting = dict(font=("Arial", 20, "bold"), width=20)
        # Заголовок
        label = tk.Label(center_frame, text="Меню", height=1, font=("Arial", 25, "bold"), width=20)
        label.pack()

        btn_graph = tk.Button(center_frame, text="Посмотреть график", command=self.manager.show_graph_win,
                              height=1, **base_setting)
        btn_graph.pack(pady=8)

        btn_file = tk.Button(center_frame,
                             text=f"Выбрать файл\n(Выбрано: "
                                  f"{os.path.basename(self.manager.current_file) if self.manager.current_file else None})",
                             height=2, command=self.manager.show_file_setting_win, **base_setting)
        btn_file.pack()

        btn_upload = tk.Button(center_frame, text="Выгрузить данные", height=1, **base_setting)
        btn_upload.pack(pady=8)

        btn_exit = tk.Button(center_frame, text="Выход", command=self.exit_program,
                             height=1, **base_setting)
        btn_exit.pack()

        


