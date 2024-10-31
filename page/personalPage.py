from appAutoTest.base.base import Base
from appAutoTest.page.UIElements import UIElements


class PersonalPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #获取优惠券元素文本
    def get_my_coupon_text(self):
        #timeout给10秒，在取结果元素的时候，降低失败等待时间
        return self.get_element(UIElements.my_coupon_id,timeout=10).get_attribute("text")
    def click_my_coupon(self):
        self.click_element(UIElements.my_coupon_id)
    #点击设置按钮
    def click_setting(self):
        self.click_element(UIElements.setting_btn_id)
