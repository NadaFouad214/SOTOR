import pytest
import softest
from ddt import ddt, file_data
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.requestOnPrem_page import sotorRequest
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json
import datetime


@pytest.mark.usefixtures("setup")
@ddt
class Testsotor(softest.TestCase):
    """signup"""
    @file_data('C:/pycharm_selenium/sotor/testdata/requestOnPremData.json')
    def test_requestsotor(self, Fname, Lname, Email,Country_code ,Number, ProjectDetails, Country,City):
        si = sotorRequest(self.driver)
        si.request_on_prem(Fname, Lname, Email,Country_code, Number, ProjectDetails, Country,City)
        actual_result = si.validRequest()
        print(actual_result)
        expectedResult = True
        self.soft_assert(self.assertEqual, expectedResult, actual_result)
        self.assert_all()