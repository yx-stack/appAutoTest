from appAutoTest.base.base import Base
from appAutoTest.page.UIElements import UIElements


class HomePage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    """点击我按钮"""
    def click_me_btn(self):
        self.click_element(UIElements.me_btn_id)
