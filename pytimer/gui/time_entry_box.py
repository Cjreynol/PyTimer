from tkinter import Button, Entry, Toplevel


class TimeEntryBox:
    """
    """

    def __init__(self, controller, window_title):
        self.window = Toplevel()
        self.window.title(window_title)
        self.controller = controller
        self._create()
        self._arrange()

    def _create(self):
        self.hour_entry = Entry(self.window, width = 2)
        self.minute_entry = Entry(self.window, width = 2)
        self.second_entry = Entry(self.window, width = 5)

        self.confirm = Button(self.window, 
                                text = "Confirm",
                                command = lambda: self.controller.confirm_callback(self.retrieve_and_close))
        self.window.bind("<Return>", lambda event: self.controller.confirm_callback(self.retrieve_and_close))

        self.cancel = Button(self.window, 
                                text = "Cancel", 
                                command = lambda: self.window.destroy())
    
    def _arrange(self):
        self.hour_entry.grid(row = 0, column = 0)
        self.minute_entry.grid(row = 0, column = 1)
        self.second_entry.grid(row = 0, column = 2)
        self.hour_entry.focus()

        self.cancel.grid(row = 1, column = 1)
        self.confirm.grid(row = 1, column = 2)

    def retrieve_and_close(self):
        time_str = self._get_time_string()
        self.window.destroy()
        return time_str

    def _get_time_string(self):
        hours = self.hour_entry.get()
        if hours == "":
            hours = 0
        minutes = self.minute_entry.get()
        if minutes == "":
            minutes = 0
        seconds = self.second_entry.get()
        if seconds == "":
            seconds = 0
        
        return "{}:{}:{}".format(hours, minutes, seconds)
