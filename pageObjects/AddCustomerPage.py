import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    # Add Customer page

    link_csutomer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_csutomer_menu_item_xpath="//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txt_email_xpath="//input[@id='Email']"
    txt_pass_xpath="//input[@id='Password']"
    txt_first_name_xpath = "//input[@id='FirstName']"
    txt_last_name_xpath = "//input[@id='LastName']"
    btn_gender_male_xpath = "//input[@id='Gender_Male']"
    btn_gender_female_xpath = "//input[@id='Gender_Female']"
    date_of_birth_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    checkbox_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    txt_newsletter_xpath = "//span[@data-select2-id='4']"
    list_item_newsletter_yourStoreName_xpath = "//li[@id='select2-SelectedNewsletterSubscriptionStoreIds-result-kx7y-1']"
    list_item_newsletter_Teststore2_xpath = "//li[@id='select2-SelectedNewsletterSubscriptionStoreIds-result-zii4-2']"
    txt_customerRoles_xpath="//div[@class='input-group-append input-group-required']"
    list_item_Administrtors_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-1n5o-1']"
    list_item_ForumModeratores_xpath ="//li[@id='select2-SelectedCustomerRoleIds-result-1n5o-2']"
    list_item_Registered_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-tbne-3']"
    list_item_Guests_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-8vhv-4']"
    list_item_Vendors_xpath ="//li[@id='select2-SelectedCustomerRoleIds-result-7daz-5']"
    dr_manage_ofVendor_xpath="//select[@id='VendorId']"
    txt_Admin_comment_xpath="//textarea[@id='AdminComment']"
    btn_save_xpath="//button[@name='save']"



    def __init__(self,driver):
        self.driver = driver


    def clickOnCustomerMenu(self):

        self.driver.find_element(By.XPATH, self.link_csutomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.link_csutomer_menu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def sefPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_pass_xpath).send_keys(password)

    def sefFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_first_name_xpath).send_keys(firstname)

    def sefLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_last_name_xpath).send_keys(lastname)

    def clickOnGender(self,gender):
        if gender=='Male':

            self.driver.find_element(By.XPATH,self.btn_gender_male_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.btn_gender_female_xpath).click()
        else:
            print("Please fill proper gender details")

    def clickOnDateBirth(self,dateofbirth):
        self.driver.find_element(By.XPATH,self.date_of_birth_xpath).send_keys(dateofbirth)

    def setCompneyName(self,companeyName):
        self.driver.find_element(By.XPATH,self.txt_company_name_xpath).send_keys(companeyName)

    def click_tax_checkbox(self):
        self.driver.find_element(By.XPATH,self.checkbox_tax_exempt_xpath).click()
        time.sleep(4)

    def setNewsLetter(self,letter):
        self.driver.find_element(By.CSS_SELECTOR, ".select2-selection").click()
        dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-results__options")))

        options = dropdown.find_elements(By.XPATH, "//ul[@class='select2-results__options']/li")

        for option in options:
            if option.text.strip() ==letter:
                option.click()

                break
        else:
            print("Provide correct newsletter details")


    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, "//div[@class='input-group-append input-group-required']").click()

        # self.driver.find_element(By.CSS_SELECTOR, "li[title='Registered'] span[role='presentation']").click()
        # time.sleep(4)

        role_dropdown = self.driver.find_element(By.XPATH, "//div[@class='input-group-append input-group-required']")
        role_dropdown.click()
        time.sleep(3)

        role_options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".select2-results li")))

        self.role_found = False
        for option in role_options:
            if option.text.strip() == role:
                option.click()
                self.role_found = True
                break

        else:
            print("Provide correct role")


    def setManagerofVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.dr_manage_ofVendor_xpath))
        drp.select_by_visible_text(value)

    def addAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txt_Admin_comment_xpath).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()














