from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests\chromedriver.exe")
        print("test")
    
    def test_register(self):
        self.regLink = self.WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ml-2")))
        # self.browser.find_element_by_class_name("ml-2")

        self.regLink.click()
        print("test")
        self.username = self.browser.find_element_by_id("id_username")
        self.email = self.browser.find_element_by_id("id_email")
        self.password1 = self.browser.find_element_by_id("id_password1")
        self.password2 = self.browser.find_element_by_id("id_password2")
        self.registerButton = self.browser.find_element_by_class_name("btn login_btn form-control")

        self.username.send_keys("username7")
        self.email.send_keys("qwertghnm@gmail.com")
        self.password1.send_keys("eFgbbcvfgb1!")
        self.password2.send_keys("eFgbbcvfgb1!")

        self.registerButton.click()

    
    def tearDown(self):
        self.browser.quit()