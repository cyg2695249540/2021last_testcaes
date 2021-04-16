# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token.py
# @Author   : Pluto.
# @Time     : 2021/4/16 8:58
import allure
import pytest
import requests


@allure.feature("获取access_token模块")
class TestGetToken:
    @allure.story("获取通讯录模块token")
    @pytest.mark.parametrize("corpid, corpsecret,errmsg",
                             [("ww0ae123b953d2b956", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "ok"),
                              ("", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "corpid missing"),
                              ("ww0ae123b953d2b956", "", "corpsecret missing")],
                             ids={"正确的corpid和corpsecret", "缺少corpid", "缺少corpsecret"})
    def test_get_token(self, corpid, corpsecret, errmsg):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=get_token_url)
        assert r.json()["errmsg"] == errmsg
