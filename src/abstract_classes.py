from abc import ABC, abstractmethod

class Parser(ABC):
    """
    Абстрактный класс для работы с API вакансий.
    """

    def __init__(self, file_worker):
        """
        Инициализация парсера.
        :param file_worker: объект для работы с файлами
        """
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """
        Метод для загрузки вакансий по ключевому слову.
        """
        pass

    @abstractmethod
    def _Parser__connect(self, params: dict) -> dict:
        """
        Приватный метод подключения к API.
        :param params: параметры запроса
        :return: данные ответа от API
        """
        pass


class FileWorker(ABC):
    """
    Абстрактный класс для работы с файловыми хранилищами вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавить вакансию в файл."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удалить вакансию из файла."""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Получить все вакансии из файла."""
        pass
