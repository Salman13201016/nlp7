import multiprocessing
import psutil

def estimate_max_selenium_workers():
    logical_cores = multiprocessing.cpu_count()
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    # Assume ~500MB per worker
    max_by_ram = ram_gb / 0.5
    max_by_cpu = logical_cores * 1.5
    recommended = int(min(max_by_ram, max_by_cpu))
    print(f"Logical cores: {logical_cores}")
    print(f"Available RAM: {ram_gb:.2f} GB")
    print(f"Estimated max Selenium workers: {recommended}")
    return recommended

estimate_max_selenium_workers()