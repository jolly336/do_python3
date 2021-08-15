#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 函数-可变参数（序列解包）、关键字参数、默认参数
# @Time    : 2019/4/14 上午11:29
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
参数：
1. 必须参数 add(2, 3)
2. 关键字参数 c = add(y=3, x=2)，明确告诉 Python 实参是给哪个形参赋值
3. 默认参数 print_student_files(name, gender='男', age=20, college='人民路小学')
'''


# 1. 必须参数

def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


# <class 'tuple'>
damages = damage(3, 6)
print(type(damages))
# error，根据序号获取返回结果这种写法很不好，时间一长就不知道 [0]代表乐啥。拒绝使用元组角标来解包！！！
# 建议：直接用多个变量来接收结果，序列解包
print(damages[0], damages[1])

# 序列解包-返回结果实际意义返回
skill1_damage, skill2_damage = damage(3, 6)
print(skill1_damage, skill2_damage)

# 序列解包

a = 1
b = 2
c = 3

# 简洁写法，上面 3行可简写这一行代码
a, b, c = 1, 2, 3
d = 1, 2, 3  # tuple，用一个变量接收三个数值
print(type(d))

# 序列解包-什么是序列解包？用三个变量来接收 d
a, b, c = d

a = 1
b = 1
c = 1

a, b, c = 1, 1, 1
a = b = c = 1  # 链式调用
print(a, b, c)

# 2. 关键字参数

def add(x, y):
    result = x + y
    return result


c = add(y=3, x=2)
print(c)


# 3. 默认参数
# 必须参数必须在默认参数前面！！！
def print_student_files(name, gender='男', age=20, college='人民路小学'):
    print("我叫 " + name)
    print("我今年 " + str(age) + '岁') # int age 不能和字符串相加，必须 str(age) 转一下
    print("我是 " + gender + '生')
    print("我在 " + college + '上学')


print_student_files('Nelson', '男', 20, '人民路小学')
print('---')
print_student_files('Daryl')

print('---')
print_student_files('Rocky', '女', 21)
# SyntaxError: positional argument follows keyword argument
# print_student_files('Rocky', gender='女', 17, college='光明小学') # 默认参数和必须参数混着用，错误！必须参数必须在前面
print_student_files('Rocky', gender='女', age=17, college='光明小学')
