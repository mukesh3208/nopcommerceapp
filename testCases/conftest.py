import pytest
from selenium import webdriver
from utilities.customLogger2 import LogGen


@pytest.fixture()
def setup(browser):
    logger = LogGen.loggen()
    if browser == 'chrome':
        logger.info("Launching Chrome browser..........")
        driver=webdriver.Chrome(executable_path=r"C:\Users\kumarmu\Documents\pythonSelenium\nopcommerceapp\drivers\chromedriver.exe")
    elif browser == 'firefox':
        logger.info("Launching Firefox browser..........")
        driver=webdriver.Firefox(executable_path=r"C:\Users\kumarmu\Documents\pythonSelenium\nopcommerceapp\drivers\geckodriver.exe")
    else:
        logger.info("Launching Chrome browser..........")
        driver = webdriver.Chrome(executable_path=r"C:\Users\kumarmu\Documents\pythonSelenium\nopcommerceapp\drivers\chromedriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##########PyTest HTML Report #########

# It is a hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is a hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)