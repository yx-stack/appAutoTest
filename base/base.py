import os
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,loc,timeout=10,poll_frequency=0.9):
        """
        获取单个元素方法
        :param loc:（By.ID,id属性值），(By.CLASS_NAME,class属性值），(By.XPATH,xpath属性值）
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素时间间隔
        :return::元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        获取多个元素方法
        :param loc:（By.ID,id属性值），(By.CLASS_NAME,class属性值），(By.XPATH,xpath属性值）
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素时间间隔
        :return:元素定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))
    def click_element(self, loc,timeout=10,poll_frequency=1.0):
        """
        点击元素方法
        :param loc:（By.ID,id属性值），(By.CLASS_NAME,class属性值），(By.XPATH,xpath属性值）
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素时间间隔
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).click()
    def send_element(self,loc,text,timeout=10,poll_frequency=1.0,):
        """
        输入文本内容
        :param loc:（By.ID,id属性值），(By.CLASS_NAME,class属性值），(By.XPATH,xpath属性值）
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素时间间隔
        :return:
        """
        self.input=self.get_element(loc, timeout, poll_frequency)
        self.input.clear()
        self.input.send_keys(text)
    def scroll_screen(self,sc=1):
        time.sleep(3)
        """
        :param sc: sc=1:向上，sc=2:向下，sc=3：向左，sc=4:向右
        :return:
        """
        #获取屏幕分辨率
        self.screen_size=self.driver.get_window_size()
        #获取宽
        self.wight=self.screen_size.get("width")
        #获取高
        self.high=self.screen_size.get("height")
        #根据宽高判断
        if sc==1:
            #向上滑动
            self.driver.swipe(self.wight*0.5, self.high*0.8, self.wight*0.5,self.high*0.2,2000)
        if sc==2:
            #向下滑动
            self.driver.swipe(self.wight*0.5, self.high*0.2, self.wight*0.8,high*0.2,2000)
        if sc==3:
            #向左滑动
            self.driver.swipe(self.wight*0.8, self.high*0.5, self.wight*0.2,self.high*0.5,2000)
        if sc==4:
            #向右滑动
            self.driver.swipe(self.wight*0.2, self.high*0.5, self.wight*0.8,self.high*0.5,2000)
    #图片名默认叫截图
    def screem_shot(self):
        """
        报告添加截图
        :param name:截图名字
        :return:
        """
        png_name=(os.getcwd()+os.sep+"Images"+os.sep+"{}.png".format(int(time.time()))).replace("\\","/").strip()
        #png_name="F:/PYDEMO/appTest/appAutoTest/Images"+"/{}.png".format(int(time.time()))
        #截图方法
        self.driver.get_screenshot_as_file(png_name)
        #二进制打开文件
        with open(png_name,"rb") as f:
            allure.attach(f.read(),"截图",allure.attachment_type.PNG)

    def get_toast(self,toast):
        toast_text=(By.XPATH,"//*[contains(@text,'{}')]".format(toast))
        return self.get_element(toast_text,timeout=10,poll_frequency=.5).text

