from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def delete(self, student_id): # New
        pass

    @abstractmethod
    def search_by_id(self, student_id):
        pass

    @abstractmethod
    def search_by_name(self, name):
        pass

    @abstractmethod
    def search_by_group(self, group):
        pass

    @abstractmethod
    def get_all(self):
        pass

