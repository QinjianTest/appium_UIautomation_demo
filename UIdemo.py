import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

class DemoTrade:
    def test_demo_trade(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "14",  # 替换为你的设备 Android 版本
            "deviceName": "R5CW32J9XDA",  # 替换为你的设备名称
            "appPackage": "com.mitrade.mobile.demo",  # 替换为你的应用包名
            "appActivity": "com.mitrade.app.splash.view.SplashActivity",  # 替换为你的应用启动活动
            'automationName': 'UiAutomator2',  # 使用 UiAutomator2 自动化引擎
            'noReset': True,  # 保持应用的状态
            'disableWindowAnimation': True,# 禁用窗口动画
            'adbExecTimeout': 60000, # 增加设备发现超时时间到 60 秒
            'skipDeviceInitialization': True,  # 跳过设备初始化
        }
        driver = webdriver.Remote('http://localhost:4723', desired_caps)
        #time.sleep(5)
        if driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Hub")'):
            print("识别到Hub")
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Trade")').click()
            time.sleep(1)
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Bitcoin")').click()
            time.sleep(1)
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Buy")').click()
            #进入下单页，获取保证金
            sellPrice1 = driver.find_element(By.ID, 'com.mitrade.mobile.demo:id/tvRealMMargin').get_attribute("text")
            price1 = sellPrice1.split(" ")[1]
            print("前置：",price1)
            time.sleep(1)
            # 点击加号，获取保证金
            driver.find_element(By.ID, 'com.mitrade.mobile.demo:id/rlAdd').click()
            sellPrice2 = driver.find_element(By.ID, 'com.mitrade.mobile.demo:id/tvRealMMargin').get_attribute("text")
            price2 = sellPrice2.split(" ")[1]
            print("后置：", price2)
            # 对比
            if price1 != price2:
                print("价格不同，通过")
        else:
            print("没有进入登录页")
        driver.quit()
        print("------end-----")

if __name__ == '__main__':
    demo_trade = DemoTrade()
    demo_trade.test_demo_trade()
