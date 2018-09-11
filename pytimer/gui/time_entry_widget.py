from tkinter            import Entry, Frame, Label, StringVar

from pytimer.stopwatch  import Stopwatch


class TimeEntryWidget(Frame):
    """
    """

    HOURS_LENGTH = 2
    MINUTES_LENGTH = 2
    SECONDS_LENGTH = 5

    def __init__(self, root):
        super().__init__(root)
        
        self._create()
        self._arrange()

    def _create(self):
        self.hours_var = StringVar()
        self.hours_var.trace('w', lambda *args: 
                                    self._enforce_length(self.hours_var, 
                                                        self.HOURS_LENGTH))
        self.hours_entry = Entry(self, textvariable = self.hours_var, 
                                width = self.HOURS_LENGTH)
        self.hours_entry.focus()
        

        self.hm_separator = Label(self, text = ":")

        self.minutes_var = StringVar()
        self.minutes_var.trace('w', lambda *args: 
                                    self._enforce_length(self.minutes_var, 
                                                        self.MINUTES_LENGTH))
        self.minutes_entry = Entry(self, textvariable = self.minutes_var, 
                                    width = self.MINUTES_LENGTH)

        self.ms_separator = Label(self, text = ":")

        self.seconds_var = StringVar()
        self.seconds_var.trace('w', lambda *args: 
                                    self._enforce_length(self.seconds_var, 
                                                        self.SECONDS_LENGTH))
        self.seconds_entry = Entry(self, textvariable = self.seconds_var,
                                    width = self.SECONDS_LENGTH)
        
    def _arrange(self):
        self.hours_entry.grid(row = 0, column = 0)
        self.hm_separator.grid(row = 0, column = 1)
        self.minutes_entry.grid(row = 0, column = 2)
        self.ms_separator.grid(row = 0, column = 3)
        self.seconds_entry.grid(row = 0, column = 4)

    def _enforce_length(self, string_var, length):
        """
        """
        string_var.set(string_var.get()[:length])

    def get_time_string(self):
        hours = self.hours_var.get()
        if hours == "":
            hours = 0
        minutes = self.minutes_var.get()
        if minutes == "":
            minutes = 0
        seconds = self.seconds_var.get()
        if seconds == "":
            seconds = 0
        
        return "{}:{}:{}".format(hours, minutes, seconds)

    def get_time_in_ms(self):
        return Stopwatch.time_str_to_ms(self.get_time_string())
