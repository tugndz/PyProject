from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep")
time.sleep(5)

# Ghi ra nhiều sheet Excel:
with pd.ExcelWriter("mst_doanhnghiep.xlsx") as writer:
    for i in range(1, 6):  # ví dụ lặp 5 trang
        # Tạo dataframe giả để demo
        df = pd.DataFrame({
            'Tên doanh nghiệp': [f'DN {i}-1', f'DN {i}-2'],
            'Mã số thuế': [f'12345{i}', f'67890{i}'],
            'Ngày cấp': ['01/01/2021', '05/05/2022']
        })
        df.to_excel(writer, sheet_name=f'Trang_{i}', index=False)

driver.quit()
