import requests
from src.abstract_classes import Parser

class HH(Parser):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self, file_worker):
        super().__init__(file_worker)
        self.vacancies = []

    def load_vacancies(self, keyword: str):
        self.__fetch_data(keyword)

    def __fetch_data(self, keyword):
        params = {
            "text": keyword,
            "area": 113,  # Россия
            "per_page": 50,
            "page": 0
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            self.vacancies = response.json().get("items", [])
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
