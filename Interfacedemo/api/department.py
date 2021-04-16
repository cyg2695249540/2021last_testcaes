# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : department.py
# @Author   : Pluto.
# @Time     : 2021/4/16 19:33
from Interfacedemo.api.wework import WeWork


class Department(WeWork):
    def create_department(self, department_name, department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": department_name,
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        req = {
            "method": "post",
            "url": create_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def update_department(self, department_name, department_id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        date = {
            "name": department_name,
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        req = {
            "method": "post",
            "url": update_url,
            "json": date
        }
        r = self.send_and_requests(req)
        return r.json()

    def delete_department(self, department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        req = {
            "method": "get",
            "url": delete_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_department_list(self):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": get_department_list_url
        }
        r = self.send_and_requests(req)
        return r.json()
