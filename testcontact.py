import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        product= browser.find_element_by_class_name("tile")
        product.click()
        
        head = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product__title")))
    
        button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME,"app-buy-button")))
        button.click()

        basket_head = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart-product__title")))

        # Assert
        assert head.text == basket_head.text, "Product present in the basket"
        
    finally:
        time.sleep(5)
        browser.quit()