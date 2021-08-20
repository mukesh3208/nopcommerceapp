import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import searchCustomer
from utilities.customLogger2 import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login successful*************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomersMenu()
        self.addcust.clickCustomersMenuItem()

        searchcust = searchCustomer(self.driver)
        searchcust.setEmail("mukesh3208@gmail.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("mukesh3208@gmail.com")
        assert True == status
        self.driver.close()