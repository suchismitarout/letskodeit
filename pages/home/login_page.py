from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class LoginPage(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "Login"
    _user_email = "user_email"
    _password = "user_password"
    _login_button = "commit"
    _user_icon = "//span[@class='navbar-current-user']"
    _invalid_login = "//div[contains(text(),'Invalid email or password')]"

    # def get_login_link(self):
    #     return self.driver.find_element_by_link_text(self._login_link)
    #
    # def get_email(self):
    #     return self.driver.find_element_by_id(self._user_email)
    #
    # def get_passwd(self):
    #     return self.driver.find_element_by_id(self._password)
    #
    # def click_login(self):
    #     return self.driver.find_element_by_name(self._login_button)

    def click_login_link(self):
        self.elementclick(self. _login_link,locatortype='linktext')
        time.sleep(2)

    def enter_email(self,email):
        self.sendkeys(email,self._user_email)

    def enter_pwd(self,pwd):
        self.sendkeys(pwd,self._password)

    def clicklogin(self):
        self.elementclick(self._login_button,locatortype='name')
        time.sleep(2)

    def login(self,email,pwd):
        self.click_login_link()
        self.enter_email(email)
        self.enter_pwd(pwd)
        self.clicklogin()


    def verifylogin(self):
        result = self.iselementpresent(self._user_icon,locatortype='xpath')
        return result

    def verifyinvalidlogin(self):
        result = self.iselementpresent(self._invalid_login,locatortype='xpath')
        return result