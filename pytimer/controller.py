from os                     import path

from tkinter.filedialog     import askopenfilename, asksaveasfilename

from pytimer.split_handler  import SplitHandler
from pytimer.gui            import (MainWindow, SplitsView, StopwatchView, 
                                        TimeEntryBox)
from pytimer.stopwatch      import Stopwatch


class Controller:
    """
    Manages both the GUI and the stopwatch, passing information between them.
    """

    PYTIMER_EXTENSION = ".pytimer"
    FILETYPES = (("pytimer files", "*" + PYTIMER_EXTENSION),)
    
    def __init__(self, support_dir):
        self.window = MainWindow(self)
        self.support_dir = support_dir

        self.stopwatch_view = StopwatchView(self.window.root, self)
        self.splits_view = SplitsView(self.window.root, self)

        self.stopwatch = Stopwatch(self.stopwatch_view.stopwatch_label_var)
        self.split_handler = None

    def quit(self):
        self.stopwatch.shutdown()
        self.window.quit()

    def start(self):
        self.stopwatch_view.pack()
        self.window.start()

    def control_callback(self):
        """
        Determines and executes the logic for start or stop functionality, 
        depending on the state of the stopwatch.
        """
        if not self.stopwatch.timer_on:
            self.stopwatch.start()
        else:
            self.stopwatch.stop()

    def reset_callback(self):
        self.stopwatch.reset()

    def set_time_callback(self):
        self.stopwatch.stop()
        TimeEntryBox(self, "Enter new time")

    def confirm_callback(self, retrieve_func):
        time_str = retrieve_func()
        new_time = self.stopwatch.time_str_to_ms(time_str)
        if new_time is not None:
            self.stopwatch.set_time(new_time)

    def open_callback(self):
        filename = askopenfilename(initialdir = self.support_dir, 
                                    filetypes = self.FILETYPES) 
        if filename:
            self.split_handler = SplitHandler(filename)
            self.splits_view.update(self.split_handler.title, 
                                    self.split_handler.segments)
            if not self.splits_view.winfo_ismapped():
                self.swap_to_splits_callback()

    def save_callback(self):
        if self.split_handler is not None:
            filename = asksaveasfilename(initialdir = self.support_dir, 
                                        defaultextension = 
                                            self.PYTIMER_EXTENSION,
                                        filetypes = self.FILETYPES) 
            if filename:
                self.split_handler.save_splits(filename, replace = True)

    def swap_to_stopwatch_callback(self):
        if self.splits_view.winfo_ismapped():
            self.splits_view.pack_forget()

    def swap_to_splits_callback(self):
        if not self.splits_view.winfo_ismapped():
            self.splits_view.pack()

    def split_callback(self):
        if self.split_handler is not None:
            time = self.stopwatch.split()
            set_result = self.split_handler.set_split(time)
            if set_result is not None:
                diff, segment_index = set_result
                time_str, diff_str = (self.stopwatch.ms_to_time_str(time), 
                                        self.stopwatch.ms_to_time_str(diff))
                (self.splits_view.segments[segment_index].
                    update_segment_time(diff_str))

    def skip_split_callback(self):
        if self.split_handler is not None:
            self.split_handler.skip_segment()
