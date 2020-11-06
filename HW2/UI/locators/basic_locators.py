from selenium.webdriver.common.by import By


class BasePageLocators(object):

    BUY_ADV = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    GO_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')


class HomePageLocators(BasePageLocators):
    CREATE_COMPANY = (By.CLASS_NAME, 'button-module-textWrapper-3LNyYP')
    AUDIENCE = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[2]/a')

class CreateCompanyLocators(HomePageLocators):
    TYPE_COMPANY = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]')
    URL_COMPANY = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input')
    BANNER = (By.XPATH, '//*[@id="patterns_4"]/span')
    PHOTO = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div')
    ADD_PHOTO = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input')
    CONFIRM = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button')
    NUMBER_OF_COMPANY = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[4]/div[1]/span/span[3]')

class SegmentPageLocators(HomePageLocators):
    CREATE = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[5]/div[1]/button')
    CHECK_MARK = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/input')
    ADD_SEGMENT_1 = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[5]/div[1]/button/div')
    ADD_SEGMENT_2 = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/button/div')

    ############################## DELETE ##############################

    DELETE_MARK = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/input')
    ACTIONS_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[5]/div[2]/div/div/div[1]')
    DELETE_SEGMENT = (By.XPATH, '/html/body/div[6]/div/div/div/div/ul/li')

    NUMBER_OF_DIF = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[2]/div[1]/span/span[3]')





