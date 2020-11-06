

import pytest
from _pytest.fixtures import FixtureRequest


from UI.pages.basepage import BasePage
from UI.pages.homepage import HomePage
from UI.pages.segmentpage import SegmentPage
from UI.pages.createcompanypage import CreateCompanyPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.basepage: BasePage = request.getfixturevalue('base_page')
        self.homepage: HomePage = request.getfixturevalue('home_page')
        self.segmentpage: SegmentPage = request.getfixturevalue('segment_page')
        self.createcompanypage: CreateCompanyPage = request.getfixturevalue('create_company_page')

