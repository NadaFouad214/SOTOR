import pytest
import softest
from ddt import ddt, file_data
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.signUp_page import sotorSignup
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json
import datetime


@pytest.mark.usefixtures("setup")
@ddt
class Testsotor(softest.TestCase):
    """signup"""
    @file_data('C:/pycharm_selenium/sotor/testdata/signUpData.json')
    def test_signUpSotor(self,name, email, password,confirm_password):
        si = sotorSignup(self.driver)
        si.signup(name,email, password,confirm_password)
        actual_result = si.validsignup()
        print(actual_result)

        expectedResult = "Confirm Your Email"

        self.soft_assert(self.assertEqual, expectedResult, actual_result)
        self.assert_all()