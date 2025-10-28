import os
import json

def load_lang(user_lang:str) -> dict:
    """Load lang from a JSON file."""
    with open("settings.json", "r", encoding="utf-8") as f:
        settings:dict = json.load(f)
    path = settings["path"]
    file_path = os.path.join(path, "src\\res\\lang", f"{user_lang}.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
