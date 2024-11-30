import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    # Khởi tạo trình điều khiển Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def add_item_to_card(driver):  
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)  
    
    # cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    # assert cart_badge == "1"  # Kiểm tra số lượng sản phẩm trong giỏ hàng là 1

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_name == "Sauce Labs Backpack"  
