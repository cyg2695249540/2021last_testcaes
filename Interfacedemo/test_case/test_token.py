# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_token.py
# @Author   : Pluto.
# @Time     : 2021/4/16 19:33
import allure
import pytest
import yaml

from Interfacedemo.api.base_api import BaseApi


def get_datas():
    datas = yaml.safe_load(open("../datas/datas.yaml", encoding="utf-8"))
    demo = datas["demo"]
    case = datas["case"]
    return demo, case


@allure.feature("获取token模块")
class TestToken:
    def setup_class(self):
        self.token = BaseApi()

    @allure.story("geteoken测试")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("corpid, department_secret, errmsg", get_datas()[0], ids=get_datas()[1])
    def test_get_token(self, corpid, department_secret, errmsg):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={department_secret}"
        req = {
            "method": "get",
            "url": get_token_url
        }
        r = self.token.send_and_requests(req)
        assert r.status_code == 200 and r.json()["errmsg"] == errmsg
