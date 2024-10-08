Проект по автоматизации тестирования. Объекты тестирования: страница "Автоизации", "Регистрации", "Восстановление пароля" ПАО "Ростелеком" (https://b2c.passport.rt.ru/).
Проводится функциональное тестирование "Авторизации", "Регистрации" (с помощью номера телефона/почты/логина/номера лицевого счёта).
К данным элементам сайта применяется техника тест-дизайна тестирование состояний и переходов. Цель проверок состоит в выявлении реакции системы на ввод корректных и некорректных данных: пропуск введённых данных или появление сообщений об ошибках.
Наборы подготовленных данных для тестов созданы с использованием таких техник тест-дизайна, как разбиение на классы эквивалентности и граничные значения. Данные техники тест-дизайна в этом проекте применяются для того, что бы сократить количество одинаковых проверок.
Проводится проверка различных элементов страницы на их наличие и название согласно требованию. 

Для разработки тест-кейсов использованы:
методы "черного ящика",
функционального тестирования,
UX-тестирование.

Для написания автотестов использовалась интегрированная среда разработки PyCharm 2023.3.5 (Community Edition)

Для разработки автотестов применялись библиотеки:
pytest,
pytest-selenium.
Разработка проекта автотестирования выполнена по паттерну PageObject.
Использовались фикстуры параметризации, явные и неявные ожидания драйвером, различные способы описания локаторов.

Проект разработан для операционной системы Windows 10 Pro 

Браузер Google Chrome Версия Версия 129.0.6668.60 (Официальная сборка), (64 бит)

Запуск тестов: python -m pytest -v --driver Chrome --driver-path путь/chromedriver.exe
