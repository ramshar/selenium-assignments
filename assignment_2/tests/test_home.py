import unittest
from selenium import webdriver
from assignment_2.pages.home import HomePage
# from ..Pages import Home
# from ..Pages import Login


class EdxLogin(unittest.TestCase):

    def setUp(self):
        # Initialize webdriver
        self.driver = webdriver.Firefox()
        self.homepage = HomePage()


    # def visit(self):
    #     self.driver.get(URL)

    def test_home_page(self):
        self.homepage.visit()
        self.homepage.is_browser_on_page()
        self.assertEqual(
            self.homepage.driver.current_url, "https://stage.edx.org/"
        )

    def test_login_page(self):
        self.homepage.visit()
        self.homepage.is_browser_on_page()
        self.homepage.go_to_login_page()
        self.assertEqual(
            self.homepage.driver.current_url, "https://courses.stage.edx.org/login"
        )

    def test_user_login(self):
        # Open the target page
        self.homepage.visit()
        self.homepage.is_browser_on_page()
        self.homepage.go_to_login_page()
        # self.loginpage.fill_form()
        # self.loginpage.submit_form()
        # self.home.visit()
        # self.home.is_browser_on_page()
        # self.home.go_to_login_page()
        # Assert that 'edX' is present in browser title
        # self.assertTrue(self.login.is_browser_on_the_page())
        # Find and fill the email field
        # self.login.fill_form()
        # Find and click the submit button
        # self.login.submit_form()
        # Assert that 'Dashboard' is present in target pages browser title
        # self.dashboard.is_browser_on_the_page()
        self.assertIn(self.loginpage.driver.title, "Dashboard")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
