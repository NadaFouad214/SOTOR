import pytest
from selenium.webdriver.common.by import By

from pages.recognize_page import sotorRecog
import softest
from ddt import ddt, file_data, data, unpack

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
@ddt
class Testrecognation(softest.TestCase):

    @file_data('C:/pycharm_selenium/sotor/testdata/recognationData.json')
    def test_signIn(self,language,url):
        si =sotorRecog(self.driver)
        si.recognation(language,url)
        actual_res = si.validRec()
        # print(actual_res)
        expectedResult = "Recognition was completed successfully, you can now start generating your output."
        self.soft_assert(self.assertEqual, expectedResult, actual_res)
        self.assert_all()



