<h2 align="center">Курс валют</h2>


**Посилання**:
- [Telegram](https://t.me/+EsF9XRlu0cs0ZDE6)
- [LinkedIn](https://www.linkedin.com/in/anatolii-baliuk-b639a820a/)
- [YouTube](https://www.youtube.com/channel/UC545y-cBsat9g2YPboSILCA)

### Опис проекту:
Актуальний курс валют в Україні


### Інструменти розробки

**Стек:**
- Python >= 3.9
- Django >= 3
- PostgreSQL

## Розробка

##### 1) Зробити форк репозиторія і поставити зірочку)

##### 2) Клонувати репозиторій

    git clone посилання_сгенероване_в_вашому_репозиторії

##### 3) Створити віртуальне оточення

    python -m venv venv
    
##### 4) Активувати віртуальне оточення

##### 5) Встановити залежності:

    pip install -r req.txt

##### 6) Створити в корні проекту (репозиторій "kurs_valut_service")
##### файл з іменем ".env" та внести до нього дані своєї БД

    Наприклад:
    DB_RATE_NAME = 'db_name'
    DB_RATENOW_USERNAME = 'username'
    DB_RATENOW_PASSWORD = 'password'

##### 7) Виконати команду для виконання міграцій

    python manage.py migrate
    
##### 8) Створити суперюзера

    python manage.py createsuperuser
    
##### 9) Запустити сервер

    python manage.py runserver

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2021-present, KHAN - Baliuk Anatolii


