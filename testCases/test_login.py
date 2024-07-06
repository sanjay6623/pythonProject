import pytest
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen



@pytest.mark.usefixtures("setup")
class Test_01_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()



    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"

    @pytest.mark.regression
    def test_homePageTitle(self):
        self.logger.info('***************Test_01_Login***********')
        #self.driver=setup
        self.logger.info('*******Verifying Home Page Title*******')
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info('***Home page title test is passed*********')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"test_hopePageTitle.png")
            self.logger.error('*** Home page title test is failed****')
            #self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info('*** verifying login test****')
        #self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        ReadConfig.getUseremail()
        ReadConfig.getPassword()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info('*** Loging test is pass****')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error('***Login test fail****')
            #self.driver.close()
            assert False








