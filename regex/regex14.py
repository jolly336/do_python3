#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : group分组
# @Time    : 2019/4/14 下午6:08
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

"""
group分组

s = 'life is short,i use python, i love python'
问题：提取 life 和 python 之间的字符串

和爬虫很像，我们爬取 html 时，要的是标签中间的内容，不包括标签本身，标签没有太大意义。

"""

# search 与 match 一般用得少，findall 好用一点

s = 'life is short,i use python, i love python'

# 问题：截取life和python之间的字符串
# r = re.search('life\wpython', s) # 错：\w 单词字符，不包含空格
# r = re.search('life\w*python', s) # 错：\w* 重复 0或者无限个字符
r = re.search('life.*python', s)
print(r.group())

r = re.search('(life.*python)', s)  # 默认有一个圆括号，默认分组，我们可以加也可以不加
print(r.group(0))  # group(0) 是个比较特殊的情况，永远返回完整匹配结果

r = re.search('life(.*)python', s)
print(r.group(1))  # 要访问完整匹配结果的内部某个分组，需要从 1开始访问

# findall比较方便，建议使用findall！！！
r = re.findall('life(.*)python', s)
print(r)

# 再加了一个 i love python，找到中间所有数据，再加了一个分组
r = re.search('life(.*)python(.*)python', s)
print(r.group(0))
print(r.group(1))
print(r.group(2))

# 以元组返回所有数据
# ('life is short,i use python, i love python', ' is short,i use ', ', i love ')
print(r.group(0, 1, 2))  # 一种快捷写法，不用上面 r.group(0) r.group(1) r.group(2) 这种分别写法
# (' is short,i use ', ', i love ')
print(r.groups())  # r.groups() 没有完整的了，只返回匹配最后结果
