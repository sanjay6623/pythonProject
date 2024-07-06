import random
import uuid
import pytest
import time

from selenium.webdriver.common.by import By

from utilites.customLogger import LogGen
from utilites.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer

@pytest.mark.usefixtures("setup")
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self):
        self.logger.info("***** Test_003_AddCustomer *******")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successfully *********")
        self.logger.info("****** Starting Add Customer Test *******")

        self.AddCust=AddCustomer(self.driver)
        time.sleep(4)
        self.AddCust.clickOnCustomerMenu()

        self.AddCust.clickOnCustomerMenuItem()
        time.sleep(4)
        self.AddCust.clickOnAddNew()
        self.logger.info("**** Provide Customer info********")
        self.email = self.generate_user_id() + "@gmail.com"
        #time.sleep(4)
        self.AddCust.setEmail(self.email)
        self.AddCust.sefPassword("sanjay")
        self.AddCust.sefFirstName("sanju")
        self.AddCust.sefLastName("kumar")
        self.AddCust.clickOnGender("Male")
        self.AddCust.clickOnDateBirth("01/01/1984")
        self.AddCust.setCompneyName("Jaina india private limtied")
        self.AddCust.click_tax_checkbox()
        time.sleep(5)
        self.AddCust.setNewsLetter("Your store name")
        self.AddCust.setCustomerRoles("Vendor")
        self.AddCust.setManagerofVendor("Vendor 1")
        self.AddCust.addAdminComment("Please check all okay")
        self.AddCust.click_save()
        self.logger.info("****** Customer information created **********")
        self.logger.info("****** Add Custoomer validation stated *******")
        self.msg=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***** Add customer Test passed ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.info(" ****** Add Custoomer Test Failed *****")
            assert True == False


    def generate_user_id(self):
            unique_id = uuid.uuid4()  # Generate a random UUID
            return f"user_{unique_id}"

    # def generate_user_id1(self):
    #     timestamp = int(time.time())  # Get the current timestamp
    #     random_number = random.randint(1000, 9999)  # Generate a random number
    #     user_id = f"user_{timestamp}_{random_number}"
    #     return user_id


    #
    # def random_generator(size=8,chars=string.ascii_lowercase + string.digits)
    #     return ''.join(random.choice(chars) for x in range(size))






