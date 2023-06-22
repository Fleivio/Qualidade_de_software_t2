import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

delay = 3

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://www.uni-koeln.de/')
    yield driver
    driver.close()

# @pytest.mark.test
# def test_title(setup):
#     driver = setup
#     title = driver.title
#     assert "Universität zu Köln" == title

# @pytest.mark.test
# def test_swap(setup):
#     driver = setup
#     sleep(2)

#     try:
#         present = EC.presence_of_element_located((By.XPATH, "//*[@id=\"mainslider1\"]/div[2]/div/span[2]/a"))
#         WebDriverWait(driver, delay).until(present)
#     except TimeoutException:
#         print("Loading took too long")

#     rButton = driver.find_element(By.XPATH, "//*[@id=\"mainslider1\"]/div[2]/div/span[2]/a")
#     img = driver.find_element(By.XPATH, "//*[@id=\"mainslider1\"]/div[3]/div[1]/ul")

#     style1 = img.get_attribute("style")
#     rButton.click()
#     sleep(2)

#     style2 = img.get_attribute("style")
#     assert style1 != style2

# @pytest.mark.test
# def test_header_button(setup):
#     driver = setup
#     button = driver.find_element(By.XPATH, "//html/body/header/div/div[3]/div/div/nav/ul/li[1]/a")
#     dropDown = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/div")
#     sleep(2)
#     button.click()
#     sleep(2)

#     hidden = dropDown.get_attribute("aria-hidden")

#     assert hidden == "false"


# @pytest.mark.test
# def test_header_button_link(setup):
#     driver = setup
#     button = driver.find_element(By.XPATH, "//html/body/header/div/div[3]/div/div/nav/ul/li[1]/a")
#     button.click()
#     sleep(2)

#     buttonLink = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/div/ul/li[3]/ul/li[1]/a")
#     buttonLink.click()

#     sleep(2)
#     title = driver.title
#     assert title in "Rektor"

# @pytest.mark.test
# def test_links_span(setup):
#     driver = setup

#     element = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[2]/p")
#     element.click()

#     childs =  driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[2]/p/div")

#     assert childs.is_displayed()

# @pytest.mark.test
# def test_dropdown_footer(setup):
#     driver = setup
#     sleep(2)
#     button = driver.find_element(By.XPATH, "//*[@id=\"footertrigger\"]")
#     button.click()
#     sleep(2)

#     dropdown = driver.find_element(By.XPATH, "//*[@id=\"footerbox\"]")
#     assert dropdown.is_displayed()

# @pytest.mark.test
# def test_to_top(setup):
#     driver = setup

#     defScrl = driver.execute_script("return document.body.scrollHeight")

#     html = driver.find_element(By.XPATH, "/html")
#     html.send_keys(Keys.END)

#     sleep(2)
    
#     toTopButton = driver.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div/div[2]/a")
#     toTopButton.click()
#     sleep(2)
#     assert driver.execute_script("return document.body.scrollHeight") == defScrl

# @pytest.mark.test
# def test_search(setup):
#     driver = setup
#     search = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[3]/input[1]")
#     search.send_keys("test")
#     search.send_keys(Keys.ENTER)
#     sleep(2)

#     assert driver.title == "Google-Suche"

# @pytest.mark.test
# def test_language_switch(setup):
#     driver = setup
#     button = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/nav/div/form/p/span/select")
#     button.click()
#     sleep(2)

#     dropdown = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/nav/div/form/p/div")
#     dropdown.click()
#     sleep(2)

#     lang = driver.find_element(By.XPATH, "/html").get_attribute("lang")

#     assert lang == "en-US"

# @pytest.mark.test
# def test_hover(setup):
#     driver = setup
#     button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/main/article[2]/a")
#     hover = ActionChains(driver).move_to_element(button)
#     hover.perform()
#     sleep(2)

#     assert button.value_of_css_property("background-color") == "rgba(50, 71, 91, 1)"


# @pytest.mark.test
# def test_image_alt(setup):
#     driver = setup
#     img = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/main/article[2]/a/figure/img")
#     alt = img.get_attribute("alt")

#     assert alt == "Grafik"

# @pytest.mark.test
# def test_pagination(setup):
#     driver = setup
#     link = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/main/div[12]/span/a")
#     link.click()
#     sleep(2)
#     link_4 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/main/div[8]/div/section/ul[1]/li[4]/a")
#     link_4.click()
#     sleep(2)
#     link_4_father = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/main/div[8]/div/section/ul[1]/li[5]")

#     assert "current" in link_4_father.get_attribute("class")

@pytest.mark.test
def test_checkbox(setup):
    driver = setup

    try:
        present = EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a"))
        WebDriverWait(driver, delay).until(present)
    except TimeoutException:
        print("Loading took too long")
    
    link = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")
    link.click()
    sleep(2)
    link_drop = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend")
    link_drop.click()
    sleep(2)
    link_checkbox = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/div/div[1]/input")
    link_checkbox.click()
    sleep(2)

    assert link_checkbox.get_attribute("checked") 

# @pytest.mark.test
# def test_checked_count(setup):
#     driver = setup
#     sleep(2)
#     link = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")
#     link.click()
#     sleep(2)
#     link_drop = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend")
#     link_drop.click()
#     sleep(2)
#     link_checkbox = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/div/div[1]/input")
#     link_checkbox.click()
#     sleep(2)
#     box_count = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend/span")
#     assert box_count.text == "1"

# @pytest.mark.test
# def test_first_letter_selection(setup):
#     driver = setup
#     sleep(2)
#     link = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")
#     link.click()
#     sleep(2)
#     link_letter = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[1]/div/nav/ul/li[1]/a")
#     link_letter.click()
#     sleep(10)
#     first_course = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/main/div[1]/div[5]/div/ul/li/article/a/h2/em")
#     assert first_course.text[0] == "A"