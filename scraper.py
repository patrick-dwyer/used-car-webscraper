# pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def subaru_calgary_scraper():
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")

    # instantiate Chrome WebDriver with options
    driver = webdriver.Chrome(options=options)

    # open the specified URL in the browser
    driver.get("https://www.subarucalgary.com/vehicles/new/?st=year,desc&view=grid&sc=new")

    products = driver.find_elements(By.CLASS_NAME, "vehicle-card")

    scraped_data = []

    for product in products:
        print("__________________________________")
        output = product.text
        output_clean = output.replace('\n',' ')
        output_clean_parsed = output_clean.split(" ")
        year = output_clean_parsed[6]
        make = output_clean_parsed[7]
        model = output_clean_parsed[8]
        trim = output_clean_parsed[9]

        detailed_specs = product.find_elements(By.CLASS_NAME, "detailed-specs__value")

        specs_list = []
        for specs in detailed_specs:
            specs_list.append(specs.text) 
        
        odometer = specs_list[0]
        colour = specs_list[1]
        transmission = specs_list[2]      
        
        exit()

    # close the browser
    driver.quit()
    
    return scraped_data

# execute the scraper function and print the scraped data
subaru_calgary_scraper()



