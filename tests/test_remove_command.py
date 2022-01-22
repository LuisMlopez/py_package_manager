import unittest

from manager.server import _process_input, PACKAGES, REGISTERED_PACKAGES, INSTALLED_PACKAGES


class TestRemoveCommand(unittest.TestCase):
    COMMAND_NAME = 'REMOVE'

    def setUp(self) -> None:
        self.package_name = 'http'
        self.dependency = 'httplib'
        PACKAGES.update({
            REGISTERED_PACKAGES: {
                self.package_name: [self.dependency]
            },
            INSTALLED_PACKAGES: [self.package_name, self.dependency]
        })

    def test_remove_package(self):
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        
        command = f'{self.COMMAND_NAME} {self.package_name}'        
        _process_input(command)

        self.assertFalse(self.package_name in installed_packages)

    def test_remove_package_and_dependecies(self):
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)

        command = f'{self.COMMAND_NAME} {self.package_name}'
        _process_input(command)

        self.assertFalse(self.package_name in installed_packages)
        self.assertFalse(self.dependency in installed_packages)

    def test_remove_package_and_dependencies_not_possible(self):
        registered_packages = PACKAGES.get(REGISTERED_PACKAGES)
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)

        registered_packages.update({
            'ssh': [self.dependency]
        })
        installed_packages.append('ssh')

        command = f'{self.COMMAND_NAME} {self.package_name}'
        _process_input(command)

        self.assertFalse(self.package_name in installed_packages)
        self.assertTrue(self.dependency in installed_packages)

    def test_remove_package_not_exist(self):
        PACKAGES.update({
            INSTALLED_PACKAGES: list()
        })
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)

        command = f'{self.COMMAND_NAME} {self.package_name}'
        _process_input(command)

        self.assertFalse(self.package_name in installed_packages)
