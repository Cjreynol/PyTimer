from os                     import path

from tkinter.filedialog     import askopenfilename

from pytimer.main_window    import MainWindow
from pytimer.split_handler  import SplitHandler
from pytimer.splits_view    import SplitsView
from pytimer.stopwatch      import Stopwatch
from pytimer.stopwatch_view import StopwatchView
from pytimer.time_entry_box import TimeEntryBox


class Controller():
    """
    Manages both the GUI and the stopwatch, passing information between them.
    """

    BASE_DIR = path.join("~", "dev", "projects", "pytimer")
    
    def __init__(self):
        self.window = MainWindow(self)

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
        filename = askopenfilename(initialdir = self.BASE_DIR) 
        if filename:
            self.split_handler = SplitHandler(filename)
            self.splits_view.update(self.split_handler.title, 
                                    self.split_handler.segments)
            if not self.splits_view.winfo_ismapped():
                self.swap_to_splits_callback()

    def save_callback(self):
        print("save")

    def swap_to_stopwatch_callback(self):
        if self.splits_view.winfo_ismapped():
            self.splits_view.pack_forget()

    def swap_to_splits_callback(self):
        if not self.splits_view.winfo_ismapped():
            self.splits_view.pack()
