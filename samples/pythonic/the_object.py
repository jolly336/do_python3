#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 对象存在并不一定是True
# @Time    : 2019/4/21 下午11:38
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# if a:
# if None

# ''
# []
# None 永远对应False
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
    def __len__(self):
        return 0


test = Test()

print(bool(None))
print(bool([]))
print(bool(test))
# None
if test:
    print('S')
else:
    print('F')
