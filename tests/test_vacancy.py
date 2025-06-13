from src.vacancy import Vacancy

def test_vacancy_repr():
    v = Vacancy("Dev", "url", 100000, "Python")
    assert "Dev" in repr(v)


def test_vacancy_validation():
    v1 = Vacancy("Dev", "url", None, "")
    v2 = Vacancy("Dev", "url", 0, "")
    assert v1.salary == 0
    assert v2.salary == 0


def test_vacancy_comparison():
    v1 = Vacancy("Junior", "url1", 50000, "")
    v2 = Vacancy("Senior", "url2", 150000, "")
    assert v1 < v2
    assert not v1 == v2