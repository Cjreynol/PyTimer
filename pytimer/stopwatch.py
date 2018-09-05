from threading  import Thread
from time       import sleep, time


class Stopwatch():
    """
    The Stopwatch class is intended to function as a simple timer, providing 
    functionality for stopping, starting, resetting, and returning the 
    current time(split).
    """

    UPDATE_DELAY = 0.05

    def __init__(self, string_variable, elapsed_time = 0.0):
        self._start = 0.0
        self._elapsed_time = elapsed_time
        self.running = True
        self.timer_on = False

        self.time_string = string_variable
        self._setTime(self._elapsed_time)
        
        Thread(target = self._update).start()

    def shutdown(self):
        self.running = False
    
    def reset(self):
        self._start = time()
        self._elapsed_time = 0.0
        self._setTime(self._elapsed_time)

    def split(self):
        return self.time_string.get()
        
    def start(self):
        if not self.timer_on:
            self._start = time() - self._elapsed_time
            self.timer_on = True
            
    def stop(self):
        if self.timer_on:
            self.timer_on = False
    
    def _update(self):
        """
        Continues to loop, updating time and display when the timer is on, 
        until the program exits.
        """
        while self.running:
            if self.timer_on:
                self._elapsed_time = time() - self._start
                self._setTime(self._elapsed_time)
            sleep(self.UPDATE_DELAY)
        
    def _setTime(self, elapsed_time):
        """
        Converts the seconds passed into HH:MM:SS.HS format and updates the 
        time_string variable.
        """
        hours = int(elapsed_time // 3600)
        elapsed_time = elapsed_time % 3600

        minutes = int(elapsed_time // 60)
        elapsed_time = elapsed_time % 60

        seconds = int(elapsed_time)
        hseconds = str(elapsed_time - seconds).split('.')[1][0:2]

        self.time_string.set("{:>02}:{:>02}:{:>02}.{:>02}".format(hours, minutes, seconds, hseconds))
