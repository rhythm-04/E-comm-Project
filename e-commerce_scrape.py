import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
ac = ActionChains(driver)
print("Welcome to E-commerce")
search = input("Search: ")
page = int(input("Number of pages of data you want: "))
time.sleep(2)
y = 1000

# Scraping amazon
az_product_list = []
print("Welcome to amazon.in")
az_url = "https://www.amazon.in/"
driver.get(az_url)
time.sleep(2)
az_search_bar = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
az_search_bar.send_keys(search)
az_search_button = driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
az_search_button.click()
time.sleep(5)

for i in range(1, page + 1):
    az_products = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")
    time.sleep(3)
    #extracting amazon product details
    for az_product in az_products:
        try:
            product_name_az = az_product.find_element(By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")
            name_az = product_name_az.text
            link_az = az_product.find_element(By.CSS_SELECTOR, "h2 > a")
            url_az = link_az.get_attribute("href")
            time.sleep(2)
            print("Product Name:", name_az)
            print("Product URL:", url_az)
        except:
            name_az = ""
            url_az = ""
        try:
            price_az = az_product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
            print("Price:", price_az)
        except:
            price_az = ""
        try:
            mrp_az = az_product.find_element(By.CSS_SELECTOR, "span.a-price.a-text-price").text
            print("MRP:", mrp_az)
        except:
            mrp_az = ""

        try:
            rating_az = az_product.find_element(By.CSS_SELECTOR, "span.a-declarative span.a-icon-alt").get_attribute("textContent")
            print("Rating:", rating_az)
        except:
            rating_az = ""
        time.sleep(1)

        try:
            rating_count_az = az_product.find_element(By.CSS_SELECTOR,"span.a-size-base.s-underline-text").text
            print("Rating Count:", rating_count_az)
        except:
            rating_count_az = ""
        
        # dic to save amazon extracted details
        az_product_details = {
            'product name': name_az,
            'product url': url_az,
            'price': price_az,
            'mrp': mrp_az,
            'rating': rating_az,
            'count of ratings': rating_count_az,
        }
        # amazon dic to amazon list
        az_product_list.append(az_product_details)



    try:
        next_button_az = driver.find_element(By.LINK_TEXT, "Next")
        driver.execute_script("arguments[0].scrollIntoView();", next_button_az)
        next_button_az.click()
        time.sleep(5)
    except:
        print("Not able to click the next button")
    
# converting amazon scraped list into dataframe and cleaning data with the help of pandas
az_df = pd.DataFrame(az_product_list)
az_df = az_df[az_df["product name"].notna()]
az_df["rating"]=az_df["rating"].str.slice(0,3)
az_df["rating"] =az_df["rating"].str.extract(r'(\d+\.\d+)').astype(float).round(1)
az_rating_mean = az_df["rating"].mean()
az_rating_mean = az_rating_mean.__round__(1)
az_df["rating"] = az_df["rating"].fillna(az_rating_mean)
az_df["count of ratings"] = az_df["count of ratings"].str.replace(',','')
az_df["count of ratings"]=az_df["count of ratings"].str.extract(r'(\d+)').astype(float).round(1)
az_rating_count_mean = az_df["count of ratings"].mean()
az_rating_count_mean = az_rating_count_mean.__round__(1)
az_df["count of ratings"] = az_df["count of ratings"].fillna(az_rating_count_mean)
az_df["price"] = az_df["price"].str.replace(',','')
az_df["price"] = az_df["price"].str.extract(r'(\d+)').astype(float).round(1)
az_price_mean = az_df["price"].mean()
az_price_mean = az_price_mean.__round__(1)
az_df["price"]= az_df["price"].fillna(az_price_mean)
az_df["mrp"] = az_df["mrp"].str.slice(1,)
az_df["mrp"] = az_df["mrp"].str.replace(',','')
az_df["mrp"] = az_df["mrp"].str.extract(r'(\d+)').astype(float).round(1)
az_df["mrp"]=az_df["mrp"].fillna(az_df["price"])
print(az_df)

# converting df to csv
az_df.to_csv(f"{search} amazon e-comm.csv", index=False)



# scrape flipkart
print("welcome to flipkart.com")
fk_product_list = []
fk_url = "https://www.flipkart.com/"
driver.get(fk_url)

# closing the login pop-up
try:
    fk_pop_up_button = driver.find_element(By.CLASS_NAME, "_30XB9F")
    ac.move_to_element(fk_pop_up_button).click().perform()
    time.sleep(3)
except:
    print("Popup not found or unable to close it")

fk_search_bar = driver.find_element(By.CLASS_NAME, "Pke_EE")
fk_search_bar.send_keys(search)
fk_search_button = driver.find_element(By.CLASS_NAME, "_2iLD__")
fk_search_button.click()
time.sleep(5)

for i in range(1, page + 1):
    try:
        fk_products = driver.find_elements(By.CLASS_NAME, "_2kHMtA")
        # extracting flipkart product details
        for fk_product in fk_products:
            try:
                product_name_fk = fk_product.find_element(By.CLASS_NAME, "_4rR01T")
                name_fk = product_name_fk.text
                print(name_fk)
                link_fk = fk_product.find_element(By.CLASS_NAME,"_1fQZEK")
                url_fk = link_fk.get_attribute("href")
                print(url_fk)
            except:
                name_fk = ""
                url_fk = ""

            try:
                price_fk = fk_product.find_element(By.CLASS_NAME, "_30jeq3._1_WHN1").text
                print(price_fk)
            except:
                price_fk = ""

            try:
                mrp_fk = fk_product.find_element(By.CLASS_NAME, "_3I9_wc._27UcVY").text
                print(mrp_fk)
            except:
                mrp_fk = ""

            try:
                rating_fk = fk_product.find_element(By.CLASS_NAME, "_3LWZlK").text
                print(rating_fk)
            except:
                rating_fk = ""

            try:
                rating_count_fk = fk_product.find_element(By.CLASS_NAME, "_2_R_DZ").text
                print(rating_count_fk)
            except:
                rating_count_fk = ""

            # dic to save flipkart extracted details
            fk_product_details = {
                'product name': name_fk,
                'product url': url_fk,
                'price': price_fk,
                'mrp': mrp_fk,
                'rating': rating_fk,
                'count of ratings': rating_count_fk,
            }
            # flipkart dic to flipkart list
            fk_product_list.append(fk_product_details)
            
    except:
        print("Unable to find products")

    time.sleep(2)

    try:
        next_button_fk = driver.find_element(By.CLASS_NAME, "_1LKTO3")
        next_button_fk.click()
        time.sleep(3)
    except:
        print("Unable to click next button")

# converting flipkart scraped list into dataframe and cleaning data with the help of pandas
fk_df = pd.DataFrame(fk_product_list)
fk_df = fk_df[fk_df["product name"].notna()]
fk_df["rating"] =fk_df["rating"].str.extract(r'(\d+\.\d+)').astype(float).round(1)
fk_rating_mean = fk_df["rating"].mean()
fk_rating_mean = fk_rating_mean.__round__(1)
fk_df["rating"] = fk_df["rating"].fillna(fk_rating_mean)
fk_df["count of ratings"] = fk_df["count of ratings"].str.split("&",expand=True)[0]
fk_df["count of ratings"] = fk_df["count of ratings"].str.replace(" Ratings","")
fk_df["count of ratings"] = fk_df["count of ratings"].str.replace(",","")
fk_df["count of ratings"] = fk_df["count of ratings"].str.extract(r'(\d+)').astype(float).round(1)
fk_rating_count_mean = fk_df["count of ratings"].mean()
fk_rating_count_mean = fk_rating_count_mean.__round__(1)
fk_df["count of ratings"] = fk_df["count of ratings"].fillna(fk_rating_count_mean)
fk_df["price"] = fk_df["price"].str.replace(",","")
fk_df["price"] = fk_df["price"].str.slice(1,)
fk_df["price"] = fk_df["price"].str.extract(r'(\d+)').astype(float).round(1)
fk_price_mean = fk_df["price"].mean()
fk_price_mean = fk_price_mean.__round__(1)
fk_df["price"] = fk_df["price"].fillna(fk_price_mean)
fk_df["mrp"] = fk_df["mrp"].str.replace(",","")
fk_df["mrp"] = fk_df["mrp"].str.slice(1,)
fk_df["mrp"] = fk_df["mrp"].str.extract(r'(\d+)').astype(float).round(1)
fk_df["mrp"]=fk_df["mrp"].fillna(fk_df["price"])
print(fk_df)

# converting df to csv
fk_df.to_csv(f"{search}_flipkart_e-comm.csv", index=False)

driver.quit()


