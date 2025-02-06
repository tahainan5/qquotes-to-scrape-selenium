from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 

author_dict = {"name" : [], "birth_date" : [], "birth_place" : []}
author_urls = []

url = "https://quotes.toscrape.com"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url)

login_button = driver.find_element(By.XPATH, "//a[text() = 'Login']")
login_button.click()

username = driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("username")

password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("password")

login = driver.find_element(By.CSS_SELECTOR, "input[value = 'Login']")
login.click()

while True: 
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    for quote in quotes: 
        author_link = quote.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        author_urls.append(author_link)
    
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        next_button.click()
    except:
        break

author_urls = list(set(author_urls))

for url in author_urls:
    driver.get(url)
    
    name = driver.find_element(By.CSS_SELECTOR, "h3.author-title").text
    author_dict["name"].append(name)

    birth_date = driver.find_element(By.CSS_SELECTOR, "span.author-born-date").text
    author_dict["birth_date"].append(birth_date)

    birth_place = driver.find_element(By.CSS_SELECTOR, "span.author-born-location").text
    author_dict["birth_place"].append(birth_place)

df = pd.DataFrame(author_dict)
df.to_excel("yazarlar.xlsx")
