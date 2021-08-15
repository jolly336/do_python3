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
[['巴西', '克罗地亚', '墨西哥', '喀麦隆'], [], [], [], [], [], [], [], []]  # 映射到Python中

# https://www.cnblogs.com/jingqueyimu/p/15110455.html?utm_source=tuicool&utm_medium=referral
# 创建空列表，并赋值给变量 data
data = []
print(data)

# 创建名字列表，并赋值给变量 names
names = ['小白', '小黑', 'Tom', 'Jerry']
print(names)

# 列表操作

# 根据索引获取列表中的数据
x = [0, 1, 2, 3, 4, 5]
r = x[1]
print('索引 1 的数据为', r)  # 输出：索引 1 的数据为 1

# 根据索引修改列表中的数据
x = [0, 1, 2, 3, 4, 5]
x[1] = 3
print('索引 1 的数据修改后为', x[1])  # 输出：索引 1 的数据修改后为 3

# 根据索引删除列表中的数据
x = [0, 1, 2, 3, 4, 5]
del x[1]
print('删除索引 1 的数据后，列表为', x)  # 输出：删除索引 1 的数据后，列表为 [0, 2, 3, 4, 5]

# 列表拼接
r = [0, 1, 2] + [3, 4, 5]
print('列表拼接结果为', r)  # 输出：列表拼接结果为 [0, 1, 2, 3, 4, 5]

# 列表截取
x = [0, 1, 2, 3, 4, 5]
r = x[0:4]
print('从索引 0 到 4 截取列表，结果为', r)  # 输出：从索引 0 到 4 截取列表，结果为 [0, 1, 2, 3]

# 判断数据是否在列表中
x = [0, 1, 2, 3, 4, 5]
r = 2 in x
print('判断 2 是否在列表中，结果为', r)  # 输出：判断 2 是否在列表中，结果为 True

# 获取列表长度
x = [0, 1, 2, 3, 4, 5]
r = len(x)
print('列表长度为', r)  # 输出：列表长度为 6

# 获取列表中数据最大值
x = [0, 1, 2, 3, 4, 5]
r = max(x)
print('列表中数据最大值为', r)  # 输出：列表中数据最大值为 5

# 获取列表中数据最小值
x = [0, 1, 2, 3, 4, 5]
r = min(x)
print('列表中数据最小值为', r)  # 输出：列表中数据最小值为 0

# 在列表末尾添加新数据
x = [0, 1, 2, 3, 4, 5]
x.append(6)
print('在列表末尾添加新数据后，列表为', x)  # 输出：在列表末尾添加新数据后，列表为 [0, 1, 2, 3, 4, 5, 6]

# 删除列表中第一个匹配数据
x = [0, 1, 2, 3, 4, 5]
x.remove(2)
print('删除列表中第一个匹配数据后，列表为', x)  # 输出：删除列表中第一个匹配数据后，列表为 [0, 1, 3, 4, 5]

# 列表排序
x = [3, 1, 4, 2, 5, 0]
x.sort()
print('排序后的列表为', x)  # 输出：排序后的列表为 [0, 1, 2, 3, 4, 5]

# 清空列表
x = [0, 1, 2, 3, 4, 5]
x.clear()
print('清空后的列表为', x)  # 输出：清空后的列表为 []
