import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# STEP 1: Collect proxy list
driver = webdriver.Chrome()
driver.get('https://free-proxy-list.net/')
time.sleep(5)

proxy_ip_list = []
port_list = []

for i in range(1, 20):
    try:
        ip_address = driver.find_element(By.XPATH, f'//*[@id="list"]/div/div[2]/div/table/tbody/tr[{i}]/td[1]').text
        port_add = driver.find_element(By.XPATH, f'//*[@id="list"]/div/div[2]/div/table/tbody/tr[{i}]/td[2]').text
        https_support = driver.find_element(By.XPATH, f'//*[@id="list"]/div/div[2]/div/table/tbody/tr[{i}]/td[7]').text
        if https_support == "yes":
            proxy_ip_list.append(ip_address)
            port_list.append(port_add)
    except:
        pass

driver.quit()  # Close proxy page browser

# Combine IP:PORT
actual_proxy_ip_port = [f"{ip}:{port}" for ip, port in zip(proxy_ip_list, port_list)]

# STEP 2: Try each proxy
print("All proxies:", actual_proxy_ip_port)

for i in range(5):  # Try up to 5 proxies
    PROXY = random.choice(actual_proxy_ip_port)
    print(f"Trying proxy: {PROXY}")
    
    options = Options()
    options.add_argument(f'--proxy-server=http://{PROXY}')
    options.add_argument('--headless')  # Run without GUI for speed
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)  # Avoid hanging
    driver.get("https://quotes.toscrape.com/")
    print("Page title:", driver.title)
    time.sleep(5)
    driver.quit()
    break  # If success, break the loop
    