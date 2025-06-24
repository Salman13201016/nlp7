import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Fixed Proxy
PROXY = "51.158.105.94:31826"  # Use correct port for this IP

def scrape_with_fixed_proxy():
    print(f"\n Using Proxy: {PROXY}")
    try:
        options = Options()
        # options.add_argument("--headless")  # Uncomment to run browser in background
        options.add_argument(f'--proxy-server=http://{PROXY}')

        driver = webdriver.Chrome(options=options)

        #Check IP
        driver.get("https://httpbin.org/ip")
        time.sleep(2)

        # Scrape Quotes
        driver.get("https://quotes.toscrape.com")
        time.sleep(2)
        quotes = driver.find_elements(By.CSS_SELECTOR, ".quote span.text")

        if not quotes:
            raise Exception("No quotes found — maybe blocked.")

        print("Quotes Found:")
        for q in quotes:
            print(q.text)

        driver.quit()

    except Exception as e:
        print("Error occurred:", e)
        try:
            driver.quit()
        except:
            pass

# Run the function
scrape_with_fixed_proxy()
