import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class sotorSignup:
    def __init__(self, driver):
        self.driver = driver

    signup_btn = '//*[@id="root"]/div[1]/div/section[1]/header/nav/div[3]/button[2]'
    name = 'input[type="text"]'
    email = 'input[type="email"]'
    password = 'input[type="password"]'
    confirm_password = 'input[placeholder="Password confirm"]'
    create_btn = '//*[@id="root"]/div[1]/div/div/div[2]/form/div[3]/button'

    def signup(self, Name, Email, Password, confirm_password):

        self.driver.find_element(By.XPATH, self.signup_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.name).send_keys(Name)
        self.driver.find_element(By.CSS_SELECTOR, self.email).send_keys(Email)
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys(Password)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, self.confirm_password).send_keys(confirm_password)
        self.driver.find_element(By.XPATH, self.create_btn).click()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        time.sleep(2)

    def validsignup(self):
        try:
            return self.driver.find_element(By.XPATH,
                                            '//*[@id="root"]/div[1]/div/section/div[2]/div/h3').text
        except NoSuchElementException:
            return False, "Failed to locate message element"
