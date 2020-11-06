
import pytest
import time
from base import BaseCase
import allure
from allure_commons.types import AttachmentType


class Test(BaseCase):
    def test_author_positive(self):
        self.basepage.go_to_password()
        self.basepage.login("anlvovskay@mail.ru", "Anastya")
        time.sleep(3)
        assert "Кампании" in self.driver.page_source

    def test_author_negative(self):
        time.sleep(5)
        self.basepage.go_to_password()
        self.basepage.login("cdcghh@mail.ru", "Anastya")
        assert "Error" in self.driver.page_source

    def test_create_company(self):
        self.basepage.go_to_home_page()
        time.sleep(3)
        a = self.createcompanypage.create_company()
        time.sleep(6)
        assert a

    def test_create_segment(self):
        with allure.step('Go to home page'):
            self.basepage.go_to_home_page()
        time.sleep(3)
        a = self.segmentpage.create_segment()
        with allure.step('Attach screenshot'):
            allure.attach(name='Segment', body=self.driver.get_screenshot_as_png(),
                          attachment_type=AttachmentType.PNG)
        assert a

    def test_delete_segment(self):
        self.basepage.go_to_home_page()
        time.sleep(3)
        a = self.segmentpage.delete_segment()
        time.sleep(3)
        assert a













