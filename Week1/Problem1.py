from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(3)
username=driver.find_element(By.CSS_SELECTOR,"input[name='username']")
print(username)
password=driver.find_element(By.CSS_SELECTOR,"input[id='password']")
print(password)
login_btn=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
print(login_btn)
footer_link = driver.find_element(By.CSS_SELECTOR,"#page-footer a")
print(footer_link)
print("Found the elements")
driver.quit()