import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class TestTreeShopSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Thiết lập trình duyệt (Chrome)
        cls.driver = webdriver.Chrome()  # Cập nhật đường dẫn tới ChromeDriver
        cls.driver.get("https://www.tree-shop.co.uk/product-category/native-trees/")

    # def test_search_tree_shop(self):
    #     search_query = "apple"
        
    #     # Chờ một chút để trang tải hoàn toàn
    #     time.sleep(2)

    #     # Tìm kiếm phần tử tìm kiếm
    #     search_box = self.driver.find_element(By.NAME, "s")  # Giả sử trường tìm kiếm có name là 's'

    #     # Nhập từ khóa tìm kiếm
    #     search_box.send_keys(search_query)

    #     # Gửi tìm kiếm
    #     search_box.send_keys(Keys.RETURN)

    #     # Chờ một chút để kết quả tảiaaaaaaaaaaaaaaaaaaa
    #     time.sleep(2)

    #     # Kiểm tra kết quả
    #     results = self.driver.find_elements(By.CLASS_NAME, "product")  # Giả sử kết quả sản phẩm có class là 'product'
        
    #     self.assertTrue(results, f"Không tìm thấy kết quả cho '{search_query}'.")
        
    #     # Kiểm tra ít nhất một kết quả hợp lệ
    #     first_result_title = results[0].find_element(By.CLASS_NAME, "product-title").text  # Cập nhật theo class thực tế
    #     self.assertIn(search_query, first_result_title.lower(), f"Kết quả không chứa từ khóa '{search_query}'.")


    def test_add_random_products_to_cart(self):
        driver = self.driver
        
        # Đợi trang tải hoàn tất
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product")))

        # Lấy danh sách 20 sản phẩm
        products = driver.find_elements(By.CSS_SELECTOR, ".product")[:20]
        self.assertGreaterEqual(len(products), 1, "Không tìm thấy sản phẩm nào trên trang.")

        max_attempts = 10  # Giới hạn số lần thử
        attempts = 0  # Đếm số lần thử

        while len(products) < 5 and attempts < max_attempts:
            time.sleep(2)  # Chờ một chút trước khi lấy lại
            products = driver.find_elements(By.CSS_SELECTOR, ".product")[:20]
            attempts += 1  # Tăng số lần thử

        if len(products) < 5:
            print("Không đủ sản phẩm để chọn ngẫu nhiên.")
            return  # Dừng hàm nếu không đủ sản phẩm

        random_products = random.sample(products, min(5, len(products)))  # Chọn tối đa 5 sản phẩm

        for random_product in random_products:
            # Nhấn vào nút "View product" để xem chi tiết sản phẩm
            view_button = random_product.find_element(By.CSS_SELECTOR, ".button")
            view_button.click()

            # Đợi trang chi tiết sản phẩm tải xong
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "variation_id")))

            # Tìm và nhấn nút "Add to cart" trên trang chi tiết sản phẩm
            add_to_cart_button = driver.find_element(By.NAME, "variation_id")  # Đảm bảo selector đúng
            add_to_cart_button.click()

            # Đợi sản phẩm được thêm vào giỏ hàng
            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-success-message")))
            except TimeoutException:
                print("Không tìm thấy thông báo giỏ hàng sau khi thêm sản phẩm.")

            # Quay lại trang danh sách sản phẩm
            driver.back()

            # Đợi trang danh sách sản phẩm tải lại
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product")))

            # Lấy lại danh sách sản phẩm sau khi quay lại
            products = driver.find_elements(By.CSS_SELECTOR, ".product")[:20]

            # Chọn lại 5 sản phẩm ngẫu nhiên từ danh sách hiện tại
            attempts = 0  # Đặt lại số lần thử
            while len(products) < 5 and attempts < max_attempts:
                time.sleep(2)  # Chờ một chút trước khi lấy lại
                products = driver.find_elements(By.CSS_SELECTOR, ".product")[:20]
                attempts += 1  # Tăng số lần thử

            if len(products) < 5:
                print("Không đủ sản phẩm để chọn ngẫu nhiên sau khi quay lại.")
                return  # Dừng hàm nếu không đủ sản phẩm

            random_products = random.sample(products, min(5, len(products)))  # Chọn lại 5 sản phẩm ngẫu nhiên

        # Mở giỏ hàng sau khi đã thêm xong
        cart_button = driver.find_element(By.ID, "basket")  # Cập nhật selector cho nút giỏ hàng nếu cần
        cart_button.click()

        # Đợi trang giỏ hàng tải xong
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-items")))

        print("Giỏ hàng đã mở thành công!")

                
    @classmethod
    def tearDownClass(cls):
        # Đóng trình duyệt
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
