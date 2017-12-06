from tkinter import Button, Label, NO, StringVar, Tk, X


class StopwatchView:
    """
    Provides an interface for the controller to the GUI code.
    """

    BACKGROUND_COLOR = "black"
    FOREGROUND_COLOR = "#00F900"
    FONT = ("Arial", 36)

    def __init__(self):
        self.root = self._initialize_root()

        self.timer_label = None
        self.start_stop_button = None
        self.reset_button = None

        self.stopwatch_label_var = StringVar()

        self._initialize_widgets()
        self._place_widgets()

    def add_quit_function(self, function):
        self.root.protocol("WM_DELETE_WINDOW", function)

    def change_start_stop_text(self, new_text):
        """Updates the text of the start/stop button."""
        self.start_stop_button.config(text=new_text)

    def get_label_var(self):
        """Returns the StringVar connected to the timer display Label."""
        return self.stopwatch_label_var

    def quit(self):
        self.root.destroy()

    def set_reset_button_command(self, function):
        self.reset_button.config(command = function)
        
    def set_start_stop_button_command(self, function):
        self.start_stop_button.config(command = function)

    def start(self):
        """Begins the execution of the Tk window."""
        self.root.mainloop()

    def _initialize_root(self):
        """Creates and sets up the initial window with the correct properties."""
        root = Tk()
        root.title("PyTimer")
        root.config(bg=self.BACKGROUND_COLOR)
        root.wm_attributes("-topmost", True)   # keep window on top
        
        return root

    def _initialize_widgets(self):
        """Creates and sets up the widgets for the stopwatch."""
        self.timer_label = Label(self.root, textvariable=self.stopwatch_label_var)
        self.timer_label.config(fg=self.FOREGROUND_COLOR, bg=self.BACKGROUND_COLOR, font=self.FONT)

        self.start_stop_button = Button(self.root, text="Start")
        self.start_stop_button.config(highlightbackground=self.BACKGROUND_COLOR)

        self.reset_button = Button(self.root,text="Reset")
        self.reset_button.config(highlightbackground=self.BACKGROUND_COLOR)

    def _place_widgets(self):
        """Handles widget placement onto the window."""
        self.timer_label.pack(fill=X, expand=NO)
        self.start_stop_button.pack(fill=X)
        self.reset_button.pack(fill=X)
