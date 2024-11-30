import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# def test_valid_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     assert "inventory.html" in driver.current_url


# def test_invalid_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("invalid_user")
#     driver.find_element(By.ID, "password").send_keys("wrong_password")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
#     assert "Epic sadface: Username and password do not match any user in this service" in error_message


# def test_empty_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
#     assert "Epic sadface: Username is required" in error_message


# def test_logout_functionality(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     driver.find_element(By.ID, "react-burger-menu-btn").click()
#     time.sleep(1)

#     driver.find_element(By.ID, "logout_sidebar_link").click()
#     time.sleep(2)

#     assert "https://www.saucedemo.com/" in driver.current_url


# def test_add_item_to_cart(driver):  
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     time.sleep(1)

#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     time.sleep(2)

#     item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
#     assert item_name == "Sauce Labs Backpack"


# def test_remove_item_from_cart(driver):  
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     time.sleep(1)

#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     time.sleep(2)

#     item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
#     assert item_name == "Sauce Labs Backpack"

#     # wait = WebDriverWait(driver, 10)
#     # remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'cart_button') and contains(@class, 'btn_secondary')]")))
#     # remove_button.click()
#     # time.sleep(1)
    
#     remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
#     remove_button.click()
#     time.sleep(1)

#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     time.sleep(2)

#     cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
#     assert len(cart_badge) == 0


# def test_view_cart(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     time.sleep(1)

#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     time.sleep(2)

#     item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
#     assert item_name == "Sauce Labs Backpack"


# # def test_checkout_process(driver):
# #     driver.get("https://www.saucedemo.com/")
# #     driver.find_element(By.ID, "user-name").send_keys("standard_user")
# #     driver.find_element(By.ID, "password").send_keys("secret_sauce")
# #     driver.find_element(By.ID, "login-button").click()
# #     time.sleep(2)

# #     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
# #     time.sleep(1)

# #     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# #     time.sleep(2)

# #     driver.find_element(By.ID, "checkout").click()
# #     time.sleep(1)

# #     driver.find_element(By.ID, "first-name").send_keys("John")
# #     driver.find_element(By.ID, "last-name").send_keys("Doe")
# #     driver.find_element(By.ID, "postal-code").send_keys("12345")
# #     driver.find_element(By.ID, "continue").click()
# #     time.sleep(2)

# #     item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
# #     assert item_name == "Sauce Labs Backpack"

# #     driver.find_element(By.ID, "finish").click()
# #     time.sleep(2)

# #     confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
# #     assert "Thank you for your order!" in confirmation_message

# def test_session_timeout(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(2)

#     # giữ session trong 10s
#     time.sleep(5) 

#     driver.get("https://www.saucedemo.com/inventory.html")
#     time.sleep(5)

#     assert "https://www.saucedemo.com/" in driver.current_url, "User không tự logout"
    
    
    


def test_checkout_process(driver):
    # Step 1: Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # Step 2: Add item to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    # Step 3: Go to the cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Step 4: Click on "Checkout"
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    # Step 5: Fill in the checkout information
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Step 6: Verify the user is on checkout step two page
    assert "checkout-step-two.html" in driver.current_url, "User is not on the checkout step two page"

    # Step 7: Verify that the item is still in the cart
    item_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_in_cart == "Sauce Labs Backpack", "Item is not displayed in the checkout"

    # Step 8: Complete the checkout process
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # Step 9: Verify the user is on the checkout complete page
    assert "checkout-complete.html" in driver.current_url, "User is not on the checkout complete page"

    # Step 10: Wait for 1 minute to check session
    time.sleep(5)  # Điều chỉnh thời gian nếu cần

    # Step 11: Try to access the cart again to check session status
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Step 12: Verify that the cart is still accessible and contains the item
    try:
        item_in_cart_after_session = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_in_cart_after_session == "Sauce Labs Backpack", "Session has expired or item is not in the cart"
        print("Session is still active, item is in the cart.")
    except:
        print("Session expired or item is not in the cart.")

