import os
import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException

# Cấu hình
URL = "https://meinvoice.vn/tra-cuu"  # Đường dẫn tới trang tra cứu hóa đơn
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Thư mục chứa file script hiện tại
DOWNLOAD_DIR = os.path.join(SCRIPT_DIR, "misa")  # Thư mục lưu file PDF tải về
LOG_FILE = os.path.join(SCRIPT_DIR, "logs.txt")  # File lưu nhật ký hoạt động
INPUT_FILE = os.path.join(SCRIPT_DIR, "matracuu.txt")  # File chứa danh sách mã tra cứu
WAIT_TIME = 15  # Thời gian chờ tối đa (giây) cho các thao tác Selenium

# Hàm đọc danh sách mã tra cứu từ file
def read_ma_tra_cuu():
    """
    Đọc danh sách mã tra cứu từ file .txt hoặc .xlsx
    Returns:
        List chứa các mã tra cứu
    Raises:
        Exception nếu file không đúng định dạng
    """
    if INPUT_FILE.endswith(".txt"):
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]  # Loại bỏ dòng trống
    elif INPUT_FILE.endswith(".xlsx"):
        df = pd.read_excel(INPUT_FILE)
        return df.iloc[:, 0].dropna().astype(str).tolist()  # Lấy cột đầu tiên, bỏ giá trị NaN
    else:
        raise Exception("Chỉ đọc file .txt hoặc .xlsx")

# Hàm ghi log vào file và in ra màn hình
def write_log(message):
    """
    Ghi thông báo vào file log với thời gian và in ra console
    Args:
        message: Nội dung thông báo
    """
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Lấy thời gian hiện tại
        f.write(f"[{timestamp}] {message}\n")  # Ghi log với định dạng [thời gian] nội dung
    print(message)

# Hàm thiết lập trình duyệt Chrome
def setup_driver():
    """
    Thiết lập trình duyệt Chrome với các tùy chọn như thư mục tải xuống và mở toàn màn hình
    Returns:
        Đối tượng webdriver đã được cấu hình
    """
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)  # Tạo thư mục tải xuống nếu chưa tồn tại
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,  # Thiết lập thư mục tải xuống
        "download.prompt_for_download": False,  # Tắt hộp thoại hỏi nơi lưu file
        "download.directory_upgrade": True,  # Cho phép ghi đè thư mục tải xuống
        "plugins.always_open_pdf_externally": True  # Tự động tải PDF thay vì mở trong trình duyệt
    })
    options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ toàn màn hình
    return webdriver.Chrome(options=options)

# Hàm kiểm tra xem trang web đã tải xong chưa
def check_website_loaded(driver):
    """
    Kiểm tra xem trang web đã tải thành công bằng cách tìm ô nhập mã tra cứu
    Args:
        driver: Đối tượng webdriver
    Returns:
        True nếu trang tải thành công, False nếu không
    """
    try:
        WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, "txtCode"))  # Đợi ô nhập mã xuất hiện
        )
        return True
    except TimeoutException:
        write_log("Không thể tải trang meinvoice.vn - Kiểm tra kết nối internet.")
        return False

# Hàm tra cứu hóa đơn
def tra_cuu_hoa_don(driver, ma_tra_cuu):
    """
    Thực hiện tra cứu hóa đơn với mã tra cứu và tải PDF nếu có
    Args:
        driver: Đối tượng webdriver
        ma_tra_cuu: Mã tra cứu hóa đơn
    """
    try:
        driver.get(URL)  # Mở trang tra cứu
        if not check_website_loaded(driver):
            write_log(f"Mã '{ma_tra_cuu}': Không tải được trang.")
            return
        wait = WebDriverWait(driver, WAIT_TIME)  # Thiết lập thời gian chờ

        # Nhập mã tra cứu vào ô tìm kiếm
        input_box = wait.until(EC.presence_of_element_located((By.ID, "txtCode")))
        input_box.clear()  # Xóa nội dung ô nhập
        input_box.send_keys(ma_tra_cuu)  # Nhập mã tra cứu

        # Nhấn nút tra cứu
        search_btn = driver.find_element(By.ID, "btnSearchInvoice")
        search_btn.click()

        # Đợi kết quả hoặc thông báo lỗi
        try:
            wait.until(EC.presence_of_element_located((By.ID, "showPopupInvoice")))  # Đợi popup kết quả
            write_log(f"Mã '{ma_tra_cuu}': Tìm thấy hóa đơn.")

            # Click nút "Tải hóa đơn"
            try:
                btn_open_download = wait.until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "download-invoice"))  # Đợi nút tải
                )
                driver.execute_script("arguments[0].click();", btn_open_download)  # Click bằng JavaScript

                # Đợi menu tải PDF và click
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "txt-download-pdf")))
                pdf_btn = driver.find_element(By.CLASS_NAME, "txt-download-pdf")
                pdf_btn.click()
                time.sleep(3)  # Đợi 3 giây để file PDF tải xuống
                write_log(f"Mã '{ma_tra_cuu}': Đã tải hóa đơn PDF.")
            except Exception as e:
                write_log(f"Mã '{ma_tra_cuu}': Không thể tải PDF: {str(e)}")
        except TimeoutException:
            write_log(f"Mã '{ma_tra_cuu}': Không tìm thấy hóa đơn.")
    except Exception as e:
        write_log(f"Mã '{ma_tra_cuu}': Lỗi khi tra cứu: {str(e)}")

# Hàm chính điều khiển luồng chương trình
def main():
    """
    Hàm chính: Đọc danh sách mã tra cứu, thực hiện tra cứu và tải PDF
    """
    try:
        ma_tra_cuu_list = read_ma_tra_cuu()  # Đọc danh sách mã tra cứu
        driver = setup_driver()  # Khởi tạo trình duyệt
        for ma in ma_tra_cuu_list:
            tra_cuu_hoa_don(driver, ma)  # Tra cứu từng mã
            time.sleep(2)  # Đợi 2 giây giữa các lần tra cứu
        driver.quit()  # Đóng trình duyệt
        write_log("Hoàn tất quá trình tra cứu.")
    except Exception as e:
        write_log(f"Lỗi tổng quát: {str(e)}")

if __name__ == "__main__":
    main()