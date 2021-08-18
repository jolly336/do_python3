#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 集合 set 无序
# @Time    : 2019/2/26 下午11:44
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print(type({1, 2, 3, 4, 5, 6}))  # <class 'set'>
# 不支持切片！！！
# print({1, 2, 3, 4, 5, 6}[0]) # TypeError: 'set' object does not support indexing
# print({1, 2, 3, 4, 5, 6}[0:2]) # TypeError: 'set' object is not subscriptable

# 不重复
print({1, 1, 2, 2, 3, 3, 4, 4})

# 操作
print(len({1, 2, 3}))
print(1 in {1, 2, 3})
print(1 not in {1, 2, 3})
print([1, 2, 3][0])

# 去重：求2个set的差集
print({1, 2, 3, 4, 5, 6} - {3, 4})

# 交集
print({1, 2, 3, 4, 5, 6} & {3, 4})

# 并集：合并无重复
print({1, 2, 3, 4, 5, 6} | {3, 4, 7})

# 空集合

print(type({}))  # <class 'dict'>
print(type(set()))  # <class 'set'>
print(len(set()))  # <class 'set'>

# 创建空集合，并赋值给变量 data
data = set()  # 注意：{} 用于创建空字典，因此创建空集合不能用 {}

# 集合操作
# 添加数据
x = {0, 1, 2, 3, 4, 5}
x.add(6)
print('添加数据后集合为', x)  # 输出：添加数据后集合为 {0, 1, 2, 3, 4, 5, 6}

# 删除数据
x = {0, 1, 2, 3, 4, 5}
x.remove(3)
print('删除数据集合为', x)  # 输出：删除数据集合为 {0, 1, 2, 4, 5}

# 判断数据是否在集合中
x = {0, 1, 2, 3, 4, 5}
r = 2 in x
print('判断 2 是否在集合中，结果为', r)  # 输出：判断 2 是否在集合中，结果为 True

# 获取集合长度
x = {0, 1, 2, 3, 4, 5}
r = len(x)
print('集合长度为', r)  # 输出：集合长度为 6

# 获取集合中数据最大值
x = {0, 1, 2, 3, 4, 5}
r = max(x)
print('集合中数据最大值为', r)  # 输出：集合中数据最大值为 5

# 获取集合中数据最小值
x = {0, 1, 2, 3, 4, 5}
r = min(x)
print('集合中数据最小值为', r)  # 输出：集合中数据最小值为 0

# 清空集合
x = {0, 1, 2, 3, 4, 5}
x.clear()
print('清空后的集合为', x)  # 输出：清空后的集合为 set()
