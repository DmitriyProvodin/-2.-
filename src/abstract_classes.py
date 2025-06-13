from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword: str):
        pass


class FileWorker(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy): pass

    @abstractmethod
    def delete_vacancy(self, vacancy): pass

    @abstractmethod
    def get_vacancies(self): pass
