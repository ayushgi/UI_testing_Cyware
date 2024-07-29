# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl = "https://artoftesting.com/samplesiteforselenium"


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Correctly set up the ChromeDriver with the Service class
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    request.cls.driver = driver
    yield driver
    driver.quit()
