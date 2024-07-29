import pytest

from conftest import BaseUrl
from pages.SamplePage import SamplePage
import  time

@pytest.mark.usefixtures("browser")
class Test_login():

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.link_page = SamplePage(self.driver)
        self.inp_text = SamplePage(self.driver)
        self.hover_page = SamplePage(self.driver)
        self.double_click = SamplePage(self.driver)
        self.accept_click = SamplePage(self.driver)
        self.radio_male = SamplePage(self.driver)
        self.radio_female = SamplePage(self.driver)
        self.checkbox_item=SamplePage(self.driver)
        self.dropdowm_item = SamplePage(self.driver)
        self.generate_item = SamplePage(self.driver)
        self.cnfbtn = SamplePage(self.driver)
        self.acceptgenerate = SamplePage(self.driver)
        self.acceptcnf = SamplePage(self.driver)

    @pytest.mark.link
    def test_linktemp(self):
        self.link_page.linktemp()
        time.sleep(3)

    @pytest.mark.textinput
    def test_textinput(self):
        self.inp_text.textinput()
        time.sleep(3)

    @pytest.mark.hover
    def test_hovertemp(self):
        self.hover_page.hovertemp()
        time.sleep(3)

    @pytest.mark.doubleclick
    def test_doubleclick(self):
        self.double_click.doubleclick()
        time.sleep(3)

    @pytest.mark.alert
    def test_acceptalert(self):
        self.accept_click.acceptalert()
        time.sleep(3)

    @pytest.mark.radio
    def test_radiomale(self):
        self.radio_male.radiomale()
        time.sleep(3)

    @pytest.mark.radio
    def test_radiofemale(self):
        self.radio_female.radiofemale()
        time.sleep(3)

    @pytest.mark.checkbox
    def test_checkbox(self):
        self.checkbox_item.checkbox()
        time.sleep(3)

    @pytest.mark.dropdown
    def test_dropdown(self):
        self.dropdowm_item.dropdown()
        time.sleep(3)

    @pytest.mark.alert
    def test_generatealert(self):
        self.generate_item.generatealert()
        time.sleep(3)

    @pytest.mark.alert
    def test_acceptgeneratealert(self):
        self.acceptgenerate.acceptgeneratealert()
        time.sleep(3)

    @pytest.mark.confirmation
    def test_cnf(self):
        self.cnfbtn.cnf()
        time.sleep(3)

    @pytest.mark.confirmation
    def test_acceptcnf(self):
        self.acceptcnf.acceptcnf()
        time.sleep(3)

    def teardown_class(self):
        self.driver.quit()