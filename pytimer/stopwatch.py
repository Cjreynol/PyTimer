from threading  import Thread
from time       import sleep, time


class Stopwatch():
    """
    The Stopwatch class is intended to function as a simple timer, providing 
    functionality for stopping, starting, resetting, and returning the 
    current time(split).
    """

    UPDATE_DELAY = 0.05

    def __init__(self, string_variable):
        self.done = False
        self.timer_on = False

        self._start = None
        # used to keep track when timer is off
        self._elapsed_time = 0.0

        self.time_string_var = string_variable
        self._set_time_string(self._elapsed_time)
        
        Thread(target = self._update).start()

    def shutdown(self):
        """
        Set the done flag to signal the time updating thread to stop after its 
        next update loop finishes.
        """
        self.done = True
    
    def reset(self):
        """
        Put the Stopwatch back to 0, with no time elapsed.
        """
        self.set_time(0.0)

    def set_time(self, new_time):
        """
        Set the current Stopwatch time to the time(in ms) passed in.
        """
        self._start = time()
        self._elapsed_time = new_time
        self._set_time_string(self._elapsed_time)

    def split(self):
        """
        Return the current time(in ms) of the Stopwatch.
        """
        time_str = self.time_string_var.get()
        return self._time_str_to_ms(time_str)
        
    def start(self):
        """
        Set the flag for the background thread to begin updating the timer.

        If the timer is already on, this method does nothing.
        """
        if not self.timer_on:
            self._start = time() - self._elapsed_time
            self.timer_on = True
            
    def stop(self):
        """
        Set the flag for the background thread to stop updating the timer.

        If the timer is already off, this method does nothing.
        """
        if self.timer_on:
            self.timer_on = False
    
    def _update(self):
        """
        Loop updating the time string until the Stopwatch is shutdown.
        """
        while not self.done:
            if self.timer_on:
                self._elapsed_time = time() - self._start
                self._set_time_string(self._elapsed_time)
            sleep(self.UPDATE_DELAY)

    def _time_str_to_ms(self, time_str):
        """
        Convert a string in the HH:MM:SS.HS format into milliseconds.
        """
        hours, minutes, seconds = map(float, time_str.split(':'))
        return seconds + minutes * 60 + hours * 3600

    def _ms_to_time_str(self, ms):
        """
        Converts the milliseconds passed into HH:MM:SS.HS format.
        """
        hours, ms = divmod(ms, 3600)
        minutes, ms = divmod(ms, 60)
        seconds = int(ms)
        hseconds = str(ms - seconds).split('.')[1][0:2]
        
        return "{:>02}:{:>02}:{:>02}.{:>02}".format(int(hours), int(minutes), 
                                                    seconds, hseconds)
        
    def _set_time_string(self, elapsed):
        """
        Set the time string using the passed in time, expected to be in 
        milliseconds.
        """
        new_str = self._ms_to_time_str(elapsed)
        self.time_string_var.set(new_str)
