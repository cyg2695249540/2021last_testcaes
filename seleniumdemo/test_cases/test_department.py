# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/29 11:18
import allure
import pytest
import yaml

from seleniumdemo.pages.main_page import MainPage


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    addepartment = datas["addepartment"]
    case1 = datas["case5"]
    addepartmentfail = datas["addepartmentfail"]
    case2 = datas["case6"]
    return addepartment, case1, addepartmentfail, case2


@allure.feature("部门模块")
class TestAddepartment:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    @allure.story("添加部门成功")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname", get_datas()[0], ids=get_datas()[1])
    def test_addepartment(self, departmentname):
        departmentnamelist = self.main.goto_contact_page().goto_addepartment_page().addepartment(
            departmentname).save_department().get_department_list()
        assert departmentname in departmentnamelist

    @allure.story("取消添加部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname", get_datas()[2], ids=get_datas()[3])
    def test_addepartment_cancel(self, departmentname):
        departmentnamelist = self.main.goto_contact_page().goto_addepartment_page().addepartment(
            departmentname).cancel_department().get_department_list()
        assert departmentname not in departmentnamelist
