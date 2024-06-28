# Diplom_3
Тест для проверки веб-приложения "Stellar Burgers" с помощью библиотеки Pytest, Requests и allure-pytest
Структура проекта:

tests/ - папка с файлами тестов:

tests/test_main_functions.py - тесты для проверки основного функционала
tests/test_order_feed.py - тесты для проверки раздела "Лента заказов"
tests/test_password_recovery.py - тесты для проверки восстановления пароля
tests/test_profile.py - тесты для проверки личного кабинета

Директории locators - в которой содержится 6 файлов с локаторами и pages - в которой содержится 6 файлов

Файл "helper.py" - файл, в котором лежат данные для пользователя

Файл "conftest.py" - Файл, в котором лежат фикстуры, в которую передается сгенерированные данные для создание пользователя.

Файл "constants.py" - константы, URL-адреса и данные для тестов

Файл ".gitignore" - файл для проекта в Git/GinHub

Файл "requirements.txt" - файл с внешними зависимостями

README.md - файл с описанием проекта 

Папка "allure_results/" - папка с отчетами Allure

Для запуска тестов должны быть установлены пакеты:
Pytest
Requests
Allure-pytest
Allure-python-commons
Для генерации отчетов необходимо дополнительно установить:
пакет Allure
фреймворк JDK
Запуск всех тестов выполняется командой:

$ pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

$ pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:

$ allure serve allure_results

Генерация файла внешних зависимостей requirements.txt выполняется командой:

$  pip freeze > requirements.txt

Установка зависимостей из файла requirements.txt выполняется командой:

$ pip install -r requirements.txt