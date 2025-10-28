import ttkbootstrap as ttk
import logging
from src.utils.LoadLang import load_lang

logger = logging.getLogger("UI_Main")
logger.setLevel(logging.INFO)

class MainApplication(ttk.Window):
    def __init__(self,geometry,title,lang):
        super().__init__(themename="darkly")
        self.title(title)
        # self.iconbitmap("res\\icon.ico")
        self.geometry(geometry)
        
        self.lang_data = load_lang(lang)["UI"]

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=20)
        self.input_bar = ttk.Entry(self.input_frame,
                                   textvariable=ttk.StringVar(value=self.lang_data["app_input_bar_placeholder"]),width=40)
        self.left_column = ttk.Frame(self)
        self.left_column.pack(side=ttk.LEFT, fill=ttk.Y , expand=True)
        self.right_column = ttk.Frame(self)
        self.right_column.pack(side=ttk.RIGHT, fill=ttk.Y, expand=True)
        self.label = ttk.Label(self.right_column, text="Hello World!",foreground="#107bd2")
        self.label.pack(padx=10, pady=10)
        self.button = ttk.Button(self.left_column, text="Click Me!", command=self.on_button_click)
        self.button.pack( padx=10, pady=10)

        
    def on_button_click(self):
        self.label.config(text="Button Clicked!")