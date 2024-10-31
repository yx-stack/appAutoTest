from appAutoTest.base.base import Base
from appAutoTest.page.UIElements import UIElements


class SettingPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)


    #点击退出按钮
    def logout(self,tag=1):
        # 滑动
        self.scroll_screen(1)
        self.click_element(UIElements.exit_btn_id)
        #如果tag==1确认退出，否则取消退出
        if int(tag)==1:
            self.click_element(UIElements.confirm_btn_id)
        else:
            self.click_element(UIElements.cancel_btn_id)

