from appium import webdriver

import sys,os
#����Զ���·����python����·��
sys.path.append(os.getcwd())
def get_phone_driver(pac,act):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'snxing'
    desired_caps['appPackage'] =pac
    desired_caps['appActivity'] = act
    #��ȡtoast��Ϣ��������
    desired_caps['automationName'] = 'Uiautomator2'
    return  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # ʵ����page����