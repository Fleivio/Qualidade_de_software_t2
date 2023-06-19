import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
    rButton = driver.find_element(By.XPATH, "//*[@id=\"mainslider1\"]/div[2]/div/span[2]/a")
    img = driver.find_element(By.XPATH, "//*[@id=\"mainslider1\"]/div[3]/div[1]/ul")

    style1 = img.get_attribute("style")
    rButton.click()
    sleep(2)

    style2 = img.get_attribute("style")
    assert style1 != style2

@pytest.mark.test
def test_header_button(setup):
    driver = setup
    button = driver.find_element(By.XPATH, "//html/body/header/div/div[3]/div/div/nav/ul/li[1]/a")
    dropDown = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/div")
    sleep(2)
    button.click()
    sleep(2)

    hidden = dropDown.get_attribute("aria-hidden")

    assert hidden == "false"


@pytest.mark.test
def test_header_button_link(setup):
    driver = setup
    button = driver.find_element(By.XPATH, "//html/body/header/div/div[3]/div/div/nav/ul/li[1]/a")
    button.click()
    sleep(2)

    buttonLink = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/div/ul/li[3]/ul/li[1]/a")
    buttonLink.click()

    sleep(2)
    title = driver.title
    assert title in "Rektor"

@pytest.mark.test
def test_links_span(setup):
    driver = setup

    element = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[2]/p")
    element.click()

    childs =  driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[2]/p/div")

    assert childs.is_displayed()

@pytest.mark.test
def test_dropdown_footer(setup):
    driver = setup
    sleep(2)
    button = driver.find_element(By.XPATH, "//*[@id=\"footertrigger\"]")
    button.click()
    sleep(2)

    dropdown = driver.find_element(By.XPATH, "//*[@id=\"footerbox\"]")
    assert dropdown.is_displayed()

@pytest.mark.test
def test_to_top(setup):
    driver = setup

    defScrl = driver.execute_script("return document.body.scrollHeight")

    html = driver.find_element(By.XPATH, "/html")
    html.send_keys(Keys.END)

    sleep(2)
    
    toTopButton = driver.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div/div[2]/a")
    toTopButton.click()
    sleep(2)
    assert driver.execute_script("return document.body.scrollHeight") == defScrl
