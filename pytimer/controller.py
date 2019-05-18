from chadlib.gui        import ControllerBase, SLComponent, SLController

from .split_handler     import SplitHandler
from .gui               import (MainWindow, NewSplitEntryBox, SplitsView, 
                                    StopwatchView, TimeEntryBox)
from .stopwatch         import Stopwatch


class Controller(SLController, ControllerBase):
    """
    Manages both the GUI and the stopwatch, passing information between them.
    """
    
    def __init__(self, application_name, application_state):
        FILE_EXTENSION = "." + application_name.lower()
        self.sl_component = SLComponent(self, FILE_EXTENSION,
                                    (("pytimer files", "*" + FILE_EXTENSION),), 
                                    application_name)
        super().__init__(application_name, application_state, StopwatchView)

        self.stopwatch = Stopwatch(self.current_view.stopwatch_label_var)
        self.splits_view = SplitsView(self, self.window.root, None)
        self.split_handler = None


    def stop(self):
        """
        """
        self.stopwatch.shutdown()
        super().stop()

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

    def load_logic(self, filename):
        """
        Prompt the user for a filename and open/read/display that split file.
        """
        title, segments = SplitHandler.read_splitfile(filename)
        self.split_handler = SplitHandler(title, segments)
        self.splits_view.update(self.split_handler.title, 
                                self.split_handler.segments)

        if not self.splits_view.winfo_ismapped():
            self.swap_to_splits_callback()
        else:
            self.splits_view.hide_open_splitfile_buttons()

    def save_logic(self, filename):
        """
        Prompt the user for a filename and write out the current splits to 
        that file.
        """
        if self.split_handler is not None:
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
        NewSplitEntryBox(self)

    def new_from_callback(self):
        """
        Create prompt window for making a new split file, populated with 
        the information from the current split file.
        """
        if self.split_handler is not None:
            split_data = self.split_handler.build_json_object(replace = False)
            NewSplitEntryBox(self, split_data)

    def get_menu_data(self):
        menu_setup = super().get_menu_data()
        menu_setup = self.sl_component.get_menu_data(menu_setup)

        menu_setup.add_submenu_item("File", "New Split", self.new_callback, 
                                    "{}-n")
        menu_setup.add_submenu_item("File", "New From Current", 
                                    self.new_from_callback, "{}-Shift-n")

        menu_setup.add_submenu_item("View", "Stopwatch View", 
                                    self.swap_to_stopwatch_callback, 
                                    "{}-Key-1")
        menu_setup.add_submenu_item("View", "Splits View", 
                                    self.swap_to_splits_callback, 
                                    "{}-Key-2")

        menu_setup.add_submenu_item("Controls", "Toggle", self.toggle_callback, 
                                    "space")
        menu_setup.add_submenu_item("Controls", "Reset", self.reset_callback, 
                                    "{}-r")
        menu_setup.add_submenu_item("Controls", "Set Time", 
                                    self.set_time_callback, 
                                    "{}-t")
        menu_setup.add_submenu_item("Controls", "Split", self.split_callback, 
                                    "Return")
        menu_setup.add_submenu_item("Controls", "Back Split", 
                                    self.back_split_callback, 
                                    "{}-[")
        menu_setup.add_submenu_item("Controls", "Forward Split", 
                                    self.skip_split_callback,
                                    "{}-]")
        return menu_setup
