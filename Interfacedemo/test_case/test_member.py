# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2021/4/16 19:34
import allure
import pytest
import yaml

from Interfacedemo.api.member import Member


@allure.feature("成员模块")
class TestMember:
    def setup(self):
        self.member = Member()
        token_info = yaml.safe_load(open("config.yaml", encoding="utf-8"))
        department_corpsecret = self.member.base_jsonpath(token_info, "$..department_secret")[0]
        self.member.get_token(department_corpsecret)

    @allure.feature("添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name, userid", [("张三", "zhangsan")], ids={"添加成员"})
    def test_create_member(self, name, userid):
        r = self.member.create_member(name)
        backjson = {
            "errcode": 0,
            "errmsg": "created"
        }
        assert r == backjson
        memberdetail = self.member.get_memberdetail(userid)
        username = self.member.base_jsonpath(memberdetail, "$..name")[0]
        assert username == name

    @allure.feature("更新成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name, userid", [("张三1", "zhangsan")], ids={"更新成员"})
    def test_update_member(self, name, userid):
        r = self.member.update_member(name)
        backjson = {
            "errcode": 0,
            "errmsg": "updated"
        }
        assert r == backjson
        memberdetail = self.member.get_memberdetail(userid)
        username = self.member.base_jsonpath(memberdetail, "$..name")[0]
        assert username == name

    @allure.story("删除成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("userid,name,department_id", [("zhangsan", "张三1", 1)], ids={"删除成员"})
    def test_delete_member(self, userid, name, department_id):
        r = self.member.delete_member(userid)
        backjson = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        assert r == backjson
        department_member_list = self.member.get_department_member_list(department_id)
        department_member_name_list = self.member.base_jsonpath(department_member_list, "$..name")
        assert name not in department_member_name_list

    @allure.story("读取成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("userid", [("zhangsan")], ids={"读取成员"})
    def test_get_memberdetail(self, userid):
        # backjson = self.member.get_memberdetail(userid)
        # schemajson = json.load(open("./json_schema/get_memberdetail_schema.json", encoding="utf-8"))
        # self.member.base_jsonschema(backjson, schemajson)
        pass

    @allure.story("获取部门成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("userid", [("zhangsan")], ids={"获取部门成员"})
    def test_get_department_member_list(self, userid):
        # backjson = self.member.get_department_member_list()
        # schemajson = json.load(open("./json_schema/get_department_member_list_schema.json", encoding="utf-8"))
        # self.member.base_jsonschema(backjson, schemajson)
        pass
