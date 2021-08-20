from selenium.webdriver.support.select import Select


class searchCustomer:
    textbox_email_id="SearchEmail"
    textbox_firstName_id = "SearchFirstName"
    textbox_lastName_id = "SearchLastName"
    select_dobMonth_id = "SearchMonthOfBirth"
    select_dobDay_id = "SearchDayOfBirth"
    textbox_company_id = "SearchCompany"
    textbox_ipAddress_id = "SearchIpAddress"
    button_search_id = "search-customers"

    table_searchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_column_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element_by_id(self.textbox_firstName_id).clear()
        self.driver.find_element_by_id(self.textbox_firstName_id).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_id(self.textbox_lastName_id).clear()
        self.driver.find_element_by_id(self.textbox_lastName_id).send_keys(lastname)

    def setdobMonth(self,dobmonth):
        self.driver.find_element_by_id(self.select_dobMonth_id).click()
        self.sel = Select(self.driver.find_element_by_id(self.select_dobMonth_id))
        self.sel.select_by_visible_text(dobmonth)

    def setdobDay(self,dobday):
        self.driver.find_element_by_id(self.select_dobDay_id).click()
        self.sel = Select(self.driver.find_element_by_id(self.select_dobDay_id))
        self.sel.select_by_visible_text(dobday)

    def setCompany(self,company):
        self.driver.find_element_by_id(self.textbox_company_id).clear()
        self.driver.find_element_by_id(self.textbox_company_id).send_keys(company)

    def setipaddress(self, ipaddress):
        self.driver.find_element_by_id(self.textbox_ipAddress_id).clear()
        self.driver.find_element_by_id(self.textbox_ipAddress_id).send_keys(ipaddress)

    def clickSearch(self):
        self.driver.find_element_by_id(self.button_search_id).click()

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.table_column_xpath))

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.table_rows_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
