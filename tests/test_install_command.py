import unittest

from manager.manager import CommandManager
from manager.install import InstallCommand
from persistance_interface.on_memory_interface import OnMemoryInterface


class TestInstallCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.interface = OnMemoryInterface()

    def test_install_package(self):
        package_name = 'http'
        self.interface.add_dependency(package_name)
        
        args = [package_name]
        command_class = InstallCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()
        self.assertTrue(package_name in installed_packages)

    def test_install_package_and_dependecies(self):
        package_name = 'http'
        dependencies = ['httplib', 'ssh']
        self.interface.add_dependency(package_name, dependencies)

        args = [package_name] + dependencies
        command_class = InstallCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()
        self.assertTrue(package_name in installed_packages)
        for dependency in dependencies:
            self.assertTrue(dependency in installed_packages)

    def test_install_package_not_exist(self):
        package_name = 'http'
      
        args = [package_name]
        command_class = InstallCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()
        self.assertFalse(package_name in installed_packages)

    def test_package_already_installed(self):
        package_name = 'http'
        self.interface.add_dependency(package_name)
        self.interface.add_package(package_name)

        args = [package_name]
        command_class = InstallCommand
        manager = CommandManager(command_class, self.interface, *args)
        manager.process_command()

        installed_packages = self.interface.list_installed_packages()
        self.assertTrue(package_name.lower() in installed_packages)
