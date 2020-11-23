from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:
    def __init__(self,driver):
        self.driver = driver


    # 自己封装的方法 就是用来找元素
    def find_element(self, tuple):
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(tuple[0], tuple[1]))

    #把点击的方法抽取出来
    def click_element(self,tuple):
        self.find_element(tuple).click()

    #向输入框里面输入内容的方法
    def input_element_content(self,tuple,content):
        self.find_element(tuple).send_keys(content)

    def swipe_element(self,start_ele,end_ele):
        self.driver.drag_and_drop(start_ele, end_ele)
