from pytimer.stopwatch  import Stopwatch
from pytimer.view       import View


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
