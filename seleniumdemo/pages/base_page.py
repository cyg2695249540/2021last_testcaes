# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_page.py
# @Author   : Pluto.
# @Time     : 2021/4/29 11:17
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, base_driver=None):
        if base_driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver: WebDriver = base_driver
        if self._base_url != "":
            self.driver.get(url=self._base_url)
        self.driver.implicitly_wait(3)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_send_keys(self, locator, value):
        return self.find(locator).send_keys(value)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_click(self, element):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    def get_result_text(self):
        sleep(1)
        getresult = (By.ID, "js_tips")
        return self.find_and_get_text(getresult)
