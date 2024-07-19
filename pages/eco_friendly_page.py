from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text

    def check_item_category(self, text):
        item_category = self.find(loc.item_category_loc)
        assert item_category.text == text
