from time import sleep

from selenium.webdriver.common.by import By

from appAutoTest.base.getDriver import get_phone_driver
#实例化driver
from appAutoTest.page.publicPage import PublicPage

driver=get_phone_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
#实例化统一入口页
page_obj=PublicPage(driver)
#首页点击我按钮
page_obj.get_homePage().click_me_btn()
#注册页点击已有账号，去登录
page_obj.get_registerPage().click_exist_acc_login()
#调用登录方法，登录页输入账号,登录页输入密码,登录页点击登录按钮
page_obj.get_loginPage().login("13816403462","123214")
toast_element=(By.XPATH,"//*[contains(@text,'错误')]")

toast_txt=page_obj.get_loginPage().get_element(toast_element,timeout=5,poll_frequency=0.1).text
print(toast_txt)

#退出操作
