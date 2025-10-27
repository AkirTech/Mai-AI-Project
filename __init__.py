from src.ui import main
from src.utils import *
import logging
import json
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Main")

def main_loader():
    logger.info("Main Loader Started")
    #load settings.json
    with open("settings.json", "r", encoding="utf-8") as f:
        settings:dict = json.load(f)
    if settings["oobe"]:
        oobe_loader(settings)
    else:
        app_loader(settings)

def oobe_loader(base_settings:dict):
    logger.info("OOBE Loader Started")

def app_loader(base_settings:dict):
    logger.info("App Loader Started")

    main_window = main.MainApplication()
    main_window.mainloop()

    
if __name__ == '__main__':
    main_loader()