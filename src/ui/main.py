<<<<<<< Updated upstream
@ -0,0 +1,29 @@
=======
>>>>>>> Stashed changes
import ttkbootstrap as ttk
import logging

logger = logging.getLogger("UI_Main")
logger.setLevel(logging.INFO)

class MainApplication(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Main Application")
        # self.iconbitmap("res\\icon.ico")
        self.geometry("400x300")
        

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=20)
        self.input_bar = ttk.Entry(self.input_frame,textvariable=ttk.StringVar(value="Start chating here..."),width=40)
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