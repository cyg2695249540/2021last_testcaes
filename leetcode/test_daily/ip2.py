# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : ip2.py
# @Author   : Pluto.
# @Time     : 2021/4/25 21:04
def ip():
    a = "192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.28?192.0.0.1"
    b = a.replace("?", "!").split("!")
    b = set(b)
    lista = []
    for i in b:
        if i != "":
            lista.append(i)
    listb = sorted(lista, key=lambda x: x[-1])
    print(listb)
    for i in listb:
        print(listb.index(i)+1,i)


if __name__ == '__main__':
    ip()
