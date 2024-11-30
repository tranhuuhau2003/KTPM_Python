import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestTreeShopAddToCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Thiết lập trình duyệt (Chrome)
        cls.driver = webdriver.Chrome()  # Cập nhật đường dẫn tới ChromeDriver
        cls.driver.get("https://www.tree-shop.co.uk/")  # Mở trang chính của web

    def test_add_to_cart(self):
        product_name = "aspen"  # Thay thế bằng tên sản phẩm cụ thể bạn muốn thử nghiệm
        
        # Tìm kiếm sản phẩm
        search_box = self.driver.find_element(By.NAME, "s")  # Giả sử trường tìm kiếm có name là 's'
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

        # Chờ một chút để kết quả tải
        time.sleep(2)

        # Nhấn vào sản phẩm đầu tiên trong kết quả
        first_product = self.driver.find_element(By.CSS_SELECTOR, ".product a")  # Giả sử sản phẩm có class là 'product'
        first_product.click()

        # Chờ để trang sản phẩm tải
        time.sleep(2)

        # Nhấn nút "Add to Cart"
        add_to_cart_button = self.driver.find_element(By.NAME, "variation_id")  # Cập nhật tên thực tế của nút
        add_to_cart_button.click()

        # Chờ để giỏ hàng cập nhật
        time.sleep(2)

        view_basket_button = self.driver.find_element(By.ID, "basket") 
        view_basket_button.click()
        time.sleep(5)
            
        # # Kiểm tra thông báo giỏ hàng đã cập nhật
        cart_message = self.driver.find_element(By.CSS_SELECTOR, "woocommerce-message")  # Giả sử thông báo có class là 'woocommerce-message'
        self.assertIn("đã được thêm vào giỏ hàng", cart_message.text, "Sản phẩm không được thêm vào giỏ hàng.")
         
    def test_scroll_and_add_to_cart(self):     
        # Đợi cho trang tải
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".category-item"))
        )

        # Bước 2: Cuộn xuống để hiển thị danh mục
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Bước 3: Chọn danh mục đầu tiên
        first_category = self.driver.find_element(By.CSS_SELECTOR, ".category-item")  # Chọn selector phù hợp với danh mục
        first_category.click()
        
        # Bước 4: Đợi cho trang sản phẩm tải
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item"))
        )

        # Bước 5: Chọn sản phẩm đầu tiên trong danh mục
        first_product = self.driver.find_element(By.CSS_SELECTOR, ".product-item")
        first_product.click()
        
        # Bước 6: Thêm sản phẩm vào giỏ hàng
        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart-button")
        add_to_cart_button.click()
        
        # Bước 7: Mở giỏ hàng
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, ".cart-icon")
        cart_icon.click()

        # Bước 8: Đợi và kiểm tra giỏ hàng
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Giỏ hàng")  # Kiểm tra xem tiêu đề có chứa "Giỏ hàng" hay không
        )
        self.assertIn("Giỏ hàng", self.driver.title, "Giỏ hàng không mở đúng cách.")

    @classmethod
    def tearDownClass(cls):
        # Đóng trình duyệt
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
