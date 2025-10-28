from src.ui import main
from src.ui import SelectLang
from src.utils import *
import logging
import json
import tkinter as tk
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Main")

TITLE = "Mai AI v0.1"

def main_loader():
    logger.info("Main Loader Started")
    path = os.path.abspath(os.path.dirname(__file__))
    #load settings.json
    with open("settings.json", "r", encoding="utf-8") as f:
        settings:dict = json.load(f)
    settings["path"] = path
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
    if settings["user_language"] == "":
        logger.info("No language selected, please select a language.")
        select_lang_window = SelectLang.SelectLangWindow(geometry="300x100", title="Language Selector", lang_list=get_lang_list())
        select_lang_window.position_center()
        select_lang_window.mainloop()
    if settings["oobe"]:
        oobe_loader(settings)
    else:
        app_loader(settings)

def oobe_loader(base_settings:dict):
    logger.info("OOBE Loader Started")
    tk_instance = tk.Tk()
    screen_params = tk_instance.winfo_screenwidth(), tk_instance.winfo_screenheight() # 获取屏幕分辨率 w,h
    app_width = screen_params[0] // 3 * 2
    app_height = screen_params[1] // 4 * 3
    app_appear = (screen_params[0]) // 2, (screen_params[1]) // 2
    app_config = f"{app_width}x{app_height}+{app_appear[0]}+{app_appear[1]}"
    user_screen_size = "{}x{}".format(screen_params[0], screen_params[1])
    base_settings["user_screen_size"] = user_screen_size
    base_settings["user_mainwindow_params"] = app_config
    base_settings["oobe"] = False
    
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(base_settings, f, indent=4)
    logger.info(f"Screen settings saved to settings.json")
    main_window = main.MainApplication(geometry=base_settings["user_mainwindow_params"],
                                       title=TITLE)
    main_window.mainloop()
def app_loader(base_settings:dict):
    logger.info("App Loader Started")

    main_window = main.MainApplication(geometry=base_settings["user_mainwindow_params"],
                                       title=TITLE)
    main_window.mainloop()

    
if __name__ == '__main__':
    main_loader()