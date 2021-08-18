#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数量词
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
数量词

内容：[字符集]{数量词}

不加数量词，匹配出现的是一个个的字符，加上数量词出来就是一个个单词

"""

s = 'python 1111java&___678\nphp'

# 问题：把 s 字符串里的所有单词都匹配出来

r = re.findall('[a-z]', s)
print(r)  # ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'p', 'h', 'p'] 结果不是一个一个单词出现的

# []{} 数量词
r = re.findall('[a-z]{3}', s)  # [字符集]{数量词}，匹配 a-z 的数量，这里是匹配 3个 a-z 的字符
print(r)

r = re.findall('[a-z]{3,6}', s)  # 范围：{3,6}，最小3，最大6。['python', 'java', 'php']
# 思考：我们设置 3,6 的范围，按理匹配到 pyt 已经够了这个范围，为啥最后会返回来完整的 python？
# 这个涉及到贪婪与非贪婪的问题了！
print(r)
