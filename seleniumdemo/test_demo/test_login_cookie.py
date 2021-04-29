# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_login_cookie.py
# @Author   : Pluto.
# @Time     : 2021/4/29 9:22
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get(url="https://work.weixin.qq.com/wework_admin/frame")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'R7m1EkOVdk-TSdJb_ZIHF-t1thIZeuo6jnmcGi4MeFVphWQYRmyy2uyz-ZVQiLPbrUg1Rj39NeckB4y2FP0CcR26npuBOnkGcrKcDKS6uYNwd0OZTTMGnQ3JkTgtSaFL9kim7rSiZOx_-u_2oz3zBnI1yZAx0Ntzn8UnsrwkHW2JX5WmLgQk21gXASw3FOyn3g5MTI29ph3AWoIH0NHqk05PhvT53BksBCsoc6iX0yth1av8Z9AxNfo-uu0pN7GvIzX1_8dZbA2MiZfvYKxdfQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/',
             'secure': True, 'value': '1615866554'},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '0_e29f78a9450a4'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324964157309'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': False,
                             'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
                             'value': '1619442941'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'wwrtx.cs_ind',
             'path': '/', 'secure': True, 'value': ''},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': True,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': 'work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '1dedh5p'},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '4715055819'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
             'secure': True, 'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'eDFCKFCe06cak8OFW0Dwq3d_QIZQNqrv8bPGuj6dKJaXnD90J53FpGsYr5wUbOr7'},
            {'domain': '.qq.com', 'expiry': 1619745513, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1595137090.1619356099'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': True, 'name': 'wwrtx.refid',
             'path': '/', 'secure': True, 'value': '03529572'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1619442437'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1682731113, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1292933409.1618303525'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1622251117.102701, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': 'd6137915366d508b82a6fd128aa0470c85c76b2fdbc05a4eec00d7e699ac43e0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3646679'},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'SMKc+mma2P'},
            {'domain': '.qq.com', 'expiry': 2250224435, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/',
             'secure': True, 'value': '3452354556991474700'}]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get(url="https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("C:/Users/uiui/Desktop/txl.xlsx")
        assert "txl.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text