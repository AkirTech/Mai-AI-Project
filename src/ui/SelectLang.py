import ttkbootstrap as ttk
import logging
import json
import os

TITLES = ["Select Language", "选择语言", "Sélectionner la langue", 
            "Sprache auswählen", "Seleccionar idioma","言語を選択する",
            "選擇語言"]
CONFIRM_BUTTON_TEXTS = ["Confirm", "确认", "Confirmer", "Bestätigen",
                         "Confirmar","確認","選擇"]

def get_lang_list(path) -> list:
    lang_list = os.listdir(f"{path}"+"\\src\\res\\lang")
    return [lang.replace(".json","") for lang in lang_list]

logger = logging.getLogger("Language Selector")
logger.setLevel(logging.INFO)
logger.info("Language Selector Started")
with open("settings.json", "r", encoding="utf-8") as f:
    settings:dict = json.load(f)
path = settings["path"]
lang_list = get_lang_list(path)

class SelectLangWindow(ttk.Window):
    def __init__(self,path:str):
        super().__init__(themename="darkly")
        title = TITLES[0]
        self.title(title)
        # self.iconbitmap("res\\icon.ico")
        geometry = "400x200"
        self.geometry(geometry)
        self.lang_list = get_lang_list(path)
        self.title_index = 0
        self.lang_var = ttk.StringVar(value=lang_list[0])
        self.lang_selector = ttk.Combobox(self, values=self.lang_list, textvariable=self.lang_var)
        self.lang_selector.pack(pady=20)
        self.select_button = ttk.Button(self, text=CONFIRM_BUTTON_TEXTS[0], command=self.on_confirm_click)
        self.select_button.pack(padx=10, pady=10)
        self.after(2000, self.change_title_lang)

    def on_confirm_click(self):
        settings["user_language"] = self.lang_var.get()
        with open("settings.json", "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4)
        logger.info(f"Language selected: {settings['user_language']}")
        self.destroy()
    def change_title_lang(self):
        current_title = TITLES[self.title_index % len(TITLES)]
        current_confirm = CONFIRM_BUTTON_TEXTS[self.title_index % len(CONFIRM_BUTTON_TEXTS)]
        self.title_index += 1
        self.title(current_title)
        self.select_button.config(text=current_confirm)
        self.select_button.update()
        self.update()
        self.after(2000, self.change_title_lang)
        

if __name__ == '__main__':
    selector = SelectLangWindow(path=path)
    selector.position_center()
    selector.mainloop()