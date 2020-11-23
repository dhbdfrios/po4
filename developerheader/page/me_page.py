from selenium.webdriver.common.by import By
import logging
from base.base_action import BaseAction
class Test_me(BaseAction):
    me_login = (By.ID,'io.manong.developerdaily:id/login_btn')
    me_nick_name = (By.XPATH,'//*[contains(@text,"xiha")]')
    me_io = (By.XPATH,'//*[contains(@text,"我的IO")]')
    me_setting = (By.XPATH,'//*[contains(@text,"设置")]')
    me_login_info = (By.ID,'io.manong.developerdaily:id/login_btn')
    def __init__(self, driver):
        super().__init__(driver)

    #点击登录注册
    def click_login(self):
        self.click_element(self.me_login)

    def swipe_io_nickname(self):
        nick_name = self.find_element(self.me_nick_name)
        io_icon = self.find_element(self.me_io)
        self.swipe_element(io_icon,nick_name)

    def swipe_io_setting(self):
        setting = self.find_element(self.me_setting)
        io_icon = self.find_element(self.me_io)
        self.swipe_element(io_icon, setting)

    def click_setting(self):
        self.click_element(self.me_setting)

    def get_login_info(self):
        return self.find_element(self.me_login_info).text