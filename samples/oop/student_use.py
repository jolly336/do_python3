#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类的使用
# @Time    : 2019/4/14 下午12:24
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 类的定义放在一个模块，类的使用放到另外一个模块
from student import Student

student1 = Student('Nelon', 20)
student2 = Student('Jolly', 21)
student3 = Student('xxx', 1)

# 查看实例内存地址
print(id(student1))
print(id(student2))
print(id(student3))
