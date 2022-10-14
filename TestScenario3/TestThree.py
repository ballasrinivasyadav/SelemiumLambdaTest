import time
import pytest
from TestScenario3.HomePage import HomePage
from TestScenario3.submitButton import SubmitButton

@pytest.mark.usefixture
class TestThree:

    def testthree(self,setup):

        home = HomePage(self.driver)
        home.getInputform().click()

        submitbutton = SubmitButton(self.driver)
        submitbutton.getSubmit().click()
        time.sleep(5)
        submitbutton.getFillout()

        time.sleep(10)
        home.getName()

        home.getEmail()

        home.getPassword()

        home.getCompany()

        home.getWebsite()

        time.sleep(5)
        home.getCountry()

        home.getCity()

        home.getAddressOne()

        home.getAddressTwo()

        home.getState()

        home.getPincode()

        submitbutton.getSubmit().click()

        home.getSuccess()



