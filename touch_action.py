from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'BTF4C17216005082'

desired_caps['app'] = 'E:\mymoney.apk'
desired_caps['appPackage'] = 'com.mymoney'
desired_caps['appActivity'] = 'com.mymoney.biz.splash.SplashScreenActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    return x,y

# 水平向左滑动
def swipeLeft():
    # 拿到屏幕的尺寸
    l = get_size()

    # 起点
    x1 = l[0]*0.9
    y1 = l[1]*0.5
    x2 = l[0]*0.1

    # 最后一个参数是滑动过程的时长 duration
    driver.swipe(x1,y1,x2,y1,1000)

# 向上滑动
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)

def swipeDown():
    l=get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.35)
    y2 = int(l[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)

def swipeRight():
    l=get_size()
    y1 = int(l[1] * 0.5)
    x1 = int(l[0] * 0.25)
    x2 = int(l[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)

# 下一步的按钮
WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id('com.mymoney:id/next_btn'))
# 向左滑动两次 导航界面
for i in range(2):
    swipeLeft()
    sleep(0.5)

# 点击开始笔记按钮
driver.find_element_by_id('com.mymoney:id/begin_btn').click()

# 这个应用有的时候会弹出红包广告 如果有 关闭
try:
    closeBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closeBtn.click()

# 点击更多按钮
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()
# 等待整个布局加载完成
WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id('com.mymoney:id/content_container_ly'))
# 向上滑动
swipeUp()
# 点击高级
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
# 点击密码手势
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
#点击手势密码保护
driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

# 手势滑动两次
for i in range(2):
    TouchAction(driver).\
        press(x=240,y=578).\
        wait(1000).\
        move_to(x=540,y=578).\
        wait(1000).\
        move_to(x=842,y=869).\
        wait(1000).\
        move_to(x=833,y=1170).\
        wait(1000).\
        release().\
        wait(1000).\
        perform()

