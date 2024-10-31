from selenium.webdriver.common.by import By


class UIElements:
    """首页元素"""
    #我
    me_btn_id=(By.ID,"com.yunmall.lc:id/tab_me")
    """注册页"""
    #已有账号去登录
    exist_acc_login_btn_id=(By.ID,"com.yunmall.lc:id/gotologon")
    """登录页面"""
    #账号按钮
    account_btn_id=(By.ID,"com.yunmall.lc:id/logon_account_textview")
    #密码按钮
    password_btn_id=(By.ID,"com.yunmall.lc:id/logon_password_textview")
    #登录按钮
    login_btn_id=(By.ID,"com.yunmall.lc:id/logon_button")
    """个人中心页面"""
    #我的优惠券
    my_coupon_id=(By.ID,"com.yunmall.lc:id/txt_my_coupons")
    #设置按钮
    setting_btn_id=(By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """设置页面"""
    #退出按钮
    exit_btn_id=(By.ID,"com.yunmall.lc:id/setting_logout")
    #弹窗取消按钮
    cancel_btn_id=(By.ID,"com.yunmall.lc:id/ymdialog_left_button")
    #弹窗确认按钮
    confirm_btn_id=(By.ID,"com.yunmall.lc:id/ymdialog_right_button")
    #关闭登录页
    close_login_btn_id = (By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")