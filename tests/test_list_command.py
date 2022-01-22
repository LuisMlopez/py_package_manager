import unittest

from manager.server import _process_input, PACKAGES, REGISTERED_PACKAGES, INSTALLED_PACKAGES


class TestRemoveCommand(unittest.TestCase):
    COMMAND_NAME = 'LIST'

    def setUp(self) -> None:
        self.package_name = 'http'
        self.dependency = 'httplib'
        PACKAGES.update({
            REGISTERED_PACKAGES: {
                self.package_name: [self.dependency]
            },
            INSTALLED_PACKAGES: [self.package_name, self.dependency]
        })

    def test_list_installed_packages(self):
        command = f'{self.COMMAND_NAME} {self.package_name}'        
        _process_input(command)