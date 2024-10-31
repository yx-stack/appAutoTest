from appAutoTest.base.base import Base
from appAutoTest.page.UIElements import UIElements


class LoginPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #输入账号密码登录
    def login(self,account,password):
        #输入账号
        self.send_element(UIElements.account_btn_id,account)
        #输入密码
        self.send_element(UIElements.password_btn_id,password)
        #点击登录按钮
        self.click_element(UIElements.login_btn_id)
    def closeLoginPage(self):
        #点击×，退出登录页
        self.click_element(UIElements.close_login_btn_id)
    def if_login_btn(self):
        #判断登录按钮是否存在
        self.get_element(UIElements.close_login_btn_id)

