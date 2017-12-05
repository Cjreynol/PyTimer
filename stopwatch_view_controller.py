from stopwatch import Stopwatch
from stopwatch_view import StopwatchView


class StopwatchViewController():
    
    def __init__(self):
        self.view = StopwatchView()
        self.stopwatch = Stopwatch(self.view.get_label_var(), self.view.get_root())
        self._setup_view()

    def _setup_view(self):
        self.view.set_start_stop_button_command(self._control_button_logic)
        self.view.set_reset_button_command(self.stopwatch.reset)

    def start(self):
        self.view.start()

    def _control_button_logic(self):
        if not self.stopwatch.running:
            self.stopwatch.start()
            self.view.change_start_stop_text("Stop")
        else:
            self.stopwatch.stop()
            self.view.change_start_stop_text("Start")
