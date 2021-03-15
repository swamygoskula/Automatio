from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://ww1.demoaut.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print('number of links',len(links))

for link in links:
    print(link.text)
driver.find_element_by_link_text("DEMO ACCOUNT").click()
driver.close()