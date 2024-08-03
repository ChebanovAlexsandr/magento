from selenium import webdriver
import pytest
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
from pages.eco_friendly_page import EcoPage
from selenium.webdriver.remote.webdriver import WebDriver


class Chrome(WebDriver):

    def __init__(self, remote_host, remote_port):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')

        super().__init__(
            command_executor=f"http://{remote_host}:{remote_port}/wd/hub",
            options=chrome_options
        )


@pytest.fixture
def driver():
    browser = Chrome(
        remote_host="localhost",
        remote_port=4444
    )
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)


@pytest.fixture()
def eco_page(driver):
    return EcoPage(driver)
