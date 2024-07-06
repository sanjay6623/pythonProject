
import pytest
import time
from selenium.webdriver.common.by import By

from pageObjects.Search_customerPage import SearchCustomer
from utilites.customLogger import LogGen
from utilites.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer

@pytest.mark.usefixtures("setup")
class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomer(self):
        self.logger.info("***** Test_004_SearchCustomer *******")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successfully *********")
        self.logger.info("****** Starting Search Customer Test *******")

        self.AddCust=AddCustomer(self.driver)
        time.sleep(4)
        self.AddCust.clickOnCustomerMenu()

        self.AddCust.clickOnCustomerMenuItem()
        time.sleep(4)
        self.SC=SearchCustomer(self.driver)
        self.logger.info("****** Entering Email for Search*********")
        self.SC.setEmail("kiyjcycyhjc676008@gmail.com")
        self.SC.setFirstName("Virat")
        self.SC.lastName("Kohli")
        self.SC.clickSearch_btn()
        self.logger.info("******** Entering First and Last Name*******")
        self.SC.searchContactByEmail("kiyjcycyhjc676008@gmail.com")
        status=self.SC.searchContactByEmail("kiyjcycyhjc676008@gmail.com")

        self.SC.searchByName("Virat Kohli")
        time.sleep(4)
        self.logger.info("*******Search Result validation Done********")





