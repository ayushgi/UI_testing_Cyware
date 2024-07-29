# THIS IS FILE IS FOR WRITING CODE TO TAKE INPUT,ALERT,TEXTBOX,DROPDOWN,RADIO BUTTON,CLICK BUTTON


from datetime import datetime
from pathlib import Path
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver


# Test case 1: To click on a link
    def webelement_Click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

# Test case 2: To Hover on Button
    def webelement_Hover(self,locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

# Test case 3: To Double click on Button
    def webelement_doubleclick(self,locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.double_click(element).perform()

# Test case 4: To accept the Ok popups from the top
    def webelement_switchtoalertok(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()



# Test case 5: Radio Button

    def webelement_radiomale(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()


    def webelement_radiofemale(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

# Test case - 7 To select Drop down based on value,index,id
    def webelement_dropdown(self,locator):
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        sel = Select(dropdown_element)
        sel.select_by_value('Performance')
# Test case - 8 To generate alert
    def webelement_generatealert(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def webelement_switchtoalertokforgenerate(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
# Test case - 9 confirm btn
    def webelement_cnfbtn(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def webelement_switchtoalertokforcnf(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
