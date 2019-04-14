#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-如何在实例变量中操作类变量
# @Time    : 2019/4/14 下午12:14
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类最基本的作用：封装
# 类和对象

# 类：首字母大写，驼峰式命名
# 类是个模块，可以生成各种不同对象
class Student():
    # 学生数量
    sum = 0

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print('当前班级学生总数为：' + str(self.__class__.sum))
        print(self.__class__.sum)

    def do_homework(self):
        print('homework')


student1 = Student('Nelson', 18)
student2 = Student('Nelson', 18)
student3 = Student('Nelson', 18)
