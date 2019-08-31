from .controller        import Controller


VERSION = ('2', '3', '0')

APPLICATION_NAME = "PyTimer"


def create_application_controller():
    return Controller(APPLICATION_NAME, None)

if __name__ == "__main__":
    controller = create_application_controller()
    controller.start()
