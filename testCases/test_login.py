import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger2 import LogGen
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("***********************Test_001_Login******************")
        self.logger.info("**************Verifying Home Page Title**********")
        self.driver = setup
        # self.log.info("Open app with url ", self.baseURL)
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        # self.log.info("Actual page title is {}".format(actual_title))
        expected_title = "Your store. Login"
        # self.log.info("Expected page title is ".format(expected_title))
        if actual_title == expected_title:
            assert True
            self.logger.info("Actual page title and expected page title are equal ")
            self.driver.close()
            self.logger.info("**************Home Page Title is Passed **********")
        else:
            self.logger.info("Actual and expected page titles are not matching ")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            #   self.log.info("Screenshot saved is " + ".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************Home Page Title is Failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************Verify login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        # self.log.info("Actual page title is ", actual_title)
        expected_title = "Dashboard / nopCommerce administration"
        # self.log.info("Expected page title is ", expected_title)
        if actual_title == expected_title:
            assert True
            self.logger.info("Actual page title and expected page title are equal ")
            self.logger.info("**************Login test is Passed **********")
            self.driver.close()
        else:
            self.logger.info("Actual and expected page titles are not matching ")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            #   self.log.info(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("**************Login test is Failed **********")
            assert False
