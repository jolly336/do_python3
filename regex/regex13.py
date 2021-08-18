#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : search与match函数
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

# search与match一般用得少，findall好用一点

a = 'A8C3721D86'
# match从首字母开始找，找不到就返回None
r = re.match('\d', a)
# None
print(r)
# search搜索整个字符串，找到就返回
r1 = re.search('\d', a)
# <_sre.SRE_Match object; span=(1, 2), match='8'>
print(r1)
print(r1.group())
print(r1.span())

# match与search一旦找到结果，就立即返回，不会继续寻找；findall会全部寻找
r3 = re.findall('\d', a)
print(r3)


# Q：2个数为一组，凡是大于50的替换为100，小于50的替换为0
def convert(value):
    pass


r = re.sub('\d', convert, a)
print(r)
