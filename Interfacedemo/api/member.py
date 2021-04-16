# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : member.py
# @Author   : Pluto.
# @Time     : 2021/4/16 19:33
from Interfacedemo.api.wework import WeWork


class Member(WeWork):
    def create_member(self, name):
        createmember_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "zhangsan",
            "name": name,
            "mobile": "13711111111",
            "department": [1]
        }
        req = {
            "method": "post",
            "url": createmember_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def update_member(self, name):
        update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "zhangsan",
            "name": name,
            "mobile": "13711111111",
            "department": [1]
        }
        req = {
            "method": "post",
            "url": update_member_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def delete_member(self, userid):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        req = {
            "method": "get",
            "url": delete_member_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_memberdetail(self, userid):
        get_memberdetail_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        req = {
            "method": "get",
            "url": get_memberdetail_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_department_member_list(self, department_id):
        get_department_member_list = f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={self.token}&department_id={department_id}"
        req = {
            "method": "get",
            "url": get_department_member_list
        }
        r = self.send_and_requests(req)
        return r.json()
