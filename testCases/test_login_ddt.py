import time

import pytest
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
from utilites import XLUtils



@pytest.mark.usefixtures("setup")
class Test_02_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    filepath = ".//TestData//Testdatas.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self):
        self.logger.info("**********Test_02_DDT_Test********")
        self.logger.info('*** verifying login test****')

        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.filepath,"Sheet1")
        print("Number of Rows  in excel sheet" , self.rows)
        st1_status=[] #Empty variable
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.filepath,"Sheet1", r, 1)
            self.password = XLUtils.readData(self.filepath,"Sheet1", r, 2)
            self.exp = XLUtils.readData(self.filepath,"Sheet1", r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Loging passed****")
                    self.lp.clickLogout()
                    st1_status.append("Pass")
                    XLUtils.writeData(self.filepath,'Sheet1',r,4,"Pass")
                    XLUtils.fillGreen(self.filepath,"Sheet1",r,4)


                elif self.exp=="Fail":
                    self.logger.info("******Failed******")
                    self.lp.clickLogout()
                    st1_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Fail***")
                    st1_status.append("Fail")


                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    st1_status.append("Pass")
                    XLUtils.writeData(self.filepath, 'Sheet1', r, 4, "Fail")
                    XLUtils.fillRed(self.filepath, "Sheet1", r, 4)
                    time.sleep(5)
            if "Fail" not in st1_status:
                self.logger.info("Loging DDT test Passed")
                assert True
            else:
                self.logger.info("**** Loging DDT test Failed")

                assert False
        self.logger.info("*** End of Loging DDT Test****")
        self.logger.info("************ Completed TC_Loging DDT_02 ******")














