import pytest
from selenium.webdriver.common.by import By

from pages.signIn_page import sotor
import softest
from ddt import ddt, file_data, data, unpack

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
@ddt
class Testsign_in(softest.TestCase):
    """tc1:valid signin"""

    @file_data('C:/pycharm_selenium/sotor/testdata/signInData.json')
    def test_signIn(self, email, password):
        si = sotor(self.driver)
        si.signin_button()
        si.signin(email, password)
        actual_res = si.validResult()
        #print(actual_res)
        expectedResult = "User Successfully Login"
        self.soft_assert(self.assertEqual, expectedResult, actual_res)
        self.assert_all()


