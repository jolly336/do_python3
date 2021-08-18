#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 条件控制 if
# @Time    : 2019/4/7 下午11:07
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
    条件控制 循环控制 分支
    if else for while switch
    选择性问题
'''

mood = True

# 1.if-else
# Python 不能混淆、压缩
# 云服务，自己的服务器，代码托管在自己的服务器上，压缩和加密显得不那么重要！
# 商业授权（桌面应用程序）桌面应用需要加密，不然别人能看到代码！

# if 不止是变量，还可以表达式
if mood:
    print('go to left')
    # print('back away')
else:
    print('go to right')

# 2.用户登录

# python constant 没有常量，一般常量要大写
ACCOUNT = 'qiyue'
PASSWORD = '123456'

# Python 使用下划线来连接2个单词

print('please input account')
user_account = input()
print('please input password')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print('success')
else:
    print('fail')

# 3.snippet 片段

# 4.pass 空语句/占位语句

if True:
    pass

# 5.if-elif-else

a = input()
# 输入1，表明 a 接受到的是字符串，动态语言没有具体类型
print(type(a))  # <class 'str'>
a = int(a)
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
else:
    print('shopping')

# 6.如何写出优雅的代码？

# a 和 b 不能同时为False
a = 1
b = 0

# if condition:
#     pass
# else:
#     pass

# 不要用 or 只做boolean运算结果，也可以返回数值
# a or b
