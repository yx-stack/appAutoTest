import os,sys
sys.path.append(os.getcwd())
from time import sleep
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import TimeoutException
from appAutoTest.base import getFileData
from appAutoTest.base.getDriver import get_phone_driver
from appAutoTest.page.publicPage import PublicPage
from appAutoTest.base.getFileData import getFileData
def get_login_data():
   suc_list=[]
   fail_list=[]
   login_data=getFileData().get_yaml_data("login_data.yml")
   for i in login_data:
       #预期失败测试用例case_num,account,passwd,toast,expect_data
       if login_data.get(i).get("toast"):
           fail_list.append((i,login_data.get(i).get("account"),login_data.get(i).get("passwd"),
                            login_data.get(i).get("toast"),login_data.get(i).get("expect_data")))

       else:
           suc_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd"),
                            login_data.get(i).get("expect_data")))


   return {"suc": suc_list, "fail": fail_list}
print(get_login_data().get('suc'))
class TestLogin:
    def setup(self):
        #初始化driver
        self.driver=get_phone_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        #初始化统一入口
        self.obj_page=PublicPage(self.driver)
    def teardown(self):
        #退出driver对象
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_test(self):
        self.obj_page.get_homePage().click_me_btn()
        self.obj_page.get_registerPage().click_exist_acc_login()

    @pytest.mark.parametrize("case_num,account,passwd,expect_data",get_login_data().get("suc"))
    def test_login_suc(self,case_num,account,passwd,expect_data):

        """
        :param case_num: 用例编号
        :param account:用户名
        :param passwd: 密码
        :param expect_data:预期结果
        :return:
        """
        self.obj_page.get_loginPage().login(account,passwd)
        try:
            my_coupon=self.obj_page.get_personalPage().get_my_coupon_text()
            print("------",my_coupon)
            try:
                assert expect_data==my_coupon
            except ArithmeticError:
                """停留在个人中心，需执行退出操作"""
                #截图
                self.obj_page.get_personalPage().screem_shot()
                assert False
            finally:
                #退出driver
                self.obj_page.get_personalPage().click_setting()
                self.obj_page.get_settingPage().logout()
        except TimeoutException:
            #截图
            self.obj_page.get_personalPage().screem_shot()
            #关闭页面
            self.obj_page.get_loginPage().closeLoginPage()
            assert False

    @pytest.mark.parametrize("case_num,account,passwd,toast,expect_data", get_login_data().get("fail"))
    def test_login_fail(self,case_num,account,passwd,toast,expect_data):
        """
        :param case_num: 用例编号
        :param account:用户名
        :param passwd: 密码
        :param toast::错误提示
        :param expect_data:预期结果
        :return:
        """
        self.obj_page.get_loginPage().login(account, passwd)
        try:
            # 获取到toast
            toast_data = self.obj_page.get_personalPage().get_toast(toast)
            print(toast_data)
            try:
                #判断是否有登录按钮
                self.obj_page.get_loginPage().if_login_btn()
                #断言成功
                assert toast_data == expect_data
                #关闭登录页面
                self.obj_page.get_loginPage().closeLoginPage()
            except TimeoutException:
                #截屏
                self.obj_page.get_loginPage().screem_shot()
                #可能进入个人中心页，点击退出页面
                self.obj_page.get_personalPage().click_setting()
                self.obj_page.get_settingPage().logout()
                assert False
            except AssertionError:
                # 截屏
                self.obj_page.get_loginPage().screem_shot()
                #关闭登录页
                self.obj_page.get_loginPage().closeLoginPage()
                assert False
        except TimeoutException:
            #获取不到toast
            try:
                #登录按钮存在关闭登录页面
                self.obj_page.get_loginPage().if_login_btn()
                self.obj_page.get_loginPage().closeLoginPage()
            except TimeoutException:
                # 截图
                self.obj_page.get_personalPage().screem_shot()
                #登录按钮不存在，可能进入个人中心，退出登录
                self.obj_page.get_personalPage().click_setting()
                self.obj_page.get_settingPage().logout()
                assert False





