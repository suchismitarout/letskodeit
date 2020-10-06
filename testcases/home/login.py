from selenium import webdriver
from pages.home.login_page import LoginPage
import time
import unittest
import pytest

class LoginTest(unittest.TestCase):
    apt = webdriver.ChromeOptions()
    apt.add_argument("user-data-dir=C:/Users/Suchismita/AppData/Local/Google/Chrome/User Data/Profile 1")
    driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe", options=apt)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get("https://letskodeit.teachable.com/")
        self.driver.maximize_window()
        log_page = LoginPage(self.driver)
        log_page.login("test@email.com","abcabc")
        time.sleep(2)
        result = log_page.verifylogin()
        assert result == True
        self.driver.quit()
        # user_icon = driver.find_element_by_xpath("//span[@class='navbar-current-user']")
        # if user_icon is not None:
        #     print("login is successful.")
        # else:
        #     print("login failed.")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get("https://letskodeit.teachable.com/")
        self.driver.maximize_window()
        log_page = LoginPage(self.driver)
        log_page.login("test@email.com", "abcabcx")
        time.sleep(2)
        result = log_page.verifyinvalidlogin()
        assert result == True


# ff = LoginTest()
# ff.test_valid_login()
