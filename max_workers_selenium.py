import multiprocessing
import psutil
from selenium import webdriver
import time

def measure_selenium_memory():
    # Launch Selenium browser
    driver = webdriver.Chrome()
    time.sleep(2)  # Give browser a moment to settle
    
    # Get the process id
    pid = driver.service.process.pid
    
    # Get memory usage of main driver process + its children (renderer etc)
    proc = psutil.Process(pid)
    mem = proc.memory_info().rss
    for child in proc.children(recursive=True):
        mem += child.memory_info().rss
    
    # Convert to MB
    mem_mb = mem / (1024 ** 2)
    driver.quit()
    return mem_mb

def estimate_max_selenium_workers_dynamic():
    logical_cores = multiprocessing.cpu_count()
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    
    print(f"Logical cores: {logical_cores}")
    print(f"Available RAM: {ram_gb:.2f} GB")

    # Measure actual memory usage of one selenium instance
    selenium_mem_mb = measure_selenium_memory()
    print(f"Measured Selenium instance memory: {selenium_mem_mb:.2f} MB")

    # Compute max workers
    max_by_ram = (ram_gb * 1024) / selenium_mem_mb
    max_by_cpu = logical_cores * 1.5
    recommended = int(min(max_by_ram, max_by_cpu))

    print(f"Estimated max Selenium workers: {recommended}")
    return recommended

estimate_max_selenium_workers_dynamic()
