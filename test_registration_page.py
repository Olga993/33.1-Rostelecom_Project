from pages.locators import AuthLocators
from pages.register_page import RegisterPage

from settings import *


# 013 Левая часть формы «Регистрация» содержит логотип и продуктовый слоган
def test_page_left_registration(selenium):
    try:
        page_reg = RegisterPage(selenium)
        assert page_reg.page_left_registration.text != ''
    except AssertionError:
        print('Элемент отсутствует в левой части формы')


# 014 Формы «Регистрация» содержит основные элементы:
# поля ввода: Имя, Фамилия, Регион, email, Пароль, Подтверждение пароля; кнопка "Продолжить"
def test_elements_of_register(selenium):
    try:
        page_reg = RegisterPage(selenium)
        card_of_reg = [page_reg.first_name, page_reg.last_name, page_reg.address_registration,
                       page_reg.email_registration, page_reg.password_registration,
                       page_reg.password_registration_confirm, page_reg.registration_btn]
        for i in range(len(card_of_reg)):
            assert page_reg.first_name in card_of_reg
            assert page_reg.last_name in card_of_reg
            assert page_reg.email_registration in card_of_reg
            assert page_reg.address_registration in card_of_reg
            assert page_reg.password_registration in card_of_reg
            assert page_reg.password_registration_confirm in card_of_reg
            assert page_reg.registration_btn in card_of_reg
    except AssertionError:
        print('Элемент отсутствует в форме «Регистрация»')


# 015 Названия элементов формы «Регистрация» соответствуют указанным
def test_names_elements_of_register(selenium):
    try:
        page_reg = RegisterPage(selenium)
        assert 'Имя' in page_reg.card_of_registration.text
        assert 'Фамилия' in page_reg.card_of_registration.text
        assert 'Регион' in page_reg.card_of_registration.text
        assert 'E-mail или мобильный телефон' in page_reg.card_of_registration.text
        assert 'Пароль' in page_reg.card_of_registration.text
        assert 'Подтверждение пароля' in page_reg.card_of_registration.text
        assert 'Продолжить' in page_reg.card_of_registration.text
    except AssertionError:
        print('Название элемента в форме «Регистрация» не соответствует Требованию')


# 016 Регистрация с валидными данными
def test_register_by_valid_data(selenium):
    page_reg = RegisterPage(selenium)
    page_reg.first_name.send_keys(Settings.f_name)
    page_reg.first_name.clear()
    page_reg.last_name.send_keys(Settings.l_name)
    page_reg.last_name.clear()
    page_reg.email_registration.send_keys(Settings.valid_email_for_reg)
    page_reg.email_registration.clear()
    page_reg.password_registration.send_keys(Settings.valid_password)
    page_reg.password_registration.clear()
    page_reg.password_registration_confirm.send_keys(Settings.valid_password)
    page_reg.password_registration_confirm.clear()
    page_reg.registration_btn.click()


# 017 Регистрация с валидными данными:
# в поле ввода "Имя" и "Фамилия" - знак тире (-)
def test_register_by_valid_data_(selenium):
    page_reg = RegisterPage(selenium)
    page_reg.first_name.send_keys(Settings.f_name_)
    page_reg.first_name.clear()
    page_reg.last_name.send_keys(Settings.l_name_)
    page_reg.last_name.clear()
    page_reg.email_registration.send_keys(Settings.valid_email_for_reg)
    page_reg.email_registration.clear()
    page_reg.password_registration.send_keys(Settings.valid_password)
    page_reg.password_registration.clear()
    page_reg.password_registration_confirm.send_keys(Settings.valid_password)
    page_reg.password_registration_confirm.clear()
    page_reg.registration_btn.click()


# 018 Поля ввода "Пароль" и "Подтвердить пароль" с валидными данными
# (пароли совпадают)
def test_password_registration_confirm_valid_data(selenium):
    page_reg = RegisterPage(selenium)
    page_reg.password_registration.send_keys(Settings.password1)
    page_reg.password_registration.clear()
    page_reg.password_registration_confirm.send_keys(Settings.password1)
    page_reg.password_registration_confirm.clear()
    page_reg.registration_btn.click()


# 019 Поля ввода "Пароль" и "Подтвердить пароль" валидными данными
# (пароли не совпадают)
def test_password_registration_confirm_invalid_data(selenium):
    page_reg = RegisterPage(selenium)
    page_reg.password_registration.send_keys(Settings.password1)
    page_reg.password_registration.clear()
    page_reg.password_registration_confirm.send_keys(Settings.password1)
    page_reg.password_registration_confirm.clear()
    page_reg.registration_btn.click()

    assert 'Пароли не совпадают' not in page_reg.container_password_confirm.text


# 020 Регистрация пользователя по email, который был использован ранее для регистрации
def test_register_by_invalid_data(selenium):
    page_reg = RegisterPage(selenium)
    page_reg.first_name.send_keys(Settings.f_name)
    page_reg.first_name.clear()
    page_reg.last_name.send_keys(Settings.l_name)
    page_reg.last_name.clear()
    page_reg.email_registration.send_keys(Settings.valid_email)
    page_reg.email_registration.clear()
    page_reg.password_registration.send_keys(Settings.valid_password)
    page_reg.password_registration.clear()
    page_reg.password_registration_confirm.send_keys(Settings.valid_password)
    page_reg.password_registration_confirm.clear()
    page_reg.registration_btn.click()

    assert "Учётная запись уже существует" in page_reg.find_other_element(*AuthLocators.error_account_exists).text
