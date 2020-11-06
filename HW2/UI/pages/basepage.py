
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from UI.locators import basic_locators


class BasePage(object):
    locators = basic_locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None)-> WebElement:
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        button.click()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def go_to_password(self):
        self.click(self.locators.BUY_ADV)

    def login(self, email, password):
        search_field = self.find(self.locators.EMAIL)
        search_field.clear()
        search_field.send_keys(email)
        search_field = self.find(self.locators.PASSWORD)
        search_field.clear()
        search_field.send_keys(password)
        self.find(self.locators.GO_BUTTON).click()


    def go_to_home_page(self):
        self.go_to_password()
        self.login("anlvovskay@mail.ru", "Anastya")






