#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 函数-可变参数（序列解包）、关键字参数、默认参数
# @Time    : 2019/4/14 上午11:29
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 1. 必须参数

def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


# <class 'tuple'>
damages = damage(3, 6)
print(type(damages))
# error，根据序号获取返回结果
print(damages[0], damages[1])

# 序列解包-返回结果实际意义返回
skill1_damage, skill2_damage = damage(3, 6)
print(skill1_damage, skill2_damage)

# 序列解包

a = 1
b = 2
c = 3

a, b, c = 1, 2, 3
d = 1, 2, 3
print(type(d))

# 序列解包
a, b, c = d


# 2. 关键字参数

def add(x, y):
    result = x + y
    return result


c = add(y=3, x=2)
print(c)


# 3. 默认参数

def print_student_files(name, gender='男', age=20, college='人民路小学'):
    print("我叫" + name)
    print("我今年" + str(age) + '岁')
    print("我是" + gender + '生')
    print("我在" + college + '上学')


print_student_files('Nelson', '男', 20, '人民路小学')
print('---')
print_student_files('Daryl')

print('---')
print_student_files('Rocky', '女', 21)
# SyntaxError: positional argument follows keyword argument
# print_student_files('Rocky', gender='女', 17, college='光明小学')
