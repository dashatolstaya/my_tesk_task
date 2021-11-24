import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua/"


def test_contact():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(10)
        browser.get(link)

        # Act
        browser.implicitly_wait(5)   
        product= browser.find_element_by_class_name("tile")
        product.click()

        browser.implicitly_wait(5) 
        button = browser.find_element_by_tag_name("app-buy-button")
        button.click()

        # Assert
        # Write your asserts here
        assert 1
    finally:
        time.sleep(10)
        browser.quit()