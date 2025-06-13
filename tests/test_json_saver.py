import os
import json
import pytest
from json_saver import JSONSaver
from vacancy import Vacancy

TEST_FILE = "test_vacancies.json"

@pytest.fixture
def saver():
    saver = JSONSaver(filename=TEST_FILE)
    yield saver
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_and_get_vacancy(saver):
    v = Vacancy("Dev", "url", 100000, "Python")
    saver.add_vacancy(v)
    vacancies = saver.get_vacancies()
    assert any(v['url'] == "url" for v in vacancies)

def test_delete_vacancy(saver):
    v = Vacancy("Dev", "url", 100000, "Python")
    saver.add_vacancy(v)
    saver.delete_vacancy(v)
    vacancies = saver.get_vacancies()
    assert not any(v['url'] == "url" for v in vacancies)
