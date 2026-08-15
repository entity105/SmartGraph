from windows.base_window import BaseWindow
import pandas as pd
import tkinter as tk
import os

class EditFileInterface(BaseWindow):
    is_over = False

    def __init__(self, manager, title="Файлы", size="500x250"):
        self.entry = None
        super().__init__(manager, title, size)

    def setup(self):
        label1 = tk.Label(self.root, text="Создать файл", font=("Arial", 22, 'bold'))
        label1.pack(anchor='n', expand=True, pady=10)

        label2 = tk.Label(self.root, text="Имя файла:", font=("Arial", 14, 'bold'))
        label2.place(x=20, y=100)

        self.entry = tk.Entry(self.root, font=("Arial", 15, "bold"), width=20)
        self.entry.place(x=150, y=100)

        btn_add = tk.Button(self.root, text="Добавить", font=("Arial", 20, "bold"),
                            command=self.save_file)
        btn_add.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=15)

    def save_file(self):
        file_name = self.entry.get().strip()

        if not file_name:
            print("Введите имя файла!")
            return

            # Запрещённые символы
        forbidden = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        if any(c in file_name for c in forbidden):
            print("Имя содержит недопустимые символы!")
            return

        # Добавляем расширение
        if not file_name.endswith(".csv"):
            file_name += ".csv"

        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", file_name)

        # Проверка на существование
        if os.path.exists(file_path):
            print(f"Файл '{file_name}' уже существует!")
            return

        self.entry.delete(0, tk.END)

        # Создание
        pd.DataFrame(columns=["day", "value"]).to_csv(file_path, index=False)
        self.manager.show_file_setting_win()
        print(f"Файл '{file_name}' создан!")

        print(self.manager.current_window)


