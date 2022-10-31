from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("E:\\Driver\\chromedriver.exe")
        cls.driver.implicitly_wait(3)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(3)

    def login(self):
        self.driver.find_element('name', 'username').send_keys("Admin")
        self.driver.implicitly_wait(3)
        self.driver.find_element('name', 'password').send_keys("admin123")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').submit()
        self.driver.implicitly_wait(3)

    def test_admin_Tab(self):
        self.login()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//span[contains(text(), "User Management ")]').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//a[text()="Users"]').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//div[@data-v-2fe357a6]//input[@data-v-844e87dc]').send_keys(
            "Charlie.Carter")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,
                                 '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').submit()
        self.driver.implicitly_wait(3)

    def test_pim_Tab(self):
        # self.login()
        self.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed....!!!")

# driver.get_screenshot_as_file("filename")

