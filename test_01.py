import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://www.uni-koeln.de/')
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.mark.test
def test_title(setup):
    driver = setup
    title = driver.title
    assert "Universität zu Köln" == title

@pytest.mark.test
def test_swap(setup):
    driver = setup

    rButton = driver.find_element(By.XPATH, "//*[@id=\"mainslider1\"]/div[2]/div/span[2]/a")
    style1 = rButton.get_attribute("class")
    rButton.click()
    sleep(2)

    style2 = rButton.get_attribute("class")
    assert style1 != style2


@pytest.mark.test
def test_header_button(setup):
    driver = setup
    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/a")))
    dropDown = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/div")))
    sleep(2)
    button.click()
    sleep(2)

    assert dropDown.is_displayed()


@pytest.mark.test
def test_header_button_link(setup):
    driver = setup
    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//html/body/header/div/div[3]/div/div/nav/ul/li[1]/a")))
    button.click()
    sleep(2)

    buttonLink = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[3]/div/div/nav/ul/li[1]/div/ul/li[3]/ul/li[1]/a")))
    buttonLink.click()

    sleep(2)
    title = driver.title
    assert title in "Rektor"


@pytest.mark.test
def test_links_span(setup):
    driver = setup

    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[2]/p")))
    element.click()

    childs =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[2]/p/div")))
    sleep(2)
    assert childs.is_displayed()

@pytest.mark.test
def test_dropdown_footer(setup):
    driver = setup

    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"footertrigger\"]")))
    button.click()
    sleep(2)

    dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"footerbox\"]")))
    assert dropdown.is_displayed()

@pytest.mark.test
def test_to_top(setup):
    driver = setup

    defScrl = driver.execute_script("return document.body.scrollHeight")

    html = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html")))
    html.send_keys(Keys.END)

    sleep(2)
    
    toTopButton = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[1]/div/div/div[2]/a")))
    toTopButton.click()
    sleep(7)
    assert driver.execute_script("return document.body.scrollHeight") == defScrl

@pytest.mark.test
def test_search(setup):
    driver = setup

    search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/form[3]/input[1]")))
    search.send_keys("test")
    search.send_keys(Keys.ENTER)
    sleep(2)

    assert driver.title == "Google-Suche"

@pytest.mark.test
def test_language_switch(setup):
    driver = setup

    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[2]/div/div/nav/div/form/p/span/select")))
    button.click()
    sleep(2)

    dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[2]/div/div/nav/div/form/p/div")))
    dropdown.click()
    sleep(2)

    lang = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html"))).get_attribute("lang")

    assert lang == "en-US"

@pytest.mark.test
def test_hover(setup):
    driver = setup

    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/article[2]/a")))
    hover = ActionChains(driver).move_to_element(button)
    hover.perform()
    sleep(2)

    assert button.value_of_css_property("background-color") == "rgba(50, 71, 91, 1)"


@pytest.mark.test
def test_image_alt(setup):
    driver = setup

    img = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/article[2]/a/figure/img")))
    alt = img.get_attribute("alt")

    assert alt == "Gebäude aus der Vogelperspektive"

@pytest.mark.test
def test_pagination(setup):
    driver = setup

    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/div[12]/span/a")))
    link.click()
    sleep(2)
    link_4 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/div[8]/div/section/ul[1]/li[4]/a")))
    link_4.click()
    sleep(2)
    link_4_father = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/div[8]/div/section/ul[1]/li[5]")))

    assert "current" in link_4_father.get_attribute("class")

@pytest.mark.test
def test_checkbox(setup):
    driver = setup
    
    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")))
    link.click()
    sleep(3)
    link_drop = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend")))
    link_drop.click()
    sleep(3)
    link_checkbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/div/div[1]/input")))
    link_checkbox.click()
    sleep(2)

    assert link_checkbox.get_attribute("checked") 

@pytest.mark.test
def test_checked_count(setup):
    driver = setup

    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")))
    link.click()

    link_drop = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend")))
    sleep(1)
    link_drop.click()

    link_checkbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/div/div[1]/input")))
    sleep(1)
    link_checkbox.click()

    box_count = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend/span")))
    assert box_count.text == "1"


@pytest.mark.test
def test_checked_c(setup):
    driver = setup

    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")))
    sleep(1)
    link.click()

    link_drop = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend")))
    link_drop.click()
    sleep(2)
    link_checkbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/div/div[1]/input")))
    link_checkbox.click()
    sleep(2)
    box_count = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[2]/div[3]/div/fieldset/legend/span")))
    assert box_count.text == "1"

@pytest.mark.test
def test_first_letter_selection(setup):
    driver = setup

    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")))
    link.click()
    sleep(2)
    link_letter = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/aside/div[2]/div[5]/div/form[1]/div/nav/ul/li[1]/a")))
    link_letter.click()
    sleep(10)
    first_course = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/div[1]/div[5]/div/ul/li/article/a/h2/em")))
    assert first_course.text[0] == "A"