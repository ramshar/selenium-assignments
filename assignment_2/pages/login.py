from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from assignment_2.pages.constants import USER_PASSWORD,USER_EMAIL


class LoginPage:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def visit(self):
        self.driver.get("https://courses.stage.edx.org/login")
        # self.driver.implicitly_wait(10)

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

    def fill_form(self):
        email_elem = self.driver.find_element_by_css_selector('#login-email')
        email_elem.send_keys(USER_EMAIL)
        pwd_elem = self.driver.find_element_by_css_selector('#login-password')
        pwd_elem.send_keys(USER_PASSWORD)

    def submit_form(self):
        submit_elem = self.driver.find_element_by_css_selector('button[type="submit"]')
        submit_elem.click()

# a= LoginPage()
# a.visit()
# a.is_browser_on_the_page()
# a.fill_form()
# a.submit_form()