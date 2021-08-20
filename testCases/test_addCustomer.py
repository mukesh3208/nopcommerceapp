import random
import string

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger2 import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********Test_003_AddCustomer**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login successful*************")

        self.logger.info("********** Starting Add Customer Test ********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomersMenu()
        self.addcust.clickCustomersMenuItem()
        self.addcust.clickaddNew()

        self.logger.info("********** Providing Customer Info ********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("123456")
        self.addcust.setFirstName("Mukesh")
        self.addcust.setLastName("Kumar")
        self.addcust.selectGender("Male")
        self.addcust.setDateOfBirth("01/01/1985")
        self.addcust.setCompanyName("Mukesh QA")
        self.addcust.selectIsTaxExempt("Yes")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerofVendor("Vendor 1")
        self.addcust.setAdminComment("Hi! Welcome Mukesh!!")
        self.addcust.clickSave()

        self.successMsg= self.driver.find_element_by_xpath(self.addcust.text_addsuccessmsg_xpath).text

        if 'The new customer has been added successfully.' in self.successMsg:
            assert True
            self.logger.info("***** Add Cutomer Test Passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.error("********* Add customer test failed *********")
            assert False

        self.driver.close()
        self.logger.info("***********Ending Home Page title test ***********")
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))