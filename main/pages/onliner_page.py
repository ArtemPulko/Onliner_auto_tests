from selenium.webdriver.remote.webelement import WebElement
from ..pages import MainPageLocators
from .base_page import BasePage

class OnlinerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = 'https://www.onliner.by/'

    @property
    def url(self) -> str:
        """
        Свойство возвращает url главной страницы онлайнера.
        :return: Строка с url.
        """
        return self._url

    @property
    def mobile_phone_catalog(self) -> WebElement:
        """
        Свойство для поиска кнопки перехода в каталог.
        :return: WebElement кнопки перехода в каталог мобильных телефонов.
        """
        return self.find_by_xpath_clickable_elem(MainPageLocators.catalog_link.value)

