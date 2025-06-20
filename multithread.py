from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import threading
from concurrent.futures import ThreadPoolExecutor

link_list =['https://www.daraz.com.bd/routers/?page=1','https://www.daraz.com.bd/routers/?page=2','https://www.daraz.com.bd/routers/?page=3','https://www.daraz.com.bd/routers/?page=4','https://www.daraz.com.bd/routers/?page=5','https://www.daraz.com.bd/routers/?page=6']


def scrape_func(link):
    driver = webdriver.Chrome()
    driver.get(link)
    print(f"{threading.current_thread().name} scraped")

    driver.maximize_window()
with ThreadPoolExecutor(max_workers=2) as executor:
    execute = [executor.submit(scrape_func,link) for link in link_list]

time.sleep(20)