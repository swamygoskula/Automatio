from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

source_element=driver.find_element_by_id("menu_admin_viewAdminModule")
target_element=driver.find_element_by_id("menu_admin_UserManagement")

actions=ActionChains(driver)
actions.drag_and_drop(source_element, target_element). perform()
