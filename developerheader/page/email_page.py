from selenium.webdriver.common.by import By
import logging
from base.base_action import BaseAction
class Test_Email(BaseAction):
    email_username = (By.ID,'io.manong.developerdaily:id/edt_email')
    email_pwd = (By.ID,'io.manong.developerdaily:id/edt_password')
    email_login_btn = (By.ID,'io.manong.developerdaily:id/btn_login')
    def __init__(self, driver):
        super().__init__(driver)

    #完成登录操作
    def login(self):
            #输入邮箱
            self.input_element_content(self.email_username,'benbenxiong567@163.com')
            #输入密码
            self.input_element_content(self.email_pwd,'1393434432500')
            #点击登录
            self.click_element(self.email_login_btn)



