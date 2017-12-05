from tkinter import Button, Label, NO, StringVar, Tk, X


class StopwatchView:
    BACKGROUND_COLOR = "black"
    FOREGROUND_COLOR = "#00F900"
    FONT = ("Courier Prime Code", 36)

    def __init__(self):
        self.root = self._initialize_root()

        self.timer_label = None
        self.start_stop_button = None
        self.reset_button = None

        self.stopwatch_label_var = StringVar()

        self._initialize_widgets()
        self._place_widgets()

    def change_start_stop_text(self, new_text):
        self.start_stop_button.config(text=new_text)

    def get_label_var(self):
        return self.stopwatch_label_var

    def get_root(self):
        return self.root

    def set_reset_button_command(self, function):
        self.reset_button.config(command = function)
        
    def set_start_stop_button_command(self, function):
        self.start_stop_button.config(command = function)

    def start(self):
        self.root.mainloop()

    def _initialize_root(self):
        root = Tk()
        root.title("PyTimer")
        root.config(bg=self.BACKGROUND_COLOR)
        root.wm_attributes("-topmost", True)   # keep window on top
        
        return root

    def _initialize_widgets(self):
        self.timer_label = Label(self.root, textvariable=self.stopwatch_label_var)
        self.timer_label.config(fg=self.FOREGROUND_COLOR, bg=self.BACKGROUND_COLOR, font=self.FONT)

        self.start_stop_button = Button(self.root, text="Start")
        self.start_stop_button.config(highlightbackground=self.BACKGROUND_COLOR)

        self.reset_button = Button(self.root,text="Reset")
        self.reset_button.config(highlightbackground=self.BACKGROUND_COLOR)

    def _place_widgets(self):
        self.timer_label.pack(fill=X, expand=NO)
        self.start_stop_button.pack(fill=X)
        self.reset_button.pack(fill=X)
