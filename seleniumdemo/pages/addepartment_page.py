# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addepartment_page.py
# @Author   : Pluto.
# @Time     : 2021/4/29 11:17
from selenium.webdriver.common.by import By

from seleniumdemo.pages.base_page import BasePage
from seleniumdemo.pages.contact_page import ContactPage


class AddepartmentPage(BasePage):
    _department_name = (By.CSS_SELECTOR, "[name='name']")
    _click_department = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _jstree_anchor = (By.XPATH,
                      "//*[@class='qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container']//a[@class='jstree-anchor']")
    _save_button = (By.CSS_SELECTOR, "[d_ck='submit']")
    _cancel_button = (By.CSS_SELECTOR, "[d_ck='cancel']")

    def addepartment(self, department):
        self.find_and_send_keys(self._department_name, department)
        self.find_and_click(self._click_department)
        departmentlist = self.finds(self._jstree_anchor)
        if departmentlist is not None:
            departmentlist[0].click()
        else:
            print("没有部门")
        return self

    def save_department(self):
        self.find_and_click(self._save_button)
        return ContactPage(self.driver)

    def cancel_department(self):
        self.find_and_click(self._cancel_button)
        return ContactPage(self.driver)
