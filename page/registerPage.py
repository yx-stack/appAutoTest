from appAutoTest.base.base import Base
from appAutoTest.page.UIElements import UIElements


class RegisterPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击已有账号去登录
    def click_exist_acc_login(self):
        self.click_element(UIElements.exist_acc_login_btn_id)