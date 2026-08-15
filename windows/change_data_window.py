import tkinter as tk
import pandas as pd
from windows.base_window import BaseWindow

class ChangeDataInterface(BaseWindow):
    is_over = True

    def __init__(self, manager, title="Изменение данных", size="600x400"):
        super().__init__(manager, title, size)
        # self.data_to_del = None

    def setup(self):
        label = tk.Label(self.root, text="Изменить данные", font=("Arial", 20, "bold"))
        label.pack(anchor='n', pady=10, expand=True)

        font = ("Arial", 15, "bold")

        text_1 = tk.Label(self.root, text="Дата:", font=font)
        text_1.place(x=20, y=130)

        self.pole_1 = tk.Entry(self.root, width=10, font=font)
        self.pole_1.place(x=80, y=130)

        text_2 = tk.Label(self.root, text="Новое значение:", font=font)
        text_2.place(x=250, y=130)

        self.pole_2 = tk.Entry(self.root, width=10, font=font)
        self.pole_2.place(x=425, y=130)

        btn_del = tk.Button(self.root, text="Удалить точку", font=("Arial", 10, "bold"),
                            command=self.del_point) # Удаление точки, если такая существует
        btn_del.place(x=75, y=162, width=130)

        btn_ready = tk.Button(self.root, text="Готово", font=("Arial", 30, "bold"),
                              command=self.close_win)  # Возвращение назад, закрытие окна
        btn_ready.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        btn_save = tk.Button(self.root, text="Сохранить", font=("Arial", 10, "bold"),
                             command=self.edit_point) # Изменение данных в файле
        btn_save.place(x=420, y=162, width=120)

    def del_point(self):
        key = self.get_row_1()
        df = pd.read_csv(self.manager.current_file)
        updated = df[df.iloc[:, 0] != key]
        updated.to_csv(self.manager.current_file, index=False)
        self.manager.graph_win.update_graph(self.manager.current_file)

    def edit_point(self):
        key = self.get_row_1()
        new_value = self.get_row_2()

        df = pd.read_csv(self.manager.current_file)

        # Обновляем значение во втором столбце, где первый == key
        df.loc[df.iloc[:, 0] == key, df.columns[1]] = new_value

        df.to_csv(self.manager.current_file, index=False)
        self.manager.graph_win.update_graph(self.manager.current_file)

    def get_row_1(self):
        row = self.pole_1.get()
        try:
            res = int(row)
            self.pole_1.delete(0, tk.END)
            return res
        except (TypeError, ValueError):
            err_label = tk.Label(self.root, text="Неверный ввод", fg="#700314", bg="#f6afb5")
            err_label.place(x=90, y=190)
            self.root.after(1500, lambda: err_label.destroy())

    def get_row_2(self):
        row = self.pole_2.get()
        try:
            res = float(row)
            self.pole_2.delete(0, tk.END)
            return res
        except (TypeError, ValueError):
            err_label = tk.Label(self.root, text="Неверный ввод", fg="#700314", bg="#f6afb5")
            err_label.place(x=440, y=190)
            self.root.after(1500, lambda: err_label.destroy())
