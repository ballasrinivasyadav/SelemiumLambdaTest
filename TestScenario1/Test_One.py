import pytest
from TestScenario1.CheckoutPage import CheckoutPage
from TestScenario1.HomePage import HomePage


@pytest.mark.usefixtures
class TestOne:

    def testone(self, setup):

        #HomePageData
        simpleform = HomePage(self.driver)
        simpleform.getDemo().click()

        #HomePage
        simpleform.setenter().send_keys("Welcome Lambda Test")

        #CheckoutPage
        check = CheckoutPage(self.driver)
        check.getcheckoutpage().click()

        message = check.getmessage()
        assert ("Welcome Lambda Test" in message)
        print(message)
