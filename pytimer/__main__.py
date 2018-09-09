from os                 import makedirs
from os.path            import exists, expanduser, join
from pytimer.controller import Controller


__version__ = ('1', '9', '2')

SUPPORT_DIR = expanduser(join("~", 
                                "Library", 
                                "Application Support", 
                                "PyTimer"))

def ensure_support_dir_exists(filepath):
    if not exists(filepath):
        makedirs(filepath)

def main():
    controller = Controller(SUPPORT_DIR)
    controller.start()


if __name__ == "__main__":
    ensure_support_dir_exists(SUPPORT_DIR)
    main()
