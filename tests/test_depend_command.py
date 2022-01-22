from unittest import TestCase

from manager.server import _process_input, PACKAGES, REGISTERED_PACKAGES, INSTALLED_PACKAGES


class TestDependCommand(TestCase):
    COMMAND_NAME = 'DEPEND'

    def setUp(self) -> None:
        PACKAGES.update({
            REGISTERED_PACKAGES: dict(),
            INSTALLED_PACKAGES: list()
        })
    
    def test_add_new_package(self):
        registered_packages = PACKAGES.get(REGISTERED_PACKAGES)
        package_name = 'HTTP'
        command = f'{self.COMMAND_NAME} {package_name}'
        
        _process_input(command)
        self.assertTrue(package_name.lower() in registered_packages)

    def test_add_new_pachage_with_dependencies(self):
        registered_packages = PACKAGES.get(REGISTERED_PACKAGES)
        package_name = 'HTTP'
        dependencies = 'httplib ssh'
        command = f'{self.COMMAND_NAME} {package_name} {dependencies}'
        
        _process_input(command)
        self.assertTrue(package_name.lower() in registered_packages)
        self.assertListEqual(dependencies.split(' '), registered_packages.get(package_name.lower()))
