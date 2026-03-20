from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://automationexercise.com/signup")
name=wait.until(EC.presence_of_element_located((By.NAME,"name")))
name.send_keys("Selena Ray")
email=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qa='signup-email']")))
email.send_keys("sele123@test.com")
btn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='signup-button']")))
btn.click()
title=wait.until(EC.element_to_be_clickable((By.ID,"id_gender1")))
title.click()
newsletter=wait.until(EC.element_to_be_clickable((By.ID,"newsletter")))
newsletter.click()
s_offers=wait.until(EC.element_to_be_clickable((By.ID,"optin")))
s_offers.click()
print("Newsletter selected:", newsletter.get_attribute("checked"))
print("Special offers selected:", s_offers.get_attribute("checked"))
driver.quit()