#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 概括字符集
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
概括字符集

* \d 就是概括字符集，表示所有数字

# 思考：为什么 Python 把匹配结果拆分成一个个的字母？
# 不管字符集还是概括字符集，都是只能匹配单一的字母或者字符，准确的说是字符。
"""

# \d \D
# \w 单词字符
# \W 非单词字符，包括像换行、回车、制表符等
# \s 空白字符，像换行、回车、制表符等
# \S 非空白字符
# . 匹配除换行符\n之外其他所有字符

s = 'python 1111java&___678\nph\rp'

r = re.findall('\d', s)  # 使用概括字符集来匹配
# r = re.findall('[0-9]]', s)  # 使用字符集来匹配，和上面效果一样
print(r)

r = re.findall('[^0-9]', s)
print(r)

# 匹配字母和数字-两者都要匹配 \w
r = re.findall('\w', s)  # \w 单词字符 = [A-Za-z0-9_]，概括字符集用 \w 就可以代替 [A-Za-z0-9_]
r = re.findall('[A-Za-z0-9_]]', s)
print(r)  # ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', '&', '_', '_', '_', '\n', 'p', 'h', 'p']
# 思考：为什么 Python 把匹配结果拆分成一个个的字母？
# 不管字符集还是概括字符集，都是只能匹配单一的字母或者字符，准确的说是字符。

r = re.findall('\W', s)  # \W 匹配非单词字符 [' ', '&', '\n', '\r']
print(r)

r = re.findall('\s', s)  # \s 空白字符 [' ', '\n', '\r']，结果不包括 &，& 不属于空白字符！！
print(r)
