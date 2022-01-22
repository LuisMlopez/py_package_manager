from manager.depend import DependCommand
from manager.install import InstallCommand
from manager.list import ListCommand
from manager.manager import CommandManager
from manager.remove import RemoveCommand
from persistance_interface.on_memory_interface import OnMemoryInterface

COMMANDS = {
    'DEPEND': DependCommand,
    'INSTALL': InstallCommand,
    'REMOVE': RemoveCommand,
    'LIST': ListCommand
}

DB_INTERFACE = OnMemoryInterface()


def _process_result(command_result):
    if not command_result:
        return

    tab = '   {}'

    if isinstance(command_result, str):
        print(tab.format(command_result))

    elif isinstance(command_result, list):
        for result in command_result:
            print(tab.format(result))


def _process_input(input_line):
    print(input_line.upper())
    command, *args = input_line.split(' ')

    if command.upper() == 'END':
        return True

    command_class = COMMANDS.get(command.upper())

    if command_class is None:
        print('Invalid command')
        return

    manager = CommandManager(command_class, DB_INTERFACE, *args)
    command_result = manager.process_command()

    _process_result(command_result)

    return False


def start_package_server():
    print('Package manager started.')
    print('Listening for commands...')

    while True:
        line = input()

        terminate = _process_input(line)

        if terminate:
            break
