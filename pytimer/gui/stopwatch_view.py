from tkinter    import Button, Frame, Label, StringVar, NO, X


class StopwatchView(Frame):
    """
    Provides an interface for the controller to the GUI code.
    """

    WINDOW_TITLE = "PyTimer"

    RESET_LABEL = "Reset"
    TOGGLE_LABEL = "Start/Stop"

    BACKGROUND_COLOR = "#000000"
    FOREGROUND_COLOR = "#00F900"

    FONT = ("Arial", 36)

    def __init__(self, root, controller):
        super().__init__(root)

        self.controller = controller
        self.stopwatch_label_var = StringVar()

        self._create()
        self._arrange()

    def _create(self):
        self.timer_label = Label(self, 
                                    textvariable=self.stopwatch_label_var, 
                                    fg=self.FOREGROUND_COLOR, 
                                    bg=self.BACKGROUND_COLOR, 
                                    font=self.FONT)
        self.timer_label.bind("<Button-1>", lambda event: 
                                        self.controller.set_time_callback())

        self.toggle = Button(self, 
                                text = self.TOGGLE_LABEL, 
                                command = self.controller.toggle_callback, 
                                highlightbackground = self.BACKGROUND_COLOR)

        self.reset = Button(self, 
                            text = self.RESET_LABEL,
                            command = self.controller.reset_callback,
                            highlightbackground = self.BACKGROUND_COLOR)

    def _arrange(self):
        self.timer_label.pack(fill = X, expand = NO)
        self.toggle.pack(fill = X)
        self.reset.pack(fill = X)
