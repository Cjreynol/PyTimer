from tkinter import Button, Label, StringVar, Tk, NO, X


class View:
    """
    Provides an interface for the controller to the GUI code.
    """

    WINDOW_TITLE = "PyTimer"

    RESET_LABEL = "Reset"
    START_LABEL = "Start"
    STOP_LABEL = "Stop"

    BACKGROUND_COLOR = "#000000"
    FOREGROUND_COLOR = "#00F900"

    FONT = ("Arial", 36)

    def __init__(self, controller):
        self.controller = controller
        self.root = self._create_root()

        self.stopwatch_label_var = StringVar()

        self._create()
        self._arrange()

    def change_start_stop_text(self, new_text):
        self.toggle.config(text = new_text)

    def quit(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()

    def _create_root(self):
        root = Tk()
        root.title(self.WINDOW_TITLE)
        root.config(bg=self.BACKGROUND_COLOR)
        root.protocol("WM_DELETE_WINDOW", self.controller.quit)
        root.bind("<Escape>", lambda event: self.controller.quit())
        
        return root

    def _create(self):
        self.timer_label = Label(self.root, textvariable=self.stopwatch_label_var, 
                                    fg=self.FOREGROUND_COLOR, 
                                    bg=self.BACKGROUND_COLOR, 
                                    font=self.FONT)
        self.timer_label.bind("<Button-1>", lambda event: 
                                        self.controller.set_time_callback())

        self.toggle = Button(self.root, 
                                text = self.START_LABEL, 
                                command = self.controller.control_callback, 
                                highlightbackground = self.BACKGROUND_COLOR)
        self.root.bind("<space>", lambda event: self.toggle.invoke())

        self.reset = Button(self.root, 
                                text = self.RESET_LABEL,
                                command = self.controller.reset_callback,
                                highlightbackground = self.BACKGROUND_COLOR)

    def _arrange(self):
        self.timer_label.pack(fill = X, expand = NO)
        self.toggle.pack(fill = X)
        self.reset.pack(fill = X)
