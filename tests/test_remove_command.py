import unittest

from manager.manager import CommandManager
from manager.remove import RemoveCommand
from persistance_interface.on_memory_interface import OnMemoryInterface


class TestRemoveCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.package_name = 'http'
        self.dependency = 'httplib'
        self.interface = OnMemoryInterface()

        self.interface.add_dependency(self.package_name, [self.dependency])
        self.interface.add_package(self.package_name)

    def test_remove_package(self):        
        args = [self.package_name]
        command_class = RemoveCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()
        self.assertFalse(self.package_name in installed_packages)

    def test_remove_package_and_dependecies(self):
        args = [self.package_name]
        command_class = RemoveCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()

        self.assertFalse(self.package_name in installed_packages)
        self.assertFalse(self.dependency in installed_packages)

    def test_remove_package_and_dependencies_not_possible(self):
        ssh_package = 'ssh'
        self.interface.add_dependency(ssh_package, [self.dependency])
        self.interface.add_package(ssh_package)

        args = [self.package_name]
        command_class = RemoveCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()

        self.assertFalse(self.package_name in installed_packages)
        self.assertTrue(self.dependency in installed_packages)

    def test_remove_package_not_exist(self):
        ssh_package = 'ssh'

        args = [ssh_package]
        command_class = RemoveCommand
        manager = CommandManager(command_class, self.interface, *args)
        result = manager.process_command()

        self.assertEqual(result, 'Package is not installed')
