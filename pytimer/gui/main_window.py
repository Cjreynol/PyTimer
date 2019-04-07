from tkinter        import Menu, Tk
from tkinter.ttk    import Frame


class MainWindow:
    """
    """

    WINDOW_TITLE = "PyTimer"

    def __init__(self, controller, shortcut_modifier):
        self.controller = controller
        self.window = self._create_window(shortcut_modifier)
        self.root = self._create_root(self.window)

        menubar = self._create_menu(shortcut_modifier)
        self.window.config(menu = menubar)

    def _create_window(self, shortcut_modifier):
        """
        Return the root window already configured and with shortcuts bound.
        """
        window = Tk()
        window.title(self.WINDOW_TITLE)
        window = self._add_window_keybindings(window, shortcut_modifier)

        return window

    def _create_root(self, window):
        """
        Return the root frame.
        """
        root = Frame(window)
        root.pack()
        return root

    def _add_window_keybindings(self, window, shortcut_modifier):
        """
        Bind all of the program's shortcuts.
        """
        window.protocol("WM_DELETE_WINDOW", self.controller.quit)

        for _, subdict in self._get_keybindings(shortcut_modifier).items():
            for keybind, pair in subdict.items():
                callback, _ = pair
                window.bind("<{}>".format(keybind),
                            self._make_event_lambda(callback))
        return window

    def _create_menu(self, shortcut_modifier):
        """
        Bind all of the program's shortcuts to menu items.
        """
        menubar = Menu(self.window)
        for menu_name, bindings in self._get_keybindings(shortcut_modifier).items():
            new_menu = Menu(menubar)
            menubar.add_cascade(label = menu_name, menu = new_menu)
            for bind, pair in bindings.items():
                callback, menu_label = pair
                new_menu.add_command(label = menu_label, command = callback,
                                        accelerator = bind.replace("Key-", ""))
        return menubar

    def quit(self):
        self.window.destroy()

    def start(self):
        self.window.mainloop()

    def _make_event_lambda(self, function):
        """
        Wrap a function to capture and throw away the event argument.
        """
        return lambda event: function()

    def _get_keybindings(self, shortcut_modifier):
        """
        Return a dict of all the keybindings in the application.
        
        Dictionary is in the form of:
        category : { shortcut_key : (callback, label) }
        """
        keybindings = {
            "File" : {
                shortcut_modifier + "-n" : (self.controller.new_callback, 
                                                "New Split"),
                shortcut_modifier + "-Shift-n" : (self.controller.new_from_callback, 
                                                "New From Current"),
                shortcut_modifier + "-o" : (self.controller.open_callback, 
                                                "Open Split..."),
                shortcut_modifier + "-s" : (self.controller.save_callback, 
                                                "Save Split as..."),
                shortcut_modifier + "-w" : (self.controller.quit, 
                                                "Close Window") },
            "View" : {
                shortcut_modifier + "-Key-1" : (self.controller.swap_to_stopwatch_callback, 
                                                "Stopwatch View"),
                shortcut_modifier + "-Key-2" : (self.controller.swap_to_splits_callback, 
                                                "Splits View") },
            "Controls" : {
                "space" : (self.controller.toggle_callback, 
                                                "Toggle"),
                shortcut_modifier + "-r" : (self.controller.reset_callback, 
                                                "Reset"),
                shortcut_modifier + "-t" : (self.controller.set_time_callback, 
                                                "Set Time"),

                "Return" : (self.controller.split_callback, "Split"),
                shortcut_modifier + "-[" : (self.controller.back_split_callback, 
                                                "Back Split"),
                shortcut_modifier + "-]" : (self.controller.skip_split_callback, 
                                                "Forward Split") } }
        return keybindings
