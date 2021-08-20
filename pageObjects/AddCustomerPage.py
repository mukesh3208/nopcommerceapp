import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customers_menu_xpath = "//i[@class='nav-icon far fa-user']/following-sibling::p"
    link_customers_menuitem_xpath="//a[@href='/Admin/Customer/List']/p"
    link_add_new_xpath="//a[@href='/Admin/Customer/Create']"
    textbox_email_id="Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    textbox_gender_male_id = "Gender_Male"
    textbox_gender_female_id = "Gender_Female"
    textbox_dateofbirth_id = "DateOfBirth"
    textbox_companyname_id = "Company"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    checkbox_istaxexempt_id = "IsTaxExempt"
    listbox_newsletter_xpath = "//label[@id='SelectedNewsletterSubscriptionStoreIds_label']/../../following-sibling::div//div[@class='k-multiselect-wrap k-floatwrap']"
    listitem_newsletter_yourstorename_xpath="//li[text()='Your store name']"
    listitem_newsletter_teststore2_xpath = "//li[text()='Test store 2']"
    listbox_customerroles_xpath ="//label[@id='SelectedCustomerRoleIds_label']/../../following-sibling::div//div[@class='k-multiselect-wrap k-floatwrap']"
    listitem_registered_xpath = "//li[contains(text(),'Registered')]"
    listitem_registeredCross_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    listitem_administrators_xpath = "//li[contains(text(),'Administrators')]"
    listitem_forumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listitem_guests_xpath = "//li[contains(text(),'Guests')]"
    listitem_vendors_xpath = "//li[contains(text(),'Vendors')]"

    select_managerofvendor_id = "VendorId"
    selectitem_notavendor_visibleText = 'Not a vendor'
    selectitem_vendor1_visibleText = 'Vendor 1'
    selectitem_vendor2_visibleText = 'Vendor 2'
    textarea_admincomment_id = "AdminComment"

    button_save_name = 'save'
    text_addsuccessmsg_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomersMenu(self):
        self.driver.find_element_by_xpath(self.link_customers_menu_xpath).click()

    def clickCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.link_customers_menuitem_xpath).click()

    def clickaddNew(self):
        self.driver.find_element_by_xpath(self.link_add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def selectGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.radio_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.radio_gender_female_id).click()

    def setDateOfBirth(self, dateOfBirth):
        self.driver.find_element_by_id(self.textbox_dateofbirth_id).clear()
        self.driver.find_element_by_id(self.textbox_dateofbirth_id).send_keys(dateOfBirth)

    def setCompanyName(self, companyName):
        self.driver.find_element_by_id(self.textbox_companyname_id).clear()
        self.driver.find_element_by_id(self.textbox_companyname_id).send_keys(companyName)

    def selectIsTaxExempt(self, IsTaxExempt):
        if IsTaxExempt == 'Yes':
            self.driver.find_element_by_id(self.checkbox_istaxexempt_id).click()

    def setCustomerRoles(self, customerRole):
        self.driver.find_element_by_xpath(self.listbox_customerroles_xpath).click()
        time.sleep(3)
        if customerRole == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.listitem_registered_xpath)
        elif customerRole == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.listitem_administrators_xpath)
        elif customerRole == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath(self.listitem_registeredCross_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.listitem_guests_xpath)
        elif customerRole == 'Forum Moderators':
            self.listitem = self.driver.find_element_by_xpath(self.listitem_forumModerators_xpath)
        elif customerRole == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.listitem_vendors_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVendor(self,ManagerofVendor):
        self.driver.find_element_by_id(self.select_managerofvendor_id).click()
        self.sel = Select(self.driver.find_element_by_id(self.select_managerofvendor_id))
        if ManagerofVendor == 'Not a Vendor':
            self.sel.select_by_visible_text(self.selectitem_notavendor_visibleText)
        elif ManagerofVendor == 'Vendor 1':
            self.sel.select_by_visible_text(self.selectitem_vendor1_visibleText)
        elif ManagerofVendor == 'Vendor 2':
            self.sel.select_by_visible_text(self.selectitem_vendor2_visibleText)

    def setAdminComment(self, adminComment):
        self.driver.find_element_by_id(self.textarea_admincomment_id).send_keys(adminComment)

    def clickSave(self):
        self.driver.find_element_by_name(self.button_save_name).click()



