class Vacancy:
    """
    Класс для представления вакансии.
    """

    __slots__ = ('name', 'url', 'salary', 'requirement')

    def __init__(self, name: str, url: str, salary: int, requirement: str):
        """
        Инициализация вакансии.
        :param name: название вакансии
        :param url: ссылка на вакансию
        :param salary: зарплата
        :param requirement: требования
        """
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.requirement = requirement

    def __repr__(self) -> str:
        """Строковое представление вакансии."""
        return f"{self.name} | {self.salary} | {self.url}"

    def _validate_salary(self, salary: int) -> int:
        """Приватная валидация зарплаты."""
        return int(salary) if salary else 0

    def __lt__(self, other: 'Vacancy') -> bool:
        """Сравнение по зарплате меньше."""
        return self.salary < other.salary

    def __eq__(self, other: 'Vacancy') -> bool:
        """Сравнение по зарплате равно."""
        return self.salary == other.salary

    @classmethod
    def cast_to_object_list(cls, data: list[dict]) -> list['Vacancy']:
        """
        Преобразование словарей в список объектов Vacancy.
        :param data: список словарей вакансий
        :return: список объектов Vacancy
        """
        result = []
        for item in data:
            result.append(
                cls(
                    name=item.get("name"),
                    url=item.get("alternate_url"),
                    salary=(item.get("salary") or {}).get("from") or 0,
                    requirement=item.get("snippet", {}).get("requirement") or ""
                )
            )
        return result
