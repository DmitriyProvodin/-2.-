from src.hh import HH
from src.json_saver import JSONSaver
from vacancy import Vacancy

def user_interaction():
    saver = JSONSaver()
    hh = HH(file_worker=saver)

    keyword = input("Введите ключевое слово для поиска: ")
    hh.load_vacancies(keyword)
    vacancies = Vacancy.cast_to_object_list(hh.vacancies)

    for v in vacancies:
        saver.add_vacancy(v)

    top_n = int(input("Сколько топ-вакансий показать по зарплате? "))
    sorted_vacancies = sorted(vacancies, reverse=True)
    print("\nТоп вакансий:")
    for v in sorted_vacancies[:top_n]:
        print(v)

    keyword = input("\nВведите ключевое слово для фильтрации по описанию: ").lower()
    filtered = [v for v in vacancies if keyword in v.requirement.lower()]
    print(f"\nВакансии по ключевому слову '{keyword}':")
    for v in filtered:
        print(v)


if __name__ == "__main__":
    user_interaction()
