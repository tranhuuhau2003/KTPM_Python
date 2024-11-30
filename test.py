from selenium import webdriver

try:
    # Khởi tạo trình điều khiển Chrome (không cần chỉ định đường dẫn nếu đã thêm vào PATH)
    driver = webdriver.Chrome()

    # Mở trang Google để kiểm tra
    driver.get("https://www.google.com")

    # In ra thông báo nếu thành công
    print("ChromeDriver đã được thêm vào PATH thành công.")

    # Đóng trình duyệt
    driver.quit()

except Exception as e:
    # In ra lỗi nếu không thể tìm thấy ChromeDriver
    print("Lỗi: ChromeDriver chưa được thêm vào PATH.")
    print(e)
