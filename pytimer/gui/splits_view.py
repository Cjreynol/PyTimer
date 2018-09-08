from tkinter            import Button, Frame, Label, StringVar, E, W, X

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
        self.title = Label(self, text = "--")
        self.split = Button(self, text = "Split", 
                                command = self.controller.split_callback)
        self.skip_split = Button(self, text = "Skip Split",
                                    command = 
                                        self.controller.skip_split_callback)

        self.name = Label(self, text = "Name".ljust(20))
        self.difference = Label(self, text = "| Diff".ljust(8))
        self.current = Label(self, text = "| This Run".ljust(11))
        self.best = Label(self, text = "| Best Run".ljust(11))

        self.segment_area = Frame(self)
        self.segments = []

    def _arrange(self):
        self.title.grid(row = 0, column = 0, columnspan = 4)
        self.split.grid(row = 1, column = 0, columnspan = 2)
        self.skip_split.grid(row = 1, column = 2, columnspan = 2)

        self.name.grid(row = 2, column = 0)
        self.difference.grid(row = 2, column = 1)
        self.best.grid(row = 2, column = 2)

        self.segment_area.grid(row = 3, column = 0, columnspan = 4)
        for segment in self.segments:
            segment.pack()

    def update(self, title, segments_data):
        self.title["text"] = title
        for widget in self.segment_area.winfo_children():
            widget.destroy()

        self.segments = [SegmentFrame(self.segment_area, segment) 
                            for segment in segments_data]
        for segment in self.segments:
            segment.pack()
        

class SegmentFrame(Frame):
    """
    """

    def __init__(self, root, segment_data):
        super().__init__(root)
        
        self._create(segment_data)
        self._arrange()

    def _create(self, segment_data):
        self.label = Label(self, text = segment_data.label.ljust(20))
        self.best_time = Label(self, text = 
                    Stopwatch.ms_to_time_str(segment_data.best_time).ljust(11))
        self.difference = Label(self, text = "--".ljust(8))

    def _arrange(self):
        self.label.grid(row = 0, column = 0)
        self.difference.grid(row = 0, column = 1)
        self.best_time.grid(row = 0, column = 2)

    def update_segment_time(self, diff):
        self.difference["text"] = diff.ljust(8)
