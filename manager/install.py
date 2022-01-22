from manager.command import Command


class InstallCommand(Command):    
    def process(self):
        package_name = self._get_package_name()
        if not package_name:
            return

        result = self.interface.add_package(package_name)
        if isinstance(result, list):
            return self._response_list(result)

        return result
    
    @staticmethod
    def _response_list(result):
        result_list = list()
        for package in result:
            result_list.append(f'{package.upper()} successfully installed')

        return result_list
