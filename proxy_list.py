import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)

driver.get('https://free-proxy-list.net/')
proxy_ip_list = []
port_list = []

for i in range(1,19):
    j = str(i)
    ip_address = driver.find_element(By.XPATH,'//*[@id="list"]/div/div[2]/div/table/tbody/tr['+j+']/td[1]').text
    port_add =  driver.find_element(By.XPATH,'//*[@id="list"]/div/div[2]/div/table/tbody/tr['+j+']/td[2]').text
    https_support = driver.find_element(By.XPATH, f'//*[@id="list"]/div/div[2]/div/table/tbody/tr[{i}]/td[7]').text
    if(https_support=="yes"):
        port_list.append(port_add)
        proxy_ip_list.append(ip_address)
driver.quit()


actual_proxy_ip_port = [f"{a}:{b}" for a, b in zip(proxy_ip_list, port_list)]

print("all proxy ip list",actual_proxy_ip_port)
import random
for i in range(1,21):
    PROXY = random.choice(actual_proxy_ip_port)
    print("proxy ip",PROXY)
    options = Options()
    options.add_argument(f'--proxy-server=http://{PROXY}')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)

    driver.get("https://quotes.toscrape.com/")
    time.sleep(10)
    driver.quit()
    break