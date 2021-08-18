#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-Python机制
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

"""
类与对象的变量查找顺序

思考：init 打印 print(age) 是啥结果？
"""
class Student():
    name = 'qiyue'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        name = name
        age = age
        # self.name = name # 先把 self.name 隐藏，验证 Python 访问变量顺序是咋样的
        # self.age = age

    def do_homework(self):
        print('homework')


student = Student('Nelson', 18)
# 实例变量，当在实例变量找不到，就会去类里面找，找不到再去父类里找
print(student.name) # qiyue
# 类变量
print(Student.name) # qiyue

# 先来看看，实例内部到底没有没有实例变量 name ?
# 使用对象隐藏的属性 __dict__
# 字典，保存当前对象下所有变量
print(student.__dict__) # {} 空字典
print(Student.__dict__) # {'__module__': '__main__', 'name': 'qiyue', 'age': 0, '__init__': <function Student.__init__ at 0x10535d950>, 'do_homework': <function Student.do_homework at 0x105385048>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
