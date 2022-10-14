from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    form = (By.XPATH, "//a[normalize-space()='Input Form Submit']")
    name = (By.XPATH, "//input[@id='name']")
    email = (By.XPATH, "//input[@id='inputEmail4']")
    password = (By.XPATH, "//input[@id='inputPassword4']")
    company = (By.XPATH, "//input[@id='company']")
    website = (By.XPATH, "//input[@id='websitename']")
    country = (By.XPATH, "//select[@name='country']")
    city = (By.XPATH, "//input[@id='inputCity']")
    address1 = (By.XPATH, "//input[@id='inputAddress1']")
    address2 = (By.XPATH, "//input[@id='inputAddress2']")
    state = (By.XPATH, "//input[@id='inputState']")
    pincode = (By.XPATH, "//input[@id='inputZip']")

    def getInputform(self):
        return self.driver.find_element(*HomePage.form)

    def getName(self):
        return self.driver.find_element(*HomePage.name).send_keys("Srinivas")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email).send_keys("Srinivasballa07@gmail.com")

    def getPassword(self):
        return self.driver.find_element(*HomePage.password).send_keys("Srinivasballa07")

    def getCompany(self):
        return self.driver.find_element(*HomePage.company).send_keys("Srinivasballa.com")

    def getWebsite(self):
        return self.driver.find_element(*HomePage.website).send_keys("Srinivas.com")

    def getCountry(self):
        sel = Select(self.driver.find_element(*HomePage.country))
        sel.select_by_visible_text("United States")

    def getCity(self):
        return self.driver.find_element(*HomePage.city).send_keys("Hyderabad")

    def getAddressOne(self):
        return self.driver.find_element(*HomePage.address1).send_keys("Hyderabad")

    def getAddressTwo(self):
        return self.driver.find_element(*HomePage.address2).send_keys("Hyderabad")

    def getState(self):
        return self.driver.find_element(*HomePage.state).send_keys("Telangana")

    def getPincode(self):
        return self.driver.find_element(*HomePage.pincode).send_keys("500012")

    def getSuccess(self):
        success = self.driver.find_element(By.XPATH, "//p[@class='success-msg hidden']").text
        assert "Thanks for contacting us, we will get back to you shortly" in success
        print(success)
