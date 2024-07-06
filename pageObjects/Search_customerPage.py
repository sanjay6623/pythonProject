from selenium.webdriver.common.by import By



class SearchCustomer:

    #Add search customer page
    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_customer_id="search-customers"
    table_xpath="//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']//tbody//tr"
    tableColumns_email_xpath="//table[@id='customers-grid']//tbody//tr//td[2]"

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)


    def setEmail(self,Email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(Email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).clear()
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fname)

    def lastName(self,lastName):
        self.driver.find_element(By.ID,self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).click()

    def clickSearch_btn(self):
        self.driver.find_element(By.ID,self.btnSearch_customer_id).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_rows_xpath))
    def getNoOfColumns(self):
        return len (self.driver.find_elements(By.XPATH,self.tableColumns_email_xpath))


    def searchContactByEmail(self,email):

        self.all_Columns = self.driver.find_elements(By.XPATH,self.tableColumns_email_xpath)
        for rows in self.all_Columns:
            if rows.text == email:


                print(rows.text)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchCustomer_email.png")
                break



        else:

            print("Search Result Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchCustomer_email_error.png")


    def searchByName(self,name):

        self.all_rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody//tr//td[3]")
        for rows in self.all_rows:
            if rows.text == name:

                print(rows.text)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchCustomer_name.png")
                break


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Error_SearchCustomer.png")
            print("Search Result Not Found")









