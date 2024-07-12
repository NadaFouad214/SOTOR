import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class sotorRequest:
    def __init__(self, driver):
        self.driver = driver

    request_on_prem_btn = '//*[@id="root"]/div[1]/div/section[1]/header/nav/div[2]/ul/li[3]/a'
    first_name = '//*[@id="first_name"]'
    last_name = 'input[placeholder="Last Name"]'
    business_email = 'input[type="email"]'
    phone_number = 'input[placeholder="Phone Number"]'
    country_list = '//*[@id=":rm:-form-item"]'
    city = '//*[@id="city"]'
    project_details = '//*[@id="project_details"]'
    Estimated_annually_processed_pages_1 = '//div/label[contains(text(),"less than 10,000 A4 Pages")]'
    Estimated_annually_processed_pages_2 = '//div/label[contains(text(),"10,000 - 50,000 A4 Pages")]'
    Estimated_annually_processed_pages_3 = '//div/label[contains(text(),"  50,000 to 200,000 A4 Pages")]'
    Estimated_annually_processed_pages_4 = '//div/label[contains(text(),"  200,000 to 500,000 A4 Pages")]'
    terms_check = '//div/label[contains(text(),"By clicking Create account, I agree that I have read and accepted")]'
    submit_btn = '//div/button[contains(text(),"Submit a Request")]'
    choose_country_btn = '//*[@id="root"]/div[1]/section/div[2]/div/form/div/div[4]/div/div/div'
    country_btn = ''

    def scroll_down(self):
        # Scroll down using JavaScript
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def request_on_prem(self, Fname, Lname, Email, Country_code, Number, ProjectDetails, Country, City):
        self.driver.find_element(By.XPATH, self.request_on_prem_btn).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.first_name))).send_keys(
            Fname)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, self.last_name).send_keys(Lname)
        self.driver.find_element(By.CSS_SELECTOR, self.business_email).send_keys(Email)
        self.driver.find_element(By.XPATH, self.choose_country_btn).click()
        option = self.driver.find_element(By.XPATH, '//*[@id="react-international-phone__' + Country_code + '-option"]')
        option.click()

        self.driver.find_element(By.CSS_SELECTOR, self.phone_number).send_keys(Number)
        self.driver.find_element(By.ID, "rfs-btn").click()

        option = self.driver.find_element(By.XPATH, '//*[@id="rfs-' + Country + '"]/span')
        option.click()
        self.driver.find_element(By.XPATH, self.city).send_keys(City)
        self.driver.find_element(By.XPATH, self.project_details).send_keys(ProjectDetails)

        for _ in range(3):
            self.scroll_down()
            #time.sleep(1)

        self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 3)
        btn1 = self.driver.find_element(By.XPATH, self.Estimated_annually_processed_pages_1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn1)
        # btn1.click()

        btn2 = self.driver.find_element(By.XPATH, self.Estimated_annually_processed_pages_2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn2)
        # btn2.click()

        btn3 = self.driver.find_element(By.XPATH, self.Estimated_annually_processed_pages_3)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn3)
        # btn3.click()

        btn4 = self.driver.find_element(By.XPATH, self.Estimated_annually_processed_pages_4)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn4)
        btn4.click()

        self.driver.find_element(By.XPATH, self.terms_check).click()
        submitting=self.driver.find_element(By.XPATH, self.submit_btn).click()

        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)

    def validRequest(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "go2072408551").is_displayed()
        except NoSuchElementException:
            return False, "Failed to locate message element"
