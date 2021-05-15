# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_appuimRecord.py
# @Author   : Pluto.
# @Time     : 2021/5/15 9:51
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeiXin:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Z91QGEWM2258H"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清除数据
        caps["noReset"] = True
        # 不重启应用
        caps["dontStopAppOnReset"] = True
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

    def test_send_message(self):
        _send_message = "test001"
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h8q").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g1n").send_keys("软件测试")
        sleep(1)
        eles = self.driver.find_elements(MobileBy.XPATH, "//*[@text='软件测试']")
        if len(eles) < 2:
            print("没有该联系人")
        else:
            eles[-1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e60").send_keys(_send_message)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e5w").click()
        news = self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/e5l")
        assert news[-1].text == _send_message

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guo").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        r = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/mr").text
        assert r == "外出打卡成功"

    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name,phone", [("LCQ", "13711111111")], ids={"addmember"})
    def test_addmember(self, name, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys(name)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys(phone)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac9").click()
        # 打印整个页面信息，找到toast元素位置方法
        # sleep(2)
        # print(self.driver.page_source)
        mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert mytoast == "添加成功"

    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name", [("LCQ")], ids={"delete member"})
    def test_deletemember(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h8q").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g1n").send_keys(name)
        sleep(1)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        if len(eles1) == 1:
            print(f"没有名为{name}的成员")
        else:
            eles1[-1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h8g").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(5)
        eles2 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        assert len(eles1) - 1 == len(eles2)
        r = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ccl").text
        assert r == "无搜索结果"
