#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : while、for 循环-解决问题的一个模式（循环、穷举）
# @Time    : 2019/4/13 下午7:04
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# while 循环

# CONDITION = True
# while CONDITION:
#     print("I am while")

# 递归算法用 while 合适点，其它使用 for
counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else:
    # 当 while 遍历结束完执行 else 语句块
    print("EOF")
