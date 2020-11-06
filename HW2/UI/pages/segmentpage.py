from UI.locators.basic_locators import SegmentPageLocators
from UI.pages.basepage import BasePage
import time


class SegmentPage(BasePage):
    locators = SegmentPageLocators()

    def create_segment(self):
        self.find(self.locators.AUDIENCE).click()
        time.sleep(2)
        a = self.find(self.locators.NUMBER_OF_DIF).text
        self.find(self.locators.CREATE).click()
        time.sleep(2)
        self.find(self.locators.CHECK_MARK).click()
        time.sleep(2)
        self.find(self.locators.ADD_SEGMENT_1).click()
        time.sleep(2)
        self.find(self.locators.ADD_SEGMENT_2).click()
        time.sleep(2)
        b = self.find(self.locators.NUMBER_OF_DIF).text
        if b > a:
            return True
        else:
            return False

    def delete_segment(self):
        self.find(self.locators.AUDIENCE).click()
        self.find(self.locators.DELETE_MARK).click()

        a = self.find(self.locators.NUMBER_OF_DIF).text
        self.find(self.locators.ACTIONS_BUTTON).click()
        self.find(self.locators.DELETE_SEGMENT).click()
        time.sleep(4)
        b = self.find(self.locators.NUMBER_OF_DIF).text
        if b < a:
            return True
        else:
            return False