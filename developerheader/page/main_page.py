from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class Test_Main(BaseAction):
    main_me = (By.XPATH,'//*[@text="我的"]')

    def __init__(self, driver):
        super().__init__(driver)

    #点击我的
    def click_mine(self):
        self.click_element(self.main_me)


    #点击消息