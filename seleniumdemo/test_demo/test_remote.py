# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_remote.py
# @Author   : Pluto.
# @Time     : 2021/4/29 9:18
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestRemote:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
