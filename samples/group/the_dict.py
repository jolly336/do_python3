#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 字典 dict {key:value} 无序
# @Time    : 2019/2/26 下午11:52
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print(type({1: 1, 2: 2, 3: 3}))  # <class 'dict'>

# 不支持下标
# {'Q': "新月打击", 'W': "苍白之瀑", 'E': "月之降临", 'R':"月神冲刺"}[0]

print({'Q': "新月打击", 'W': "苍白之瀑", 'E': "月之降临", 'R': "月神冲刺"}['Q'])

# 不能有重复的key，第二个覆盖第一个
print({'Q': "新月打击", 'Q': "苍白之瀑", 'E': "月之降临", 'R': "月神冲刺"}['Q'])  # 苍白之瀑

# key 可以任意数据类型 str int float list set dict
print({1: "新月打击", '1': "苍白之瀑", 'E': "月之降临", 'R': "月神冲刺"})

print({1: "新月打击", '1': "苍白之瀑", 'E': {1: 1}, 'R': "月神冲刺"})

# key：必须是不可变的数据类型  int str
# print({[1, 2]: "新月打击", '1': "苍白之瀑", 'E': {1: 1}, 'R': "月神冲刺"}) # TypeError: unhashable type: 'list'
print({(1, 2): "新月打击", '1': "苍白之瀑", 'E': {1: 1}, 'R': "月神冲刺"})

# 空字典
print({})
print(type({}))

