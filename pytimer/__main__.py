from os                 import makedirs
from os.path            import exists, expanduser, join
from platform           import system

from .controller        import Controller


__version__ = ('2', '1', '1')

APPLICATION_NAME = "PyTimer"

SHORTCUT_MODIFIERS = {  "Darwin" : "Command",
                        "Windows": "Control" }

SUPPORT_DIRS = {"Darwin" : expanduser(join("~", "Library", 
                                        "Application Support", 
                                        APPLICATION_NAME)),
                "Windows" : expanduser(join("~", "AppData", "Local",
                                        APPLICATION_NAME)) }

def ensure_support_dir_exists(filepath):
    """
    Check if the directory exists, if not then create it.
    """
    if not exists(filepath):
        makedirs(filepath)

def main(support_dir, shortcut_modifier):
    """
    Create the application controller, then start it running.
    """
    controller = Controller(support_dir, shortcut_modifier)
    controller.start()


if __name__ == "__main__":
    os_id = system()
    try:
        support_dir = SUPPORT_DIRS[os_id]
        shortcut_modifier = SHORTCUT_MODIFIERS[os_id]
    except KeyError as e:
        print("Operating system not supported, "
                "no known location for support directory {}.".format(str(e)))
    else:   # support dir and shortcut modifier were found
        ensure_support_dir_exists(support_dir)
        main(support_dir, shortcut_modifier)
