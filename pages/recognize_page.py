import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.signIn_page import sotor

class sotorRecog:
    def __init__(self, driver):
        self.driver = driver
        self.signIn = sotor(driver)

    rec_btn = '//*[@id="root"]/div[1]/div/section[1]/header/nav/div[2]/ul/li[2]/a'
    choose_language_btn = 'button[type="button"]'
    choose_language = 'div[role="group"]'
    file_btn = '//*[@id="root"]/div[1]/section/slot/slot/div/slot/div/div[2]/div[2]/input'
    start_recognation_btn = '//*[@id="root"]/div[1]/section/slot/slot/div/slot/div/div[3]/button'
    result = 'ml-4'

    def recognation(self,language,url):
        self.driver.find_element(By.XPATH, self.rec_btn).click()
        self.driver.implicitly_wait(5)
        self.signIn.signin("gafes89240@kravify.com","Tester123@")
        self.driver.find_element(By.XPATH, self.rec_btn).click()
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5)
        self.driver.find_element(By.CSS_SELECTOR, self.choose_language_btn).click()
        menu = self.driver.find_element(By.CSS_SELECTOR,self.choose_language)
        radio_buttons = menu.find_elements(By.CSS_SELECTOR, 'div[role="menuitemradio"]')

        desired_option = language
        for radio_button in radio_buttons:
            option_text = radio_button.text
            if option_text == desired_option:
                radio_button.click()
                break
        self.driver.find_element(By.XPATH, self.file_btn).send_keys(url)
        btn1 = self.driver.find_element(By.XPATH, self.start_recognation_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn1)
        btn1.click()

        time.sleep(5)

    def validRec(self):
            try:
                return self.driver.find_element(By.CLASS_NAME, self.result).text
            except NoSuchElementException:
                return "Failed to locate message element"
