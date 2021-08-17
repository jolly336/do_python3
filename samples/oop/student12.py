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

"""
继承（Python 可多继承）

三大特性：继承性、封装性、多态性

继承性的作用：

* 避免定义重复的方法和变量
* 

Python 虽然可以一个模块可以写多个类，但是建议：一个模块只写一个类！
"""


class Student(Human):  # 括号里的是父类
    # 学生数量
    # sum = 0

    # 构造函数
    def __init__(self, school, name, age):
        self.school = school
        # 调用父类构造函数
        # TypeError: __init__() missing 1 required positional argument: 'age'
        # 为什么要传入 self 给父类？？-普通方法，通过类调用要传递 self，实例方法不需要
        # Human.__init__(name, age)
        # 「第一种」调用父类，用类调用实例方法
        # 不推荐！如果哪天修改了父类，所有使用的地方都要做修改！
        Human.__init__(self, name, age)  # 直接调用父类构造函数，一个类调用了 init 示例方法，面向对象角度理解是不正确的，

        # 「第二种」调用父类-推荐！
        super(Student, self).__init__(name, age)  #
        # self.name = name
        # self.age = age

    def do_homework(self):
        super(Student, self).do_homework()  # super 还可以使用在方法里
        print('child homework')


student1 = Student('人民路小学', 'Nelson', 18)
# print(student1.sum)
# print(Student.sum)
print(student1.name)
print(student1.age)

student1.do_homework()

# TypeError: do_homework() missing 1 required positional argument: 'self'
# Student.do_homework()
Student.do_homework(student1)  # what? 可以运行，直接使用类调用方法，需要传入 self 参数。完全多此一举，只为了演示！
# 随便传入''，不报错，可以执行
# Student.do_homework('')

# student1.get_name()
