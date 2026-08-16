import requests
import os
import sys
import tkinter as tk
from tkinter import messagebox

class Updater:
    def __init__(self, current_version):
        self.current_version = current_version

    def get_latest_release(self):
        url = "https://api.github.com/repos/entity105/SmartGraph/releases/latest"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                data = response.json()
                return data["tag_name"], data["assets"][0]["browser_download_url"]
        except:
            pass
        return None, None

    def check_and_update(self, parent=None):
        latest, download_url = self.get_latest_release()
        if not latest:
            return

        if latest == self.current_version:
            print("Версия актуальна")
            return

        # Спрашиваем пользователя
        answer = messagebox.askyesno(
            "Обновление",
            f"Доступна новая версия {latest}\nУстановить?"
        )
        if not answer:
            return

        # Скачиваем
        try:
            response = requests.get(download_url, stream=True)
            with open("app_new.exe", "wb") as f:
                for chunk in response.iter_content(8192):
                    f.write(chunk)

            messagebox.showinfo("Обновление", "Обновление установлено!")
            os.startfile("app_new.exe")
            sys.exit(0)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось скачать обновление: {e}")