from updater import Updater

def main():
    updater = Updater(current_version="v1.0.0")
    updater.check_and_update()

    # Основной код программы
    from window_manager import WindowManager
    app = WindowManager()
    app.show_menu_win()

if __name__ == "__main__":
    main()