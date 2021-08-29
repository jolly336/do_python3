#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 对象存在并不一定是True
# @Time    : 2019/4/21 下午11:38
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
if a
if None

思考：虽然 a 和 None 是不相等的，但 if a 和 if None 走的分支确是一样的，这是为什么？

当我们做 if 判断时，对象都和 True、False 有对应关系
'''


# if a:
# if None

# '' 空字符串对应 False，非空字符串对应 True
# []
# None 永远对应 False
# 自定义对象

# 1. S
# class Test():
#     pass
#
# test = Test()
#
# if test:
#     # S
#     print('S')

class Test():
    # 内置函数，返回 0
    def __len__(self):
        return 0


test = Test()

print(bool(None))  # bool 真假判断
print(bool([]))
# test 自定义对象存在，bool(test) 不一定是 True，由 2个内置函数决定，__len__() 和 __bool()
print(bool(test))
# None
if test:
    print('S')
else:
    print('F')
