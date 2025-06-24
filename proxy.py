import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
PROXY = "20.210.76.175:8561"

options = Options()
options.add_argument(f'--proxy-server=https://{PROXY}')
driver = webdriver.Chrome(options=options)

driver.get("https://quotes.toscrape.com/")
time.sleep(10)