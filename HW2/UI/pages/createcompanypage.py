from UI.locators.basic_locators import CreateCompanyLocators
from UI.pages.basepage import BasePage
import time
import pyautogui


class CreateCompanyPage(BasePage):
    locators = CreateCompanyLocators()

    def create_company(self):
        a = self.find(self.locators.NUMBER_OF_COMPANY).text
        time.sleep(2)
        self.find(self.locators.CREATE_COMPANY).click()
        time.sleep(2)
        self.find(self.locators.TYPE_COMPANY).click()
        search_field = self.find(self.locators.URL_COMPANY)
        search_field.clear()
        search_field.send_keys('https://vk.com/suff_well')
        self.find(self.locators.BANNER).click()
        photo_download = self.find(self.locators.PHOTO)
        photo_download.click()
        time.sleep(2)
        pyautogui.write('C:\\Users\\ulvov\\Pictures\\selenium IDE.png')
        pyautogui.press('enter')
        self.find(self.locators.ADD_PHOTO).click()
        time.sleep(2)
        self.find(self.locators.CONFIRM).click()
        time.sleep(6)
        b = self.find(self.locators.NUMBER_OF_COMPANY).text
        if b > a:
            return True
        else:
            return False
