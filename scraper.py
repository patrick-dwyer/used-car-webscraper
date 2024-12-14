# pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from dealer import Dealer, Inventory
import time

def subaru_calgary_scraper(dealershipName, weblink):
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")

    # instantiate Chrome WebDriver with options
    driver = webdriver.Chrome(options=options)

    # open the specified URL in the browser
    driver.get(weblink)

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(1)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #find all vehicle products
    products = driver.find_elements(By.CLASS_NAME, "vehicle-card")

    #list to store vehicle objects
    scraped_data = []

    address = driver.find_elements(By.CLASS_NAME, 'footer__address')
    for i in address:
        print(i.text)

    #dealership info
    dealer = Dealer(name=dealershipName, location=address, inventory=[])

    for product in products:
        # print("__________________________________")
        output = product.text
        output_clean = output.replace('\n',' ')
        output_clean_parsed = output_clean.split(" ")
        year = output_clean_parsed[6]
        make = output_clean_parsed[7]
        model = output_clean_parsed[8]
        trim = output_clean_parsed[9]

        #find price        
        dollar_sign_index = output_clean_parsed.index('$')
        price = output_clean_parsed[dollar_sign_index + 1]
        

        detailed_specs = product.find_elements(By.CLASS_NAME, "detailed-specs__value")

        specs_list = []
        for specs in detailed_specs:
            specs_list.append(specs.text) 
        
        odometer = specs_list[0]
        colour = specs_list[1]
        transmission = specs_list[2]

        vehicle = Inventory(make=make, model=model, trim=trim, year=year, odometer=odometer, colour=colour, transmission=transmission, price=price)
        scraped_data.append(vehicle)
        obj_vars = vars(vehicle)
        print(obj_vars)

        # exit()    

    # close the browser
    driver.quit()
    
    return scraped_data

# execute the scraper function and print the scraped data
data = subaru_calgary_scraper('Subaru Calgary', "https://www.subarucalgary.com/vehicles/new/?st=year,desc&view=grid&sc=used")
print(len(data))





