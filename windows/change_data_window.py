import tkinter as tk
from windows.base_window import BaseWindow

class ChangeDataInterface(BaseWindow):
    is_over = True

    def __init__(self, manager, title="Изменение данных", size="600x400"):
        super().__init__(manager, title, size)

    def setup(self):
        label = tk.Label(self.root, text="Изменить данные", font=("Arial", 20, "bold"))
        label.pack(anchor='n', pady=10, expand=True)

        font = ("Arial", 15, "bold")

        text_1 = tk.Label(self.root, text="Дата:", font=font)
        text_1.place(x=20, y=130)

        pole_1 = tk.Entry(self.root, width=10, font=font)
        pole_1.place(x=80, y=130)

        text_2 = tk.Label(self.root, text="Новое значение:", font=font)
        text_2.place(x=250, y=130)

        pole_2 = tk.Entry(self.root, width=10, font=font)
        pole_2.place(x=425, y=130)

        btn_del = tk.Button(self.root, text="Удалить точку", font=("Arial", 10, "bold")) # Удаление точки, если такая существует
        btn_del.place(x=75, y=162, width=130)

        btn_ready = tk.Button(self.root, text="Готово", font=("Arial", 30, "bold"),
                              command=self.close_win)  # Возвращение назад, закрытие окна
        btn_ready.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        btn_save = tk.Button(self.root, text="Сохранить", font=("Arial", 10, "bold")) # Изменение данных в файле
        btn_save.place(x=420, y=162, width=120)