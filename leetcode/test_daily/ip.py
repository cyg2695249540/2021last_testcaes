# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : ip.py
# @Author   : Pluto.
# @Time     : 2021/4/22 20:45
def ip(a):
    a = a.replace("?", "!").split("!")
    listb = []
    for i in a:
        if i != "":
            listb.append(i)
    listb = sorted(listb, key=lambda x: x[-1])
    print(listb)


if __name__ == '__main__':
    a = "192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.28?192.0.0.1"
    ip(a)
