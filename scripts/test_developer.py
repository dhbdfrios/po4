import sys,os
sys.path.append(os.getcwd()) #告诉pytest框架要检索整个项目目录
from base.base_driver import init_driver
from page.main_page import Test_Main
from page.me_page import Test_me
from page.login_page import Test_Login
from page.email_page import Test_Email
from page.setting_page import Test_Setting
import time
class Test_Developer:
    #前置代码
    def setup(self):
        #1.初始化driver
        self.driver = init_driver()
        #2.初始化page
        self.main_page = Test_Main(self.driver)
        self.me_page = Test_me(self.driver)
        self.login_page = Test_Login(self.driver)
        self.email_page = Test_Email(self.driver)
        self.setting_page = Test_Setting(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    #只负责调用
    def test_developer(self):
        #点击我的
        self.main_page.click_mine()
        #点击登录注册
        self.me_page.click_login()
        #点击邮箱登录
        self.login_page.click_email()
        #完成登录
        self.email_page.login()
        self.me_page.swipe_io_nickname()
        self.me_page.click_setting()
        self.setting_page.click_out()
        self.setting_page.click_alert_out()
        self.me_page.swipe_io_setting()
        result = self.me_page.get_login_info()
        assert '登录' in result

