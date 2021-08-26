# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from accounts.views import home, userPage, accountSettings, registerPage, loginPage, logoutUser, products, customer



# class TestUrls(SimpleTestCase):
#     def test_home_url(self):
#         url = reverse('home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, home)
        
#     def test_user_url(self):
#         url = reverse('user-page')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, userPage)
        
#     def test_account_url(self):
#         url = reverse('account')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, accountSettings)
        
#     def test_register_url(self):
#         url = reverse('register')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, registerPage)
        
#     def test_login_url(self):
#         url = reverse('login')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, loginPage)
        
#     def test_logout_url(self):
#         url = reverse('logout')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, logoutUser)
        
#     def test_products_url(self):
#         url = reverse('products')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, products)