from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class sotor:
    def __init__(self, driver):
        self.driver = driver

    signin_btn = "//div/button[contains(text(),'Sign in')]"
    email = 'input[type="email"]'
    password = 'input[type="password"]'
    checkbox = '//*[@id="login"] '
    create_btn = "//div/button[contains(text(),'Sign In with Email')]"

    def signin_button(self):
        self.driver.find_element(By.XPATH, self.signin_btn).click()

    def signin(self, Email, Password):
        self.driver.find_element(By.CSS_SELECTOR, self.email).send_keys(Email)
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys(Password)
        self.driver.find_element(By.XPATH, self.checkbox).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.create_btn).click()
        self.driver.implicitly_wait(5)

    def validResult(self):
        try:
            return self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div').text
        except NoSuchElementException:
            return False, "Failed to locate message element"
