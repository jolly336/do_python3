#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 边界匹配
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
边界匹配符 ^$

比如：r = re.findall('^\d{4,8}$', qq)  # 匹配 9位 QQ 号，发现没匹配出来 []，边界符的作用：让正则表达式匹配完整的字符串

[字符集]{数量词}? 加了问号变成非贪婪

"""

# qq = '100001'
# qq = '101'
qq = '100000001'

# 问题：验证 QQ 号是否符合要求，要求：QQ 号要求是在 4-8 位之间

# 4~8位之间
r = re.findall('\d{4,8}', qq)
# 这种是可以匹配出来 8位 QQ 号，但是 QQ号是 9位，也会匹配出现前 8位，是不对的！
# 或者拿匹配出来的结果来原来的 QQ 号做判断，看是否相等！这种不优雅！
# 这时候可以给正则匹配加上边界即可 ^\d{4,8}$
print(r)  # ['10000000']

# 边界匹配，匹配完整字符串
r = re.findall('^\d{4,8}$', qq)  # 匹配 9位 QQ 号，发现没匹配出来 []，边界符的作用：让正则表达式匹配完整的字符串
print(r)

r = re.findall('000', qq)  # ['000', '000']，3个零为一组，匹配出现 2组
print(r)

r = re.findall('^000', qq)  # []
print(r)

r = re.findall('000$', qq)  # []
print(r)
