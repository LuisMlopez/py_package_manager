from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, interface, *args) -> None:
        self.interface = interface
        self.args = args
    
    @abstractmethod
    def process(self):
        pass

    def _get_package_name(self):
        if not self.args:
            return

        package_name = self.args[0]
        return package_name.lower()
