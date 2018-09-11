from os                     import path

from tkinter.filedialog     import askopenfilename, asksaveasfilename

from pytimer.split_handler  import SplitHandler
from pytimer.gui            import (MainWindow, NewSplitEntry, SplitsView, 
                                    StopwatchView, TimeEntryBox)
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
        """
        Stop the components and shut down the program.
        """
        self.stopwatch.shutdown()
        self.window.quit()

    def start(self):
        """
        Start the GUI.
        """
        self.stopwatch_view.pack()
        self.window.start()

    def toggle_callback(self):
        """
        Determines and executes the logic for start or stop functionality, 
        depending on the state of the stopwatch.
        """
        if not self.stopwatch.timer_on:
            self.stopwatch.start()
        else:
            self.stopwatch.stop()

    def reset_callback(self):
        """
        Puts the stopwatch into its initial state.
        """
        self.stopwatch.reset()

    def set_time_callback(self):
        """
        Create a window to allow the user to enter a new time to set.
        """
        self.stopwatch.stop()
        TimeEntryBox(self, "Enter new time")

    def confirm_callback(self, retrieve_func):
        """
        Get the time string from the time entry window and set the stopwatch 
        to the new time.
        """
        new_time = retrieve_func()
        if new_time is not None:
            self.stopwatch.set_time(new_time)

    def new_split_callback(self, retrieve_func):
        """
        """
        split_data = retrieve_func()
        title, segments = SplitHandler.parse_json(split_data)
        self.split_handler = SplitHandler(title, segments)
        self.splits_view.update(self.split_handler.title,
                                self.split_handler.segments)
        if not self.splits_view.winfo_ismapped():
            self.swap_to_splits_callback()
        else:
            self.splits_view.hide_open_splitfile_buttons()

    def open_callback(self):
        """
        Prompt the user for a filename and open/read/display that split file.
        """
        filename = askopenfilename(initialdir = self.support_dir, 
                                    filetypes = self.FILETYPES) 
        if filename:
            title, segments = SplitHandler.read_splitfile(filename)
            self.split_handler = SplitHandler(title, segments)
            self.splits_view.update(self.split_handler.title, 
                                    self.split_handler.segments)
            if not self.splits_view.winfo_ismapped():
                self.swap_to_splits_callback()
            else:
                self.splits_view.hide_open_splitfile_buttons()

    def save_callback(self):
        """
        Prompt the user for a filename and write out the current splits to 
        that file.
        """
        if self.split_handler is not None:
            filename = asksaveasfilename(initialdir = self.support_dir, 
                                        defaultextension = 
                                            self.PYTIMER_EXTENSION,
                                        filetypes = self.FILETYPES) 
            if filename:
                self.split_handler.save_splits(filename, replace = True)

    def swap_to_stopwatch_callback(self):
        """
        Shrink the view down to only the stopwatch view.
        """
        if self.splits_view.winfo_ismapped():
            self.splits_view.pack_forget()

    def swap_to_splits_callback(self):
        """
        Expand the view to include the split information.
        """
        if not self.splits_view.winfo_ismapped():
            self.splits_view.pack()
            if self.split_handler is None:
                self.splits_view.show_open_splitfile_buttons()

    def split_callback(self):
        """
        Pull the current time and update the display and split handling 
        object with it.
        """
        if self.split_handler is not None:
            time = self.stopwatch.split()
            set_result = self.split_handler.set_split(time)
            if set_result is not None:
                diff, segment_index = set_result
                time_str, diff_str = (self.stopwatch.ms_to_time_str(time), 
                                        self.stopwatch.ms_to_time_str(diff))
                (self.splits_view.segments[segment_index].
                    update_segment_time(diff_str))

    def back_split_callback(self):
        """
        Go back to the previous segment.
        """
        if self.split_handler is not None:
            self.split_handler.back_segment()

    def skip_split_callback(self):
        """
        Go to the next segment, skipping the current one.
        """
        if self.split_handler is not None:
            self.split_handler.skip_segment()

    def new_callback(self):
        """
        Create prompt window for making a new split file.
        """
        NewSplitEntry(self)
