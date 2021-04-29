# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2021/4/29 11:17
from selenium.webdriver.common.by import By

from seleniumdemo.pages.base_page import BasePage


class ContactPage(BasePage):
    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    def goto_addmember_page(self):
        from seleniumdemo.pages.addmamber_page import AddmemberPage
        self.wait_for_click(self._addmember_butto)
        self.find_and_click(self._addmember_butto)
        return AddmemberPage(self.driver)

    def get_mamberlist(self):
        self.wait_for_click(self._member_list)
        memberlist = self.finds(self._member_list)
        return [name.text for name in memberlist]
