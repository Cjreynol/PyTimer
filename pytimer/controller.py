from pytimer.stopwatch      import Stopwatch
from pytimer.time_entry_box import TimeEntryBox
from pytimer.view           import View


class Controller():
    """
    Manages both the GUI and the stopwatch, passing information between them.
    """
    
    def __init__(self):
        self.view = View(self)
        self.stopwatch = Stopwatch(self.view.stopwatch_label_var)

    def quit(self):
        self.stopwatch.shutdown()
        self.view.quit()

    def start(self):
        self.view.start()

    def control_callback(self):
        """
        Determines and executes the logic for start or stop functionality, 
        depending on the state of the stopwatch.
        """
        if not self.stopwatch.timer_on:
            self.stopwatch.start()
            self.view.change_start_stop_text(self.view.STOP_LABEL)
        else:
            self.stopwatch.stop()
            self.view.change_start_stop_text(self.view.START_LABEL)

    def reset_callback(self):
        self.stopwatch.reset()

    def set_time_callback(self):
        TimeEntryBox(self, "Enter new time")

    def confirm_callback(self, retrieve_func):
        time_str = retrieve_func()
        new_time = self.stopwatch.time_str_to_ms(time_str)
        if new_time is not None:
            self.stopwatch.set_time(new_time)
