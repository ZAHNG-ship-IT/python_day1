#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = 2
while (i < 100):
    j = 2;
    while (j < (i / j)):#j大于i的时候循环终止
        if not(i%j): break#在没有余数的情况下，终止
        j = j + 1
    if(j > i/j) : print(i,"是素数")#
    i = i + 1

print('再见')

####这里面的算数方法还没学会！！！！！

