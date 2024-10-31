from appAutoTest.page.homePage import HomePage
from appAutoTest.page.loginPage import LoginPage
from appAutoTest.page.personalPage import PersonalPage
from appAutoTest.page.registerPage import RegisterPage
from appAutoTest.page.settingPage import SettingPage


class PublicPage:
    def __init__(self,driver):
        self.driver=driver
    def get_homePage(self):
        """返回首页实例化对象"""
        return HomePage(self.driver)
    def get_loginPage(self):
        """返回登录页实例化对象"""
        return LoginPage(self.driver)
    def get_personalPage(self):
        """返回我的页实例化对象"""
        return PersonalPage(self.driver)
    def get_registerPage(self):
        """返回注册页实例化对象"""
        return RegisterPage(self.driver)
    def get_settingPage(self):
        """返回设置页实例化对象"""
        return SettingPage(self.driver)

