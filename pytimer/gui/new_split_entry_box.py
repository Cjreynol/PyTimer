from tkinter                        import (Button, Entry, Frame, Label, 
                                            Toplevel)

from pytimer.split_handler          import SplitHandler
from pytimer.gui.time_entry_widget  import TimeEntryWidget


class NewSplitEntryBox(Toplevel):
    """
    """

    def __init__(self, controller):
        super().__init__()
        self.title("Enter New Split Information")
        self.controller = controller

        self._create()
        self._arrange()

    def _create(self):
        self.title_label = Label(self, text = "Title")
        self.title_entry = Entry(self)

        self.new_segment_button = Button(self, text = "New Segment",
                                            command = self._add_segment) 
        self.segment_area = Frame(self)
        self.segments = []

        self.confirm_button = Button(self, 
                                text = "Confirm",
                                command = lambda: 
                self.controller.new_split_callback(self._retrieve_and_close))
        self.bind("<Return>", 
                            lambda event: 
                self.controller.new_split_callback(self._retrieve_and_close))

        self.cancel_button = Button(self, 
                                text = "Cancel", 
                                command = lambda: self.destroy())
        self.bind("<Escape>", lambda event: self.destroy())

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
        
        self.destroy()
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
            self.time_entry = TimeEntryWidget(self)

        def _arrange(self):
            self.name_label.grid(row = 0, column = 0)
            self.name_entry.grid(row = 1, column = 0)

            self.time_label.grid(row = 0, column = 1)
            self.time_entry.grid(row = 1, column = 1)

        def get_data(self):
            data_dict = {
                SplitHandler.Segment.LABEL_KEY: 
                                            self.name_entry.get(),
                SplitHandler.Segment.BEST_TIME_KEY: 
                                            self.time_entry.get_time_in_ms()
            }
            return data_dict
