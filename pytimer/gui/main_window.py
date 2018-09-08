from tkinter                    import Menu, Tk


class MainWindow:
    """
    """

    WINDOW_TITLE = "PyTimer"

    CLOSE_WINDOW_BIND = "Command-w"
    OPEN_BIND = "Command-o"
    SAVE_BIND = "Command-s"

    STOPWATCH_BIND = "Command-Key-1"
    SPLITS_BIND = "Command-Key-2"

    def __init__(self, controller):
        self.controller = controller
        self.root = self._create_root()
        self._create_menu()

    def _create_root(self):
        root = Tk()
        root.title(self.WINDOW_TITLE)

        root.protocol("WM_DELETE_WINDOW", self.controller.quit)
        root.bind("<Return>", lambda event: self.controller.split_callback())
        root.bind("<space>", lambda event: self.controller.control_callback())
        root.bind("<{}>".format(self.CLOSE_WINDOW_BIND), 
                    lambda event: self.controller.quit())
        root.bind("<{}>".format(self.OPEN_BIND), 
                    lambda event: self.controller.open_callback())
        root.bind("<{}>".format(self.SAVE_BIND), 
                    lambda event: self.controller.save_callback())
        root.bind("<{}>".format(self.STOPWATCH_BIND),
                    lambda event: self.controller.swap_to_stopwatch_callback())
        root.bind("<{}>".format(self.SPLITS_BIND),
                    lambda event: self.controller.swap_to_splits_callback())
        
        return root

    def _create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)

        file_menu = Menu(menubar)
        menubar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "Open File...", 
                                command = self.controller.open_callback, 
                                accelerator =self.OPEN_BIND)
        file_menu.add_command(label = "Save As...", 
                                command = self.controller.save_callback, 
                                accelerator = self.SAVE_BIND)
        file_menu.add_separator()
        file_menu.add_command(label = "Close Window", 
                                command = self.controller.quit,
                                accelerator = self.CLOSE_WINDOW_BIND)

        view_menu = Menu(menubar)
        menubar.add_cascade(label = "View", menu = view_menu)
        view_menu.add_command(label = "Stopwatch", 
                                command = 
                                    self.controller.swap_to_stopwatch_callback,
                                accelerator = 
                                    self.STOPWATCH_BIND.replace("-Key", ""))
        view_menu.add_command(label = "Splits", 
                                command = 
                                    self.controller.swap_to_splits_callback,
                                accelerator = 
                                    self.SPLITS_BIND.replace("-Key", ""))

    def quit(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()
