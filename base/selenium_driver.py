from selenium.webdriver.common.by import By

class SeleniumDriver():
    def __init__(self,driver):
        self.driver = driver

    def getbytype(self,locatortype):
        locatortype = locatortype.lower()
        if locatortype == 'id':
            return By.ID
        if locatortype == 'class':
            return By.CLASS_NAME
        if locatortype == 'xpath':
            return By.XPATH
        if locatortype == 'name':
            return By.NAME
        if locatortype == 'css':
            return By.CSS_SELECTOR
        if locatortype == 'linktext':
            return By.LINK_TEXT
        else:
            print("Entered locator type {} is invalid. Please enter a valid one.".format(locatortype))
        return False

    def getelement(self, locator, locatortype='id'):
        element = None
        try:
            locatortype = locatortype.lower()
            getby = self.getbytype(locatortype)
            element = self.driver.find_element(getby,locator)
            print("element found")
        except:
            print("element not found")
        return element

    def elementclick(self,locator,locatortype='id'):
        try:
            element = self.getelement(locator,locatortype)
            element.click()
            print("element clicked with loactor {} & locatortyp {}".format(locator,locatortype))
        except:
            print("element not clicked with loactor {} & locatortyp {}".format(locator,locatortype))

    def sendkeys(self,data,locator,locatortype='id'):
        try:
            element = self.getelement(locator,locatortype)
            element.send_keys(data)
            print("element found and keys has sent to element")
        except:
            print("element not found ")



    def iselementpresent(self, locator,locatortype='id'):
        try:
            element = self.getelement(locator,locatortype)
            if element is not None:
                print("element is present")
                return True
            else:
                print("element is not present")
                return False
        except:
            print("element is not present")
            return False

    def elementscheck(self,locator,getby):
        try:
            element_list = self.driver.find_elements(getby, locator)
            if len(element_list) > 0:
                print("element list found")
                return True
            else:
                print("elements not found")
                return False
        except:
            print("element list not found")
            return False




