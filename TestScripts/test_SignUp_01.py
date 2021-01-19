import pytest
from Pages.SignUp import SignUp
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen


class Test_SignUp_01():
        baseURL = ReadConfig.getApplicationURL()
        logger =LogGen.loggen()

        def test_signup(self,setup):
            self.logger.info("************* Test_SignUp_01**************")
            self.logger.info("User is on Homepage")

            self.driver= setup
            self.driver.get(self.baseURL)
            jio_Title = self.driver.title
            self.logger.info("User is clicking on",jio_Title)


