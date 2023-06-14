import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://www.uni-koeln.de/')
    yield driver
    driver.close()

@pytest.mark.test
def test_title(setup):
    driver = setup
    title = driver.title
    assert "Universität zu Köln" in title

@pytest.mark.test
def test_swap(setup):
    driver = setup
    sleep(2)
    lButton = driver.find_element(By.XPATH, "//a[contains (@class, 'bx-prev uzk15__iconlink')]")
    img = driver.find_element(By.XPATH, "//*[@id=\"mainslider1\"]/div[3]/div[1]/ul")
    style1 = img.get_attribute("style")
    lButton.click()
    sleep(2)
    style2 = img.get_attribute("style")
    print(style1)
    print(style2)
    assert style1 != style2
