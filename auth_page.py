from pages import base_page, locators


class AuthPage(base_page.BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.phone = None
        self.password = None
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)

        self.tub_phone = driver.find_element(*locators.AuthLocators.tub_phone)
        self.active_tub_phone = driver.find_element(*locators.AuthLocators.active_tub_phone)
        self.tub_email = driver.find_element(*locators.AuthLocators.tub_email)
        self.email = driver.find_element(*locators.AuthLocators.auth_email)
        self.pass_eml = driver.find_element(*locators.AuthLocators.auth_pass_eml)
        self.btn_enter = driver.find_element(*locators.AuthLocators.auth_btn_enter)
        self.tub_login = driver.find_element(*locators.AuthLocators.tub_login)
        self.login = driver.find_element(*locators.AuthLocators.auth_login)
        self.pass_log = driver.find_element(*locators.AuthLocators.auth_pass_log)
        self.tub_ls = driver.find_element(*locators.AuthLocators.tub_ls)
        self.placeholder_name_of_user = driver.find_element(*locators.AuthLocators.placeholder_name_of_user)
        self.forgot_password_link = driver.find_element(*locators.AuthLocators.forgot_password_link)
        self.register_link = driver.find_element(*locators.AuthLocators.register_link)
        self.page_right = driver.find_element(*locators.AuthLocators.page_right)
        self.page_left = driver.find_element(*locators.AuthLocators.page_left)
        self.card_of_auth = driver.find_element(*locators.AuthLocators.card_of_auth)
        self.menu_tub = driver.find_element(*locators.AuthLocators.menu_tub)

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)
        
    def enter_phone(self, value):
        self.phone.send_keys(value)
