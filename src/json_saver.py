import json
import os
from typing import List, Dict
from abstract_classes import FileWorker
from vacancy import Vacancy

class JSONSaver(FileWorker):
    """
    Класс для сохранения и обработки вакансий в JSON-файле.
    """

    def __init__(self, filename: str = 'vacancies.json'):
        """
        Инициализация JSONSaver.
        :param filename: имя JSON-файла
        """
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавить вакансию в файл, если она ещё не сохранена.
        :param vacancy: экземпляр класса Vacancy
        """
        vacancies = self.get_vacancies()
        if vacancy.__dict__ not in vacancies:
            vacancies.append(vacancy.__dict__)
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удалить вакансию из файла по URL.
        :param vacancy: экземпляр класса Vacancy
        """
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v['url'] != vacancy.url]
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_vacancies(self) -> List[Dict]:
        """
        Получить список вакансий из файла.
        :return: список словарей
        """
        with open(self.__filename, 'r', encoding='utf-8') as f:
            return json.load(f)
