from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from assignment_2.pages.constants import URL


class HomePage():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def visit(self):
        self.driver.get(URL)
        # self.driver.implicitly_wait(10)

    def is_browser_on_page(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.js-user-cta .btn')))

    def go_to_login_page(self):
        login_btn = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-user-cta .btn")))
        login_btn.click()

    def go_to_register_page(self):
        register_btn = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-user-cta .btn.btn-blue")))
        register_btn.click()


homePage = HomePage()
homePage.visit()
homePage.is_browser_on_page()
# homePage.go_to_login_page()
homePage.go_to_register_page()