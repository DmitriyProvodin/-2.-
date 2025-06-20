import requests
from abstract_classes import Parser

class HH(Parser):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self, file_worker):
        """
        Инициализация парсера HH.
        :param file_worker: объект для работы с файлами
        """
        super().__init__(file_worker)
        self.__base_url = "https://api.hh.ru/vacancies"
        self.vacancies = []

    def __connect(self, params: dict) -> dict:
        """
        Приватный метод подключения к API HH.
        :param params: параметры запроса
        :return: словарь с результатами
        """
        response = requests.get(self.__base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка при получении данных: {response.status_code}")
            return {}

    def load_vacancies(self, keyword: str) -> None:
        """
        Загружает вакансии по ключевому слову.
        :param keyword: поисковое слово
        """
        params = {
            "text": keyword,
            "area": 113,  # Россия
            "per_page": 50,
            "page": 0
        }
        response_data = self.__connect(params)
        self.vacancies = response_data.get("items", [])
