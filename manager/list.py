from manager.command import Command


class ListCommand(Command):    
    def process(self):
        result = self.interface.list_installed_packages()
        return self._response_list(result)

    @staticmethod
    def _response_list(result):
        result_list = list()
        for package in result:
            result_list.append(f'{package.upper()}')

        return result_list
