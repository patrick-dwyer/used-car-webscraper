# pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scraper(driver):

    products = driver.find_elements(By.CLASS_NAME, "vehicle-card")

    scraped_data = []

    for product in products:
        print("__________________________________")
        print((product.text))
    
    return scraped_data

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")

# instantiate Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

# open the specified URL in the browser
driver.get("https://www.subarucalgary.com/vehicles/new/?st=year,desc&view=grid&sc=new&qs=crosstrek")

# execute the scraper function and print the scraped data
print(scraper(driver))

# close the browser
driver.quit()

