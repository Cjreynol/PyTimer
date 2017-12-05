from time import time


class Stopwatch():
    UPDATE_DELAY = 50
    DISPLAY_STRING = "{:>02}:{:>02}:{:>02}.{:>02}"

    def __init__(self, string_variable, root, elapsed_time = 0.0):
        self.root = root
        self._start = 0.0
        self._elapsed_time = elapsed_time
        self.running = False

        self.time_string = string_variable
        self._setTime(self._elapsed_time)
    
    def _update(self):
        self._elapsed_time = time() - self._start
        self._setTime(self._elapsed_time)
        self._timer_id = self.root.after(self.UPDATE_DELAY, self._update)
        
    def _setTime(self, elapsed_time):
        hours = int(elapsed_time // 3600)
        elapsed_time = elapsed_time % 3600

        minutes = int(elapsed_time // 60)
        elapsed_time = elapsed_time % 60

        seconds = int(elapsed_time)
        hseconds = str(elapsed_time - seconds).split('.')[1][0:2]

        self.time_string.set(self.DISPLAY_STRING.format(hours, minutes, seconds, hseconds))
        
    def start(self):
        if not self.running:
            self._start = time() - self._elapsed_time
            self._update()
            self.running = True
            
    def stop(self):
        if self.running:
            self.root.after_cancel(self._timer_id)
            self._elapsed_time = time() - self._start
            self._setTime(self._elapsed_time)
            self.running = False
    
    def reset(self):
        self._start = time()
        self._elapsed_time = 0.0
        self._setTime(self._elapsed_time)
