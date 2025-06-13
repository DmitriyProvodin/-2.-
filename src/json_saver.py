import json
import os
from src.abstract_classes import FileWorker


class JSONSaver(FileWorker):
    def __init__(self, filename='vacancies.json'):
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        if vacancy.__dict__ not in vacancies:
            vacancies.append(vacancy.__dict__)
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v['url'] != vacancy.url]
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_vacancies(self):
        with open(self.__filename, 'r', encoding='utf-8') as f:
            return json.load(f)
