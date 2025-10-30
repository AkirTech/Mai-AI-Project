import ttkbootstrap as ttk
import logging
from src.utils.LoadLang import load_lang
from src.utils.GetAIAnswer import get_ai_answer,langchain_get_ai_answer
from src.utils.GS_Process import sget_audio, play_audio

logger = logging.getLogger("UI_Main")
logger.setLevel(logging.INFO)

class MainApplication(ttk.Window):
    def __init__(self,geometry,title,lang):
        super().__init__(themename="darkly")
        self.title(title)
        # self.iconbitmap("res\\icon.ico")
        self.geometry(geometry)
        
        self.lang_data = load_lang(lang)["UI"]
        logger.info(f"Language loaded: {lang}")

        self.history = []

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)

        self.down_frame = ttk.Frame(self)
        self.down_frame.pack()

        
        self.left_column = ttk.Frame(self.down_frame)
        self.left_column.pack(side=ttk.LEFT, fill=ttk.Y , expand=True)
        self.right_column = ttk.Frame(self.down_frame)
        self.right_column.pack(side=ttk.RIGHT, fill=ttk.Y, expand=True)

        self.input_bar = ttk.Entry(self.input_frame,
                            textvariable=ttk.StringVar(value=self.lang_data["app_input_bar_placeholder"]),
                            width=50,foreground="#727272")
        self.input_bar.pack(padx=10, pady=10,fill="x",anchor=ttk.N)

        self.top_k_label = ttk.Label(self.left_column, text=self.lang_data["app_top_k_label"])
        self.top_k_label.pack(padx=5, pady=(100,0),fill="x",anchor=ttk.N)
        self.top_k_scale = ttk.Scale(self.left_column, from_=20, to=80,length=200, orient=ttk.HORIZONTAL)
        self.top_k_scale.pack(padx=5, pady=10,fill="x",anchor=ttk.N)

        self.button = ttk.Button(self.left_column,width=40, text=self.lang_data["app_input_bar_button"], command=self.on_button_click)
        self.button.pack( padx=10, pady=10)
        self.out_label = ttk.Label(self.right_column, text="What AI output will be displayed here.",width=60)
        self.out_label.pack(padx=10, pady=10)
        self.sizegrip = ttk.Sizegrip(self.down_frame)
        self.sizegrip.pack(side=ttk.BOTTOM, anchor=ttk.SE)

        
    def on_button_click(self):
        self.user_prompt = self.input_bar.get()
        self.top_k = int(self.top_k_scale.get())
        self.ai_answer = get_ai_answer(prompt=self.user_prompt,history = self.history)
        tmp_to_append = {"user":self.user_prompt, "assistant":self.ai_answer}
        self.history.append(tmp_to_append)
        self.out_label.config(text=self.ai_answer)
        # sget_audio(content=self.ai_answer,lang="en",top_k=self.top_k,temperature=1,
        #            ref_audio_path="res\\ref_audio.wav",prompt_text=self.user_prompt,prompt_lang="en")
        """Wait for implementing sget_audio function.
            Considering whether to use emotion recognition to adjust the tone of TTS."""
