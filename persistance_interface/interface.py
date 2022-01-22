from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def add_dependency(self):
        pass

    @abstractmethod
    def add_package(self):
        pass

    @abstractmethod
    def remove_package(self):
        pass

    @abstractmethod
    def list_installed_packages(self):
        pass

    @abstractmethod
    def list_registered_packages(self):
        pass
