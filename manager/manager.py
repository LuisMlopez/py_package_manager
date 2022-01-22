class CommandManager:
    def __init__(self, command_class, interface, *args) -> None:
        self.command_class = command_class
        self.interface = interface
        self.args = args

        self._init_command_class()

    def _init_command_class(self):
        self.command = self.command_class(self.interface, *self.args)

    def process_command(self):
        return self.command.process()
