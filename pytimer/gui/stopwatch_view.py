from tkinter        import StringVar, NO, X
from tkinter.ttk    import Button, Frame, Label


class StopwatchView(Frame):
    """
    Provides an interface for the controller to the GUI.
    """

    def __init__(self, root, controller):
        super().__init__(root)

        self.controller = controller
        self.stopwatch_label_var = StringVar()

        self._create()
        self._arrange()
        self._bind()

    def _create(self):
        self.timer_label = Label(self, textvariable = self.stopwatch_label_var, 
                                    font = ("Arial", 36))

        self.toggle = Button(self, text = "Start/Stop", 
                                command = self.controller.toggle_callback)

        self.reset = Button(self, text = "Reset",
                            command = self.controller.reset_callback)

    def _arrange(self):
        self.timer_label.pack(fill = X, expand = NO)
        self.toggle.pack(fill = X)
        self.reset.pack(fill = X)

    def _bind(self):
        self.timer_label.bind("<Button-1>", lambda event: 
                                        self.controller.set_time_callback())
