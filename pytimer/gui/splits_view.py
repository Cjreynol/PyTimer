from tkinter            import StringVar
from tkinter.ttk        import Button, Frame, Label

from pytimer.stopwatch  import Stopwatch


class SplitsView(Frame):
    """
    """

    def __init__(self, root, controller):
        super().__init__(root)

        self.controller = controller

        self._create()
        self._arrange()

    def _create(self):
        self.title_label = Label(self, text = "--")
        self.split_button = Button(self, text = "Split", 
                                command = self.controller.split_callback)
        self.skip_split_button = Button(self, text = "Skip Split",
                                    command = 
                                        self.controller.skip_split_callback)

        self.name_header = Label(self, text = "Name".ljust(20))
        self.difference_header = Label(self, text = "| Diff".ljust(8))
        self.best_header = Label(self, text = "| Best Run".ljust(11))

        self.segment_area = Frame(self)
        self.segments = []

        self.open_button = Button(self, text = "Open Split", 
                            command = self.controller.open_callback)
        self.new_button = Button(self, text = "New Split",
                            command = self.controller.new_callback)

    def _arrange(self):
        self.title_label.grid(row = 0, column = 0, columnspan = 3)
        self.split_button.grid(row = 1, column = 0, columnspan = 2)
        self.skip_split_button.grid(row = 1, column = 2, columnspan = 2)

        self.name_header.grid(row = 2, column = 0)
        self.difference_header.grid(row = 2, column = 1)
        self.best_header.grid(row = 2, column = 2)

        self.segment_area.grid(row = 3, column = 0, columnspan = 3)
        for segment in self.segments:
            segment.pack()

    def update(self, title, segments_data):
        self.title_label["text"] = title
        for widget in self.segment_area.winfo_children():
            widget.destroy()

        self.segments = [self.SegmentFrame(self.segment_area, segment) 
                            for segment in segments_data]
        for segment in self.segments:
            segment.pack()

    def show_open_splitfile_buttons(self):
        if not self.open_button.winfo_ismapped():
            self.open_button.grid(row = 4, column = 0)
            self.new_button.grid(row = 4, column = 2)
        
    def hide_open_splitfile_buttons(self):
        if self.open_button.winfo_ismapped():
            self.open_button.grid_forget()
            self.new_button.grid_forget()


    class SegmentFrame(Frame):
        """
        """

        def __init__(self, root, segment_data):
            super().__init__(root)
            
            self._create(segment_data)
            self._arrange()

        def _create(self, segment_data):
            self.label = Label(self, text = segment_data.label.ljust(20))
            self.best_time_label = Label(self, text = 
                        Stopwatch.ms_to_time_str(segment_data.best_time).ljust(11))
            self.difference_label = Label(self, text = "--".ljust(8))

        def _arrange(self):
            self.label.grid(row = 0, column = 0)
            self.difference_label.grid(row = 0, column = 1)
            self.best_time_label.grid(row = 0, column = 2)

        def update_segment_time(self, diff):
            self.difference_label["text"] = diff.ljust(8)
