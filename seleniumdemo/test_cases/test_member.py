# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2021/4/29 11:18
import pytest

from seleniumdemo.pages.main_page import MainPage


class TestMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @pytest.mark.parametrize(" username, acctid, phone, result", [("aaa", 12345, 13711111111, "保存成功")])
    def test_addmemer(self, username, acctid, phone, result):
        getresult = self.main.goto_addmember_page().addusername(username).addacctid(acctid).addphone(
            phone).save_member().get_result_text()
        assert getresult == result
        namelist = self.main.goto_contact_page().get_mamberlist()
        assert username in namelist
