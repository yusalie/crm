from django.test.testcases import TransactionTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestLoginIncorrectDetails(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests\chromedriver.exe")
        self.browser.get("http://127.0.0.1:8000/login/?next=/")

    def test_login_incorrect_details(self):
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "username")))
            self.username.send_keys("vnjdfngvjfdbjdfnnjsjsdhs")
            self.password = self.browser.find_element_by_id("password")
            self.password.send_keys("dgyawgdygw!")
            
        except Exception as err:
            print(err)

        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)