import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

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
    rButton = driver.find_element(By.XPATH, "//a[contains (@class, 'bx-prev uzk15__iconlink')]")
    rButton.click()
    assert 1 == 1
