from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Danh sách tài khoản
usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'
url = "https://www.saucedemo.com"

# Khởi tạo driver
driver = webdriver.Chrome()

product_data = []

for username in usernames:
    driver.get(url)
    time.sleep(2)
    
    # Điền username và password
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    # Nếu login thành công
    if "inventory.html" in driver.current_url:
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for p in products:
            name = p.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = p.find_element(By.CLASS_NAME, "inventory_item_price").text
            product_data.append({'username': username, 'product': name, 'price': price})
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)

driver.quit()

# Ghi ra Excel
df = pd.DataFrame(product_data)
df.to_excel("saucedemo_products.xlsx", index=False)
