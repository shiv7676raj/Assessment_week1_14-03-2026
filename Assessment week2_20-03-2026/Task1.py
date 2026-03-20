from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
wait = WebDriverWait(driver,10)
print('Title:',driver.title)
print('URL:',driver.current_url)
#assert "Amazon" in driver.title
assert "amazon.in" in driver.current_url,"didn't find"
print('URL verified successfully!')
dropdown=wait.until(EC.presence_of_element_located((By.ID,"searchDropdownBox")))
select=Select(dropdown)
select.select_by_visible_text("Books")
search=wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
search.send_keys("Harry Potter")
search.send_keys(Keys.ENTER)
products=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal']//h2//span")))
for i in range(5):
    print(products[i].text)
products[0].click()
print('First product clicked!')
driver.quit()