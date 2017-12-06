"""
Brings the components of the application together, starting the main thread of 
execution.
"""

from stopwatch_view_controller import StopwatchViewController


if __name__ == "__main__":
    stopwatch_app = StopwatchViewController()
    stopwatch_app.start()
