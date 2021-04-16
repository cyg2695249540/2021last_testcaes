# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/16 14:29
import json

import requests
from jsonpath import jsonpath
from jsonschema import validate


class TestDepartment:
    def setup(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        self.token = r.json()["access_token"]

    def test_create_department(self):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post(url=create_url, json=data)
        backjson = {
            "errcode": 0,
            "errmsg": "created",
            "id": 2
        }
        assert r.json() == backjson
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentname = jsonpath(list, "$..department[?(@.id==2)].name")[0]
        assert departmentname == "技术部"

    def test_update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "name": "技术研发中心",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post(url=update_url, json=data)
        backjson = {
            "errcode": 0,
            "errmsg": "updated"
        }
        assert r.json() == backjson
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentname = jsonpath(list, "$..department[?(@.id==2)].name")[0]
        assert departmentname == "技术研发中心"

    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2"
        r = requests.get(url=delete_url)
        backjson = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        assert r.json() == backjson
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentlist = jsonpath(list, "$..id")
        assert 2 not in departmentlist

    def test_get_department_list(self):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        jsonschemalist = json.load(open("./json_schema/get_list_schema.json", encoding="utf-8"))
        validate(list, jsonschemalist)
