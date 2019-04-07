from tkinter                        import Button, Toplevel

from .time_entry_widget  import TimeEntryWidget


class TimeEntryBox(Toplevel):
    """
    """

    def __init__(self, controller, window_title):
        super().__init__()
        self.title(window_title)
        self.controller = controller

        self._create()
        self._arrange()

    def _create(self):
        self.time_entry = TimeEntryWidget(self)
        self.confirm = Button(self, text = "Confirm",
                                command = lambda: self.controller.
                                                    confirm_callback(
                                                    self.retrieve_and_close))
        self.bind("<Return>", lambda event: self.controller.
                                    confirm_callback(self.retrieve_and_close))
        self.cancel = Button(self, text = "Cancel", 
                                command = lambda: self.destroy())
        self.bind("<Escape>", lambda event: self.destroy())
    
    def _arrange(self):
        self.time_entry.grid(row = 0, column = 0, columnspan = 2)
        self.cancel.grid(row = 1, column = 0)
        self.confirm.grid(row = 1, column = 1)

    def retrieve_and_close(self):
        time = self.time_entry.get_time_in_ms()
        self.destroy()
        return time
