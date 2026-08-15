import tkinter as tk
from windows.base_window import BaseWindow
import os

class SettingFileInterface(BaseWindow):
    is_over = False

    def __init__(self, manager, title="Настройка файла", size="1200x600"):
        self.listbox = None
        super().__init__(manager, title, size)

    def setup(self):
        buttons_frame = tk.Frame(self.root, bd=2, relief="solid")
        buttons_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        btn_back = tk.Button(buttons_frame, text="Завершить", height=1, font=("Arial", 15, "bold"), width=20,
                             command=self.manager.show_menu_win)
        btn_back.pack(side=tk.LEFT)

        btn_new_file = tk.Button(buttons_frame, text="Добавить файл",
                                 height=1, font=("Arial", 15, "bold"), width=25,
                                 command=self.manager.show_edit_file_win)
        btn_new_file.pack(side=tk.LEFT)

        btn_del_file = tk.Button(buttons_frame, text="Удалить файл",
                                 height=1, font=("Arial", 15, "bold"), width=25,
                                 command=self.delete_file
                                 )
        btn_del_file.pack(side=tk.LEFT)

        btn_select_file = tk.Button(buttons_frame, text="Выбрать файл", height=1, font=("Arial", 15, "bold"), width=28,
                                    command=self.select_file)
        btn_select_file.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(self.root, height=20, font=("Arial", 14), selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.load_files()

    def load_files(self):
        self.listbox.delete(0, tk.END)
        data_dir = "data"

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
        for file in files:
            self.listbox.insert(tk.END, file)

    def select_file(self):
        selection = self.listbox.curselection()
        if not selection:
            print('Файл не выбран')
            lable_err = tk.Label(self.root, text="Выберите файл", fg="#700314", bg="#f6afb5")
            lable_err.place(x=930, y=50, width=250)
            self.root.after(1500, lambda: lable_err.destroy())
            return

        selected_file = self.listbox.get(selection[0])
        file_path = os.path.join("data", selected_file)
        self.manager.current_file = file_path
        self.save_file_path(file_path)

        label_success = tk.Label(self.root, text=f"Выбранный файл: {os.path.basename(file_path)}",
                                 font=("Arial", 12, "bold"))
        label_success.place(x=930, y=50)
        print(f"Выбран файл: {file_path}")

    def delete_file(self):
        """Удаляет выбранный файл из списка и с диска"""
        selection = self.listbox.curselection()
        if not selection:
            print("Файл не выбран")
            return

        # Получаем имя файла
        file_name = self.listbox.get(selection[0])
        file_path = os.path.join("data", file_name)

        # Подтверждение удаления
        confirm = tk.messagebox.askyesno(
            "Подтверждение",
            f"Удалить файл '{file_name}'?"
        )
        if not confirm:
            return

        try:
            os.remove(file_path)
            self.listbox.delete(selection[0])  # удаляем из списка
            print(f"Файл {file_name} удалён")

            # Если файлов не осталось — очищаем выделение
            if self.listbox.size() == 0:
                self.manager.current_file = None

        except Exception as e:
            print(f"Ошибка удаления: {e}")

    @staticmethod
    def save_file_path(file_path: str):
        with open("__last_file.txt", "w", encoding="utf-8") as f:
            f.write(file_path)