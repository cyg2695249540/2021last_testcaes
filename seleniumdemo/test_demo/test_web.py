# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_web.py
# @Author   : Pluto.
# @Time     : 2021/4/29 8:59
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeb():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_web(self):
        self.driver.get(url="https://ceshiren.com")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@title='所有分类' and @class='ember-view']")))
        self.driver.find_element(By.XPATH, "//*[@title='所有分类' and @class='ember-view']").click()
        time.sleep(3)
