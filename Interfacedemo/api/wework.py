# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2021/4/16 19:33
import requests

from Interfacedemo.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self, corpsecret):
        corpid = "ww0ae123b953d2b956"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        self.token = r.json()["access_token"]
        return self.token
