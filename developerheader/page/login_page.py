from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class Test_Login(BaseAction):
    me_login = (By.ID,'io.manong.developerdaily:id/btn_email')
    def __init__(self, driver):
        super().__init__(driver)
    #点击邮箱登录
    def click_email(self):
        self.click_element(self.me_login)