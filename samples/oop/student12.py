#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-没有什么不能访问
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

from human import Human


class Student(Human):
    # 学生数量
    # sum = 0

    # 构造函数
    def __init__(self, school, name, age):
        self.school = school
        # 调用父类构造函数
        # TypeError: __init__() missing 1 required positional argument: 'age'
        # 为什么要传入self给父类？？-普通方法，通过类调用要传递self，实例方法不需要
        # Human.__init__(name, age)
        # 「第一种」调用父类
        Human.__init__(self, name, age)

        # 「第二种」调用父类
        super(Student, self).__init__(name, age)
        # self.name = name
        # self.age = age

    def do_homework(self):
        super(Student, self).do_homework()
        print('child homework')


student1 = Student('人民路小学', 'Nelson', 18)
# print(student1.sum)
# print(Student.sum)
print(student1.name)
print(student1.age)

student1.do_homework()

# TypeError: do_homework() missing 1 required positional argument: 'self'
# Student.do_homework()
# 随便传入''，不报错，可以执行
# Student.do_homework('')

# student1.get_name()
