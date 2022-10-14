import pytest
from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self,driver):
        self.driver = driver
    demo = (By.XPATH,"//a[normalize-space()='Simple Form Demo']")
    enterMessage = (By.XPATH,"//input[@id='user-message']")
    def getDemo(self):
        return self.driver.find_element(*HomePage.demo)
    def setenter(self):
        return self.driver.find_element(*HomePage.enterMessage)



