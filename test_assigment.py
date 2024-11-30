from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, email, password):
    driver.get("https://demo.opencart.com")
    
    # Nhấp vào menu thả xuống "My Account"
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    )
    my_account.click()
    
    # Thêm thời gian chờ để đảm bảo menu đã mở
    time.sleep(1)

    # Tìm và nhấp vào liên kết "Login" trong menu thả xuống
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()

    # Nhập email và mật khẩu
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys(email)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    
    # Kiểm tra xem có đăng nhập thành công không
    return "account/account" in driver.current_url


def logout(driver):
    try:
        account_menu = driver.find_element(By.LINK_TEXT, "My Account")
        account_menu.click()
        logout_link = driver.find_element(By.LINK_TEXT, "Logout")
        logout_link.click()
        time.sleep(2)
        print("Đăng xuất thành công!")
    except:
        print("Không thể đăng xuất!")

def test_login_success():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    result = login(driver, "vkhlinh4@gmail.com", "041103")  # Nhập email và mật khẩu hợp lệ
    assert result == True, "Đăng nhập thành công thất bại"
    logout(driver)
    driver.quit()

def test_login_failure():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    result = login(driver, "invalid_email@example.com", "invalid_password")  # Nhập email và mật khẩu không hợp lệ
    assert result == False, "Kiểm tra đăng nhập thất bại không thành công"
    driver.quit()
