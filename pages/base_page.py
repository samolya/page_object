from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open_browser(self):
        self.driver.get(self.url)

    def is_element_present(self, how_search, what_search):
        try:
            self.driver.find_element(how_search, what_search)
        except NoSuchElementException:
            return False
        return True
