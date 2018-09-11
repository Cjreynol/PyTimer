from tkinter                import Button, Entry, Frame, Label, Toplevel

from pytimer.split_handler  import SplitHandler
from pytimer.stopwatch      import Stopwatch


class NewSplitEntry:
    """
    """

    def __init__(self, controller):
        self.window = Toplevel()
        self.window_title = "Enter New Split Information"
        self.controller = controller

        self._create()
        self._arrange()

    def _create(self):
        self.title_label = Label(self.window, text = "Title")
        self.title_entry = Entry(self.window)

        self.new_segment_button = Button(self.window, text = "New Segment",
                                            command = self._add_segment) 
        self.segment_area = Frame(self.window)
        self.segments = []

        self.confirm_button = Button(self.window, 
                                text = "Confirm",
                                command = lambda: 
                self.controller.new_split_callback(self._retrieve_and_close))
        self.window.bind("<Return>", 
                            lambda event: 
                self.controller.new_split_callback(self._retrieve_and_close))

        self.cancel_button = Button(self.window, 
                                text = "Cancel", 
                                command = lambda: self.window.destroy())
        self.window.bind("<Escape>", lambda event: self.window.destroy())

    def _arrange(self):
        self.title_label.grid(row = 0, column = 0)
        self.title_entry.grid(row = 0, column = 1)
        self.new_segment_button.grid(row = 1, column = 0)
        self.segment_area.grid(row = 2, column = 0, columnspan = 2)
        self.cancel_button.grid(row = 3, column = 0)
        self.confirm_button.grid(row = 3, column = 1)

    def _add_segment(self):
        new_segment = self.AddSegmentFrame(self.segment_area)
        new_segment.pack()
        self.segments.append(new_segment)

    def _retrieve_and_close(self):
        data_dict = {
            SplitHandler.VERSION_KEY: SplitHandler.CURRENT_FILE_VERSION,
            SplitHandler.TITLE_KEY: self.title_entry.get(),
            SplitHandler.SEGMENTS_KEY: [segment.get_data() 
                                        for segment in self.segments]
        }
        
        self.window.destroy()
        return data_dict


    class AddSegmentFrame(Frame):
        """
        """

        def __init__(self, root):
            super().__init__(root)

            self._create()
            self._arrange()

        def _create(self):
            self.name_label = Label(self, text = "Name")
            self.name_entry = Entry(self)

            self.time_label = Label(self, text = "Best Time")
            self.hour_entry = Entry(self, width = 2)
            self.minute_entry = Entry(self, width = 2)
            self.second_entry = Entry(self, width = 5)

        def _arrange(self):
            self.name_label.grid(row = 0, column = 0)
            self.name_entry.grid(row = 1, column = 0)

            self.time_label.grid(row = 0, column = 1)
            self.hour_entry.grid(row = 1, column = 1)
            self.minute_entry.grid(row = 1, column = 2)
            self.second_entry.grid(row = 1, column = 3)

        def get_data(self):
            hours = self.hour_entry.get()
            if hours == "":
                hours = 0
            minutes = self.minute_entry.get()
            if minutes == "":
                minutes = 0
            seconds = self.second_entry.get()
            if seconds == "":
                seconds = 0
            
            time_string = "{}:{}:{}".format(hours, minutes, seconds)
            data_dict = {
                SplitHandler.Segment.LABEL_KEY: self.name_entry.get(),
                SplitHandler.Segment.BEST_TIME_KEY: 
                                        Stopwatch.time_str_to_ms(time_string)
            }
            return data_dict
