from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Test_Setting(BaseAction):
    setting_out = By.XPATH,'//*[contains(@text,"退出当前账户")]'
    setting_alert_out = By.ID,'io.manong.developerdaily:id/md_buttonDefaultPositive'
    def __init__(self, driver):
        super().__init__(driver)

    def click_out(self):
        self.click_element(self.setting_out)

    def click_alert_out(self):
        self.click_element(self.setting_alert_out)

