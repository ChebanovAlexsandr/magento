from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_current_url(self, url):
        get_url = self.driver.current_url
        print(get_url)
        assert get_url == url
