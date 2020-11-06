import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from UI.pages.basepage import BasePage
from UI.pages.homepage import HomePage
from UI.pages.segmentpage import SegmentPage
from UI.pages.createcompanypage import CreateCompanyPage


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def home_page(driver):
    return HomePage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture
def create_company_page(driver):
    return CreateCompanyPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        prefs = {"download.default_directory": download_dir}
        options.add_experimental_option('prefs', prefs)

        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install(),
                                   options=options,
                                   desired_capabilities={'acceptInsecureCerts': True}
                                   )
        #driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub/',
        #                          options=options,
        #                          desired_capabilities={'acceptInsecureCerts': True}
        #                         )

    elif browser == 'firefox':
        manager = GeckoDriverManager(version=version)
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    # quit = закрыть страницу, остановить browser driver
    # close = закрыть страницу, бинарь browser driver останется запущенным
    driver.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver

    driver.quit()


