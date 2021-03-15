import unittest
from selenium import webdriver
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def SetUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
        cls.driver.maximize_window()
    def test_HomePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"web page title is not matching")

    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("adminb123")
        self.driver.find_element_by_name("Submit")
        self.assertEqual("OrangeHRM", self.driver.title, "web page title is not matching")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed....")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..C:\\Users\hp\\PycharmProjects\\Automatio\\Reports"))