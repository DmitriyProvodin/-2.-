# Вакансии с HeadHunter API

## 📌 Описание
Программа получает вакансии с hh.ru по ключевому слову, сохраняет их в JSON-файл и позволяет:
- фильтровать вакансии по ключевому слову в описании
- сортировать по зарплате
- выводить топ-N вакансий

## 🛠 Структура проекта
```
project/
├── abstract_classes.py
├── hh.py
├── json_saver.py
├── main.py
├── vacancy.py
├── vacancies.json
└── tests/
    ├── test_vacancy.py
    └── test_json_saver.py
```

## 🚀 Как запустить
1. Установить зависимости:
```
pip install -r requirements.txt
```

2. Запустить программу:
```
python main.py
```

## 🧪 Тесты
Запуск тестов с помощью `pytest`:
```
pytest tests/
```

## 💡 Пример запроса
Пользователь вводит ключевое слово, например `Python`. Программа загружает вакансии с hh.ru, сохраняет их и выводит топ-N по зарплате.

## 📂 Зависимости
См. `requirements.txt`

## 👨‍💻 Автор
Курсовая работа по Python. OpenAI ChatGPT + пользователь 😊
