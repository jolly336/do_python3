#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : pythonic与Python杂记
# @Time    : 2019/4/21 下午7:29
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
 用字典代替 switch

 函数式编程：key 对应的 value 是个函数，类似 C++ 的函数指针

 switch (day)
 {
    case 0:
        dayName = "Sunday";
        break;
    case 1:
        dayName = "Monday";
        break;
    default:
        dayName = "Unknown";
        break;
 }
'''

day = 6
switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}

# Python 变量使用下划线
# day_name = switcher[day]
day_name = switcher.get(day, 'Unknow')
print(day_name)


# 函数式编程，key 对应的 value 是个函数

def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknow'


day = 2
switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}

day_name = switcher.get(day, get_default)()
print(day_name)
