# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_scroll.py
# @Author   : Pluto.
# @Time     : 2021/5/17 20:05
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestScroll:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.android.settings"
        caps["appActivity"] = ".Settings"
        # 不清除数据
        caps["noReset"] = True
        # 不重启应用
        # caps["dontStopAppOnReset"] = True
        # 等待页面空闲的时间
        caps['settings[waitForIdleTimeout]'] = 1
        # 跳过安装，权限设置等操作
        caps["skipDeviceInitialization"] = True
        # 设置可输入中文
        caps["unicodekeyBoard"] = True
        caps["resetkeyBoard"] = True
        # 自动判断弹框
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_scroll(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("关于平板电脑").instance(0));').click()
        sleep(5)
