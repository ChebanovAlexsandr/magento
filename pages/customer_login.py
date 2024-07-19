from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import login_locators as loc
from faker import Faker

from utils import project_ec


class CustomerLogin(BasePage):
    page_url = '/customer/account/create/'

    def fill_login_form(self):
        faker = Faker("en_US")
        password = faker.password()
        first_name = self.find(loc.first_name_loc)
        last_name = self.find(loc.last_name_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        password_confirm = self.find(loc.password_confirm_loc)
        button_create = self.find(loc.button_create_an_account_loc)
        first_name.send_keys(faker.first_name())
        last_name.send_keys(faker.last_name())
        email_field.send_keys(faker.email())
        password_field.send_keys(password)
        password_confirm.send_keys(password)
        button_create.click()

    def check_alert_text(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.error_locator_loc))

        error_alert = self.driver.find_element(*loc.error_locator_loc)
        assert error_alert.text == text

    def busy_mail(self, email):
        faker = Faker("en_US")
        password = faker.password()
        first_name = self.find(loc.first_name_loc)
        last_name = self.find(loc.last_name_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        password_confirm = self.find(loc.password_confirm_loc)
        button_create = self.find(loc.button_create_an_account_loc)
        first_name.send_keys(faker.first_name())
        last_name.send_keys(faker.last_name())
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm.send_keys(password)
        button_create.click()

    def check_error_alert_text_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.error_locator_loc))

        error_alert = self.driver.find_element(*loc.error_locator_loc)
        assert error_alert.text == text
