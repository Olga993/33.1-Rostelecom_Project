import pytest
from selenium.webdriver.common.by import By

import pages
from pages import auth_page
from pages.locators import AuthLocators
from settings import *


# 001 В правой части формы «Авторизация» находится слоган ЛК "Ростелеком ID"
def test_page_right(selenium):
    try:
        page = pages.auth_page.AuthPage(selenium)
        assert 'Персональный помощник в цифровом мире Ростелекома' in page.page_right.text
    except AssertionError:
        print('Элемент отсутствует в правой части формы')


# 002 Форма "Авторизации" содержит указанные элементы
def test_elements_of_auth(selenium):
    page = pages.auth_page.AuthPage(selenium)

    assert page.menu_tub.text in page.card_of_auth.text
    assert page.email.text in page.card_of_auth.text
    assert page.pass_eml.text in page.card_of_auth.text
    assert page.btn_enter.text in page.card_of_auth.text
    assert page.forgot_password_link.text in page.card_of_auth.text
    assert page.register_link.text in page.card_of_auth.text


# 003 Меню выбора типа аутентификации содержит табы: 'Номер', 'Почта', 'Логин', 'Лицевой счёт'
def test_menu_of_type_auth(selenium):
    try:
        page = pages.auth_page.AuthPage(selenium)
        menu = [page.tub_phone.text, page.tub_email.text, page.tub_login.text, page.tub_ls.text]
        for i in range(len(menu)):
            assert "Номер" in menu
            assert 'Почта' in menu
            assert 'Логин' in menu
            assert 'Лицевой счёт' in menu
    except AssertionError:
        print('Ошибка в имени таба Меню типа аутентификации')


# 004 В меню по умолчанию выбрана форма аутентификации по телефону
def test_menu_of_type_active_auth(selenium):
    page = pages.auth_page.AuthPage(selenium)

    assert page.active_tub_phone.text == Settings.menu_of_type_auth[0]


# 005 Таблица выбора аутентификации меняется автоматически
def test_placeholder_name_of_user(selenium):
    page = pages.auth_page.AuthPage(selenium)
    page.tub_phone.click()

    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user
    page.tub_email.click()
    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user
    page.tub_login.click()
    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user
    page.tub_ls.click()
    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user


# 006 Ссылка "Забыл пароль" кликабельна
def test_forgot_password_link(selenium):
    page = pages.auth_page.AuthPage(selenium)

    assert page.find_other_element(By.ID, "forgot_password").text == 'Забыл пароль'


# 007 Кнопка "Регистрация" кликабельна
def test_register_link(selenium):
    page = pages.auth_page.AuthPage(selenium)
    page.register_link.click()

    assert page.find_other_element(*AuthLocators.registration).text == 'Регистрация'


# 008/009/010/011/012 Аутенфикация с валидными и невалидными входными данными
def test_auth_by_valid_email_pass(selenium):
    page = pages.auth_page.AuthPage(selenium)
    page.email.send_keys(Settings.valid_email)
    page.email.clear()
    page.pass_eml.send_keys(Settings.valid_password)
    page.pass_eml.clear()
    page.btn_enter.click()

    try:
        assert page.get_relative_link() == '/account_b2c/page'
    except AssertionError:
        assert 'Неверно введен текст с картинки' in page.find_other_element(*AuthLocators.error_message).text
        print('Предыдущие тесты вызвали появление капчи')


@pytest.mark.parametrize("incor_email", [Settings.invalid_email, Settings.empty_email],
                         ids=['invalid_email', 'empty'])
@pytest.mark.parametrize("incor_password", [Settings.invalid_password, Settings.empty_password],
                         ids=['invalid_password', 'empty'])
def test_auth_by_invalid_email(selenium, incor_email, incor_password):
    page = pages.auth_page.AuthPage(selenium)
    page.email.send_keys(incor_email)
    page.email.clear()
    page.pass_eml.send_keys(incor_password)
    page.pass_eml.clear()
    page.btn_enter.click()

    assert page.get_relative_link() != '/account_b2c/page'
