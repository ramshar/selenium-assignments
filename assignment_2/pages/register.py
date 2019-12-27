from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import random


class RegisterPage:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def visit(self):
        self.driver.get("https://courses.stage.edx.org/register")

    def fill_registration_form(self):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#register-email")))
        rnd_value = str(random.randint(1, 100000))
        email_field.send_keys("username" + rnd_value + "@yopmail.com")

        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#register-name")))
        full_name_field.send_keys("Ramsha Rahman")

        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#register-username")))
        username_field.send_keys("rr" + rnd_value)

        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#register-password")))
        password_field.send_keys("edxedxedx1")

        country_dropdown = Select(self.driver.find_element_by_css_selector("#register-country"))
        country_dropdown.select_by_visible_text('Pakistan')

        submit_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".register-button")))
        WebDriverWait(self.driver, 5)
        submit_button.click()


a = RegisterPage()
a.visit()
a.fill_registration_form()
