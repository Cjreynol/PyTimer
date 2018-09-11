from tkinter                    import Menu, Tk


class MainWindow:
    """
    """

    WINDOW_TITLE = "PyTimer"

    def __init__(self, controller):
        self.controller = controller
        self.root = self._create_root()
        self._create_menu()

    def _create_root(self):
        """
        Return the root window already configured and with shortcuts bound.
        """
        root = Tk()
        root.title(self.WINDOW_TITLE)
        return self._add_root_keybindings(root)

    def _add_root_keybindings(self, root):
        """
        Bind all of the program's shortcuts to their callbacks.

        Ignores the menu divides, binds them all as lambdas to capture the 
        event that is passed by using bind.
        """
        root.protocol("WM_DELETE_WINDOW", self.controller.quit)

        for _, subdict in self._get_keybindings().items():
            for bind, pair in subdict.items():
                callback, _ = pair
                root.bind("<{}>".format(bind),
                            self._make_event_lambda(callback))
        return root

    def _create_menu(self):
        """
        Bind all of the program's shortcuts to menu items.

        Each key holds a separate set of menu items, with keybinding, 
        callback, and menu label.
        """
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        for menu_name, bindings in self._get_keybindings().items():
            new_menu = Menu(menubar)
            menubar.add_cascade(label = menu_name, menu = new_menu)
            for bind, pair in bindings.items():
                callback, menu_label = pair
                new_menu.add_command(label = menu_label,
                                        command = callback,
                                        accelerator = 
                                            bind.replace("Key-", ""))

    def quit(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()

    def _make_event_lambda(self, function):
        """
        Wrap a function to capture and throw away the event argument.
        """
        return lambda event: function()

    def _get_keybindings(self):
        """
        Return a dict of all the keybindings in the application.
        
        Dictionary is in the form of:
        key : (callback, label)
        """
        keybindings = {
            "File" : {
                "Command-n" : (self.controller.new_callback, "New Split"),
                "Command-o" : (self.controller.open_callback, 
                                "Open Split..."),
                "Command-s" : (self.controller.save_callback, 
                                "Save Split as..."),
                "Command-w" : (self.controller.quit, "Close Window")
            },
            "View" : {
                "Command-Key-1" : (self.controller.swap_to_stopwatch_callback, 
                                    "Stopwatch View"),
                "Command-Key-2" : (self.controller.swap_to_splits_callback, 
                                    "Splits View")
            },
            "Controls" : {
                "space" : (self.controller.toggle_callback, "Toggle"),
                "Command-r" : (self.controller.reset_callback, "Reset"),
                "Command-t" : (self.controller.set_time_callback, "Set Time"),

                "Return" : (self.controller.split_callback, "Split"),
                "Command-[" : (self.controller.back_split_callback, 
                                "Back Split"),
                "Command-]" : (self.controller.skip_split_callback, 
                                "Forward Split")
            }
        }
        return keybindings
