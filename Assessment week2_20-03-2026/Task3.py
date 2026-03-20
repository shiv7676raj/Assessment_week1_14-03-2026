from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver, 10)
driver.get("https://www.google.com")
search=wait.until(EC.presence_of_element_located((By.NAME,"q")))
search.send_keys("Selenium Python")
sug=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//ul[@role='listbox']//li//span")))
for s in sug:
    print(s.text)

sug[0].click()
print('First Search result clicked!')