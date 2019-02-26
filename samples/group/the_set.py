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
