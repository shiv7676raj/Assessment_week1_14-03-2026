from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
websites = [
    "https://www.thesouledstore.com/",
    "https://www.nike.in/",
    "https://www.bbc.com/news",
    "https://www.python.org/"
]
for site in websites:
    sleep(3)
    driver.get(site)
    print("Page Title:", driver.title)

driver.quit()