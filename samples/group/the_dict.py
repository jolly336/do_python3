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


# 字典操作
# 根据键获取数据
x = {'name': '小白', 'age': 17}
r = x['name']
print('键为 name 的数据为', r)  # 输出：键为 name 的数据为 小白

# 新增数据
x = {'name': '小白', 'age': 17}
x['country'] = '中国'
print('新增数据后字典为', x)  # 输出：增数据后字典为 {'name': '小白', 'age': 17, 'country': '中国'}

# 修改数据
x = {'name': '小白', 'age': 17}
x['age'] = 27
print('键为 age 的数据修改后为', x['age'])  # 输出：键为 age 的数据修改后为 27

# 根据键删除数据
x = {'name': '小白', 'age': 17}
del x['age']
print('删除键为 age 的数据后，字典为', x)  # 输出：删除键为 age 的数据后，字典为 {'name': '小白'}

# 判断某个键是否在字典中
x = {'name': '小白', 'age': 17}
r = 'age' in x
print('判断键 age 是否在字典中，结果为', r)  # 输出：判断键 age 是否在字典中，结果为 True

# 获取字典长度
x = {'name': '小白', 'age': 17}
r = len(x)
print('字典长度为', r)  # 输出：字典长度为 2

# 获取字典的所有键
x = {'name': '小白', 'age': 17}
r = x.keys()
print('获取字典的所有键，结果为', r)  # 输出：获取字典的所有键，结果为 dict_keys(['name', 'age'])

# 获取字典的所有值
x = {'name': '小白', 'age': 17}
r = x.values()
print('获取字典的所有值，结果为', r)  # 输出：获取字典的所有值，结果为 dict_values(['小白', 17])

# 获取字典的所有键值对
x = {'name': '小白', 'age': 17}
r = x.items()
print('获取字典的所有键值对，结果为', r)  # 输出：获取字典的所有键值对，结果为 dict_items([('name', '小白'), ('age', 17)])

# 清空字典
x = {'name': '小白', 'age': 17}
x.clear()
print('清空后的字典为', x)  # 输出：清空后的字典为 {}
