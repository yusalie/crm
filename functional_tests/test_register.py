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
        
    
    def test_register(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("dxfxxdcffxfxfxf")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("yghvtfvghvguvfhhvgv@gmail.com")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("ftfftufctfyvcgfdyvfc1!")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("ftfftufctfyvcgfdyvfc1!")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
        
        time.sleep(2000)
