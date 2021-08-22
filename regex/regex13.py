#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : search与match函数
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
search与match函数

re 模块下还有 2个函数，search 和 match，一般用得少，没有 findAll 好用！！！

问题：2个数为一组，凡是大于50的替换为100，小于50的替换为0

"""

# search 与 match 一般用得少，findall 好用一点

a = 'A8C3721D86'

# match 从「首字母」开始找，找不到就返回 None
r = re.match('\d', a)
print(r)  # None 没有匹配到结果

# search 「搜索整个字符串」，找到就返回
r1 = re.search('\d', a)

print(r1)  # <_sre.SRE_Match object; span=(1, 2), match='8'> 匹配到一个结果
print(r1.group())  # group 读取返回结果
print(r1.span())  # 返回匹配字符串在原字符串中的位置

# 注意：match 与 search 一旦找到结果，就立即返回，不会继续寻找；findall 会全部寻找
r3 = re.findall('\d', a)
print(r3)


# Q：2个数为一组，凡是大于50的替换为100，小于50的替换为0
def convert(value):
    pass


r = re.sub('\d', convert, a)
print(r)
