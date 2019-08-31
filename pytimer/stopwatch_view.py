from tkinter            import Button, Label, StringVar, NO, X

from chadlib.gui        import View
from chadlib.utility    import event_wrapper


class StopwatchView(View):
    """
    """

    def _create_widgets(self):
        self.stopwatch_label_var = StringVar()
        self.timer_label = Label(self, textvariable = self.stopwatch_label_var, 
                                    font = ("Arial", 36))

        self.toggle = Button(self, text = "Start/Stop", 
                                command = self.controller.toggle_timer)

        self.reset = Button(self, text = "Reset",
                            command = self.controller.reset_timer)

    def _arrange_widgets(self):
        self.timer_label.pack(fill = X, expand = NO)
        self.toggle.pack(fill = X)
        self.reset.pack(fill = X)

    def _bind_actions(self):
        self.timer_label.bind("<Button-1>", event_wrapper(
                                        self.controller.get_new_time))
