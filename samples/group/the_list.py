#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 列表 [ ]
# @Time    : 2019/2/26 下午11:14
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print(type([1, 2, 3, 4, 5, 6]))
print(type(["hello", 1, 9]))
print(["hello", 1, 9, True, False])
# 嵌套列表 「二维数组」<class 'list'>
print(type([[1, 2], [3, 4], [True, False]]))

lol = ["新月打击", "苍白之瀑", "月之降临", "月神冲刺"]
print(lol[0])
print(lol[3])
# 和字符串操作类型，字符串截取
print(lol[0:2])  # ['新月打击', '苍白之瀑']
print(lol[-1:])  # ['月神冲刺']

# 追加技能

talent = ["点燃", "虚弱"]
print(lol + talent)
# print(lol * talent) # TypeError: can't multiply sequence by non-int of type 'list'
print(talent * 3)
# 列表不支持减号
# print(talent - ["点燃"]) # TypeError: unsupported operand type(s) for -: 'list' and 'list'

# 列表标识世界杯分组情况 - 嵌套列表
[['巴西', '克罗地亚', '墨西哥', '喀麦隆'], [], [], [], [], [], [], [], []] # 映射到Python中


