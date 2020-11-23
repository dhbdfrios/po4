from appium import webdriver
#初始化driver 把driver对象返回
def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = 'io.manong.developerdaily'
    desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
