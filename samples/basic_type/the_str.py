#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 字符串 单引号、双引号、三引号
# @Time    : 2019/2/26 下午10:35
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print('hello world')
print("hello world")

print(type(1))
print(type('1'))

# 引号表示字符串时要成对出现
print("Let's go!")  # 推荐双引号包含单引号
print('Let"s go!')
# 转义字符
print('Let\'s go!')

# python每行建议最大79个字符，超过要换行，三引号可以解决

print('''
hello world
hello world
hello world
''')

# 反斜杠 \n 表示回车
print("""
hello world
hello world
hello world
""")

# print函数可以解析字符串中间的转义字符 \n
print("""hello world\nhello world\nhello world""")
print('hello world\nhello world\nhello world')
print("hello world\nhello world\nhello world")

# 单引号双引号换行，使用 \ 可以敲击回车换行

# 转义字符
# \n \' \t \n换行 \r 回车

print('hello \\n world')
print('let \'s go')

print('c:\\northwind\\northwest')
# r原始字符串，「所见即所得」
print(r'c:\northwind\northwest')
# print(r'let 's go')

# 字符串操作 字符串运算

print("hello" + "world")
print("hello" * 3)
# print("hello" * "world") 只能和数字相乘

# 获取字符 角标
print("hello world"[0])  # h
print("hello world"[-1])  # d
print("hello world"[-3])  # r

print("hello world"[6])
print("hello world"[-5])

# 前闭后开 -1表示 「步长」
print("hello world"[0: 5])  # hello
print("hello world"[0: -1])  # hello worl
print("hello world"[0: -3])  # hello worl

print("hello world"[0: -3])  # hello wo
print("hello world"[6: 11])  # world
print("hello world"[6: 20])  # world
print("hello world"[6: 0])  # ''
# 步长为空，即截取后面所有字符
print("hello world"[6:])  # world
print("python java android php ruby"[6:])  # java android php ruby
print("python java android php ruby"[: -4])  # python java android php
# 负数在前面的意义：从字符串末尾开始数几个字符
print("python java android php ruby"[-4:])  # ruby

# 原始字符串
print(r'c:\windows')
print(R'c:\windows')
