class Vacancy:
    __slots__ = ('name', 'url', 'salary', 'requirement')

    def __init__(self, name: str, url: str, salary: int, requirement: str):
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.requirement = requirement

    def __repr__(self):
        return f"{self.name} | {self.salary} | {self.url}"

    def _validate_salary(self, salary):
        if not salary or salary == 0:
            return 0
        return int(salary)

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    @classmethod
    def cast_to_object_list(cls, data: list) -> list:
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
