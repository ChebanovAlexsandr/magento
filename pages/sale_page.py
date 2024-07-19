from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text

    def check_item_category(self, text):
        item_category = self.find(loc.item_category_loc)
        assert item_category.text == text
