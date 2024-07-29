from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SamplePage(BasePage):
    link_element = (
    By.XPATH, "//a[text()='This is a link' and @href=\"http://www.artoftesting.com/sampleSiteForSelenium.html\"]")
    input_element = (By.ID, "fname")
    hover_element = (By.ID, "idOfButton")
    alert_element = (By.ID,"dblClkBtn")
    radiomale_element = (By.XPATH,"//input[@value='male']")
    radiofemale_element = (By.XPATH, "//input[@value='female']")
    dropdown_element = (By.ID, "testingDropdown")
    generatealert_element=(By.XPATH,"//button[text()='Generate Alert Box']")
    conf_button = (By.XPATH,"//button[text()='Generate Confirm Box']")





    def __init__(self, driver):
        super().__init__(driver)

    def linktemp(self):
        self.webelement_Click(self.link_element)
        # self.webelement_Click(self.hover_element)

    def textinput(self):
        input_element = self.driver.find_element(By.ID, "fname").send_keys("ayushtemp")

    def hovertemp(self):
        self.webelement_Hover(self.hover_element)

    def doubleclick(self):
        self.webelement_doubleclick(self.alert_element)
    def acceptalert(self):
        self.webelement_switchtoalertok()

    def radiomale(self):
        self.webelement_radiomale(self.radiomale_element)

    def radiofemale(self):
        self.webelement_radiofemale(self.radiofemale_element)


# Test case:-6 To select checkboxes
    def checkbox(self):
        li = (By.XPATH, "//input[@type='checkbox']")
        # using locator bcz its a list so we need to get each element
        li = self.driver.find_elements(*li)
        for temp in li:
            val = temp.get_attribute('value')
            if val == 'Automation':
                temp.click()
# We can use else statement as well
            elif val=='Performance':
                temp.click()


    def dropdown(self):
        self.webelement_dropdown(self.dropdown_element)

    def generatealert(self):
        self.webelement_generatealert(self.generatealert_element)


    def cnf(self):
        self.webelement_cnfbtn(self.conf_button)


    def acceptgeneratealert(self):
        self.webelement_switchtoalertokforgenerate()

    def acceptcnf(self):
        self.webelement_switchtoalertokforcnf()





