import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger2 import LogGen
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login **************")
        self.logger.info("**************Verify login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        lst_status=[]
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1',r ,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp=="Pass":
                    self.logger.info("******Passed****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("******Failed****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif  actual_title != expected_title:
                if self.exp == "Pass":
                    self.logger.info("******Failed****")

                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******Passed****")

                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test case is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test case is Failed")
            self.driver.close()
            assert False
        self.logger.info("*******End of Login DDT Test********")
        self.logger.info("*****Completed TC_LoginDDT_002*********")