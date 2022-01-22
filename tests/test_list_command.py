import unittest

from manager.manager import CommandManager
from manager.list import ListCommand
from persistance_interface.on_memory_interface import OnMemoryInterface


class TestRemoveCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.package_name = 'http'
        self.dependency = 'httplib'
        self.interface = OnMemoryInterface()

        self.interface.add_dependency(self.package_name, [self.dependency])
        self.interface.add_package(self.package_name)

    def test_list_installed_packages(self):
        command_class = ListCommand
        manager = CommandManager(command_class, self.interface, None)
        result = manager.process_command()

        self.assertTrue(self.package_name.upper() in result)
        self.assertTrue(self.dependency.upper() in result)