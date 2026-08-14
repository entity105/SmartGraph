import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from windows.base_window import BaseWindow
import os

class GraphInterface(BaseWindow):
    is_over = False

    def __init__(self, manager, title="Работа с графиком", size="1200x600"):
        self.input_field = None
        super().__init__(manager, title, size)

        self.fig, self.ax = None, None
        self.canvas = None
        self.draw_graph()

    def setup(self):
        buttons_frame = tk.Frame(self.root, bd=2, relief="solid", padx=20)
        buttons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        btn_back = tk.Button(buttons_frame, text="Назад", height=1, font=("Arial", 15, "bold"), width=20,
                             command=self.manager.show_menu_win)
        btn_back.pack(pady=20)

        btn_add = tk.Button(buttons_frame, text="Сохранить", height=1, font=("Arial", 15, "bold"), width=20,
                            command=self.save_data)
        btn_add.pack(pady=5)

        self.input_field = tk.Entry(buttons_frame, font=("Arial", 15, "bold"))
        self.input_field.pack()

        btn_change = tk.Button(buttons_frame, text="Изменить данные", font=("Arial", 15, "bold"),
                               command=self.manager.show_change_data_win)
        btn_change.pack(anchor='s', pady=100)

        btn_exit = tk.Button(buttons_frame, text="Выход", font=("Arial", 15, "bold"),
                             command=self.exit_program)
        btn_exit.pack(side=tk.BOTTOM, pady=5)

    def save_data(self):
        data_row = self.input_field.get()
        if data_row.strip():
            print(f"Введено: {data_row}")
            self.input_field.delete(0, tk.END)  # очистить поле
        else:
            print("Поле пустое!")

        val = self.float_parse(data_row)
        if val:
            self.update_csv(self.current_file, val)
            self.update_graph(self.current_file)

    @staticmethod
    def update_csv(path:str, value):
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            df = pd.DataFrame(columns=["day", "value"])
            df.to_csv(path, index=False)

        df = pd.read_csv(path)
        last_day = df.iloc[-1, 0] if len(df) > 0 else 0
        new_row = pd.DataFrame([[last_day+1, value]], columns=df.columns)
        df_res = pd.concat([df, new_row], ignore_index=True)
        df_res.to_csv(path, index=False)

    def float_parse(self, inpt: str) -> float | None:
        try:
            res = float(inpt)
            label_success = tk.Label(self.root, text="Засчитано", fg="#18bc3b", bg="#a2f3b3")
            label_success.place(x=40, y=173, width=220)
            self.root.after(3000, lambda: label_success.destroy())
            return res
        except (TypeError, ValueError):
            label_error = tk.Label(self.root, text="Неверный ввод", fg="#700314", bg="#f6afb5")
            label_error.place(x=40, y=173, width=220)
            self.root.after(3000, lambda: label_error.destroy())

    def update_graph(self, path:str):
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            return
        df = pd.read_csv(path)
        x = df.iloc[:, 0].values
        y = df.iloc[:, 1].values
        if hasattr(self, 'line'):
            self.line.set_data(x, y)
            self.ax.relim()
            self.ax.autoscale()
        else:
            self.line, = self.ax.plot(x, y)
        self.ax.scatter(x, y, color='red')
        self.canvas.draw()

    def draw_graph(self):
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.ax.grid(True)
        self.ax.set_title("График")
        self.ax.set_xlabel("t, день")
        self.ax.set_ylabel("w, значение")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.update_graph(self.current_file)

    def close_win(self):
        super().close_win()
        plt.close('all')
        self.manager.show_menu_win()
