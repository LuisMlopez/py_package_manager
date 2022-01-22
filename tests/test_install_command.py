import unittest

from manager.server import _process_input, PACKAGES, REGISTERED_PACKAGES, INSTALLED_PACKAGES


class TestInstallCommand(unittest.TestCase):
    COMMAND_NAME = 'INSTALL'

    def setUp(self) -> None:
        PACKAGES.update({
            REGISTERED_PACKAGES: dict(),
            INSTALLED_PACKAGES: list()
        })

    def test_install_package(self):
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        registered_packages = PACKAGES.get(REGISTERED_PACKAGES)
        package_name = 'HTTP'
        registered_packages.update({
            package_name.lower(): []
        })
        
        command = f'{self.COMMAND_NAME} {package_name}'        
        _process_input(command)

        self.assertTrue(package_name.lower() in installed_packages)

    def test_install_package_and_dependecies(self):
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        registered_packages = PACKAGES.get(REGISTERED_PACKAGES)
        package_name = 'HTTP'
        dependencies = 'httplib ssh'
        registered_packages.update({
            package_name.lower(): dependencies.split(' ')
        })

        command = f'{self.COMMAND_NAME} {package_name} {dependencies}'
        _process_input(command)

        self.assertTrue(package_name.lower() in installed_packages)
        for dependency in dependencies.split(' '):
            self.assertTrue(dependency in installed_packages)

    def test_install_package_not_exist(self):
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        package_name = 'HTTP'

        command = f'{self.COMMAND_NAME} {package_name}'        
        _process_input(command)

        self.assertFalse(package_name.lower() in installed_packages)

    def test_package_already_installed(self):
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        package_name = 'HTTP'
        installed_packages.append(package_name.lower())

        command = f'{self.COMMAND_NAME} {package_name}'        
        _process_input(command)

        self.assertTrue(package_name.lower() in installed_packages)
