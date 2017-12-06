from stopwatch import Stopwatch
from stopwatch_view import StopwatchView


class StopwatchViewController():
    """
    Manages both the GUI and the stopwatch, passing information between them.
    """
    
    def __init__(self):
        self.view = StopwatchView()
        self.stopwatch = Stopwatch(self.view.get_label_var())
        self._setup_view()

    def quit(self):
        self.stopwatch.shutdown()
        self.view.quit()

    def start(self):
        self.view.start()

    def _control_button_logic(self):
        """
        Determines and executes the logic for start or stop functionality, 
        depending on the state of the stopwatch.
        """
        if not self.stopwatch.timer_on:
            self.stopwatch.start()
            self.view.change_start_stop_text("Stop")
        else:
            self.stopwatch.stop()
            self.view.change_start_stop_text("Start")

    def _setup_view(self):
        """Attaches the proper stopwatch functions as callbacks in the GUI."""
        self.view.set_start_stop_button_command(self._control_button_logic)
        self.view.set_reset_button_command(self.stopwatch.reset)
        self.view.add_quit_function(self.quit)
