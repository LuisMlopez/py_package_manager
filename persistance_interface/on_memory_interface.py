from persistance_interface.interface import Interface


class OnMemoryInterface(Interface):
    def __init__(self) -> None:
        self.installed_packages = list()
        self.registered_packages = dict()

    def add_dependency(self, package_name, dependencies=None):
        if dependencies is None:
            dependencies = list()

        dependencies = [dependency.lower() for dependency in dependencies]
        
        self.registered_packages.update({
            package_name.lower(): dependencies
        })

    def add_package(self, package_name):
        if package_name in self.installed_packages:
            return 'Package already installed'

        if package_name not in self.registered_packages:
            return 'Package not found'

        package_name = package_name.lower()
        installed = list()

        self.installed_packages.append(package_name)
        installed.append(package_name)

        installed.extend(self._install_dependencies(package_name))
        return installed

    def _install_dependencies(self, package_name):
        installed = list()
        dependecies = self.registered_packages.get(package_name)

        for dependency in dependecies:
            if dependency in self.installed_packages:
                continue
            
            self.installed_packages.append(dependency)
            installed.append(dependency)

        return installed

    def remove_package(self, package_name):
        if package_name not in self.installed_packages:
            return 'Package is not installed'

        removed_list = list()

        removed = self._remove_package(package_name)
        if removed:
            removed_list.append(package_name)
        else:
            return f'{package_name.upper()} is still needed'

        removed_list.extend(self._remove_dependencies(package_name))

        return removed_list

    def _remove_package(self, package_name):
        for installed_package in self.installed_packages:
            if package_name == installed_package:
                continue

            package_dependencies = self.registered_packages.get(installed_package, [])
            if package_name in package_dependencies:
                return False

        self.installed_packages.remove(package_name)
        return True

    def _remove_dependencies(self, package_name):
        dependencies = self.registered_packages.get(package_name, [])
        removed_list = list()
        
        for dependency in dependencies:
            removed = self._remove_package(dependency)

            if removed:
                removed_list.append(dependency)
            
            else:
                print(f'{dependency.upper()} is still needed')

        return removed_list


    def list_installed_packages(self):
        return self.installed_packages

    def list_registered_packages(self):
        return self.registered_packages
