# import openpyxl
import os
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest_html

from openpyxl import Workbook
import datetime


@pytest.fixture(autouse=True)
def setup(request):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.get("https://dev.sotoor.ai/")
    request.cls.driver = driver
    yield driver
    driver.close()




@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    config.option.htmlpath =f"C:/pycharm_selenium/sotor/reports/test_report_{timestamp}.html"
