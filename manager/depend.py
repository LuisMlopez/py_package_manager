from manager.command import Command


class DependCommand(Command):
    def process(self):
        package_name = self._get_package_name()
        if not package_name:
            return

        dependencies = self._get_dependencies()

        self.interface.add_dependency(package_name, dependencies)

    def _get_dependencies(self):
        if len(self.args) <= 1:
            return list()
        
        dependecies = self.args[1:]
        dependecies = [dependency.lower() for dependency in dependecies]
        return dependecies
