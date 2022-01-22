from unittest import TestCase

from manager.manager import CommandManager
from manager.depend import DependCommand
from persistance_interface.on_memory_interface import OnMemoryInterface


class TestDependCommand(TestCase):
    def setUp(self) -> None:
        self.interface = OnMemoryInterface()
    
    def test_add_new_package(self):
        package_name = 'HTTP'
        args = [package_name]
        
        command_class = DependCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        registered_packages = self.interface.list_registered_packages()
        self.assertTrue(package_name.lower() in registered_packages)

    def test_add_new_pachage_with_dependencies(self):
        package_name = 'HTTP'
        dependencies = ['httplib', 'ssh']
        args = [package_name] + dependencies
        
        command_class = DependCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        registered_packages = self.interface.list_registered_packages()
        self.assertTrue(package_name.lower() in registered_packages)
        self.assertListEqual(dependencies, registered_packages.get(package_name.lower()))
