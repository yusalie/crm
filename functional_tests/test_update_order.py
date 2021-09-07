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


class TestLogin(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests\chromedriver.exe")
        self.browser.get("http://127.0.0.1:8000/login/?next=/")

    def test_update_order(self):
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "username")))
            self.username.send_keys("sufster")
            self.password = self.browser.find_element_by_id("password")
            self.password.send_keys("glaceon1!")
            
        except Exception as err:
            print(err)

        try:
            self.lgnButton = self.browser.find_element_by_class_name("btn")
            self.lgnButton.click()
        except Exception as err:
            print(err)
            
        try:
            self.update = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "update")))
            
            self.update.click()
        except Exception as err:
            print(err)

        try:
            self.person = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_customer")))
            self.person.click()
            self.value = WebDriverWait(self.browser, 50).until(EC.presence_of_all_elements_located(By.XPATH, "option=4"))
            self.value.click()
            self.item = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_product")))
            self.item.click()
            self.itemvalue = WebDriverWait(self.browser, 50).until(EC.presence_of_all_elements_located(By.XPATH, "option=3"))
            self.itemvalue.click()
            self.status = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_product")))
            self.status.click()
            self.statusvalue = WebDriverWait(self.browser, 50).until(EC.presence_of_all_elements_located(By.XPATH, "option=3"))
            self.statusvalue.click()
            time.sleep(5000)
        except Exception as err:
            print(err)