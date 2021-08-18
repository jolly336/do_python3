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

"""
没有什么是不能访问

student10.py 最后思考题：为什么给方法添加双下滑下调用就报错，而实例变量添加调用不报错
student1.__score = -1
"""


class Student():
    # 学生数量
    sum = 0

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1

    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        print()

    def marking(self, score):
        if score < 0:
            return '不能够打负分'
        self.__score = score
        print(self.name + '同学考试分数为：' + str(self.__score))


student1 = Student('Nelson', 18)
student2 = Student('Jolly', 18)

# 为什么给方法添加双下滑下调用就报错，而实例变量添加调用不报错
# 由于 __score 为私有，所以此时是给 student1 对象新添加了一个实例变量
student1.__score = -13
# Python 不能动态添加私有变量的！
print(student1.__score)  # 注意：Python 动态语言的特性，修改的不是我们实例里面的私有 __score 变量，而是新添加了一个 __score 变量！
# print(student2.__score) # 报错，AttributeError: 'Student' object has no attribute '__score'

# {'name': 'Nelson', 'age': 18, '_Student__score': 0, '__score': -1}
print(student1.__dict__)  # 查看实例变量，其中 __Student__score 是 Python 把 __score 更改为这个
# python 把私有变量名称修改为 _class__var 而阻止外部访问，可以看到 Python 私有机制是比较弱的
print(student1._Student__score)  # 读取被 Python 更改后的变量，严格来说 Python 是没有私有的。。。
# AttributeError: 'Student' object has no attribute '__score'
# print(student2.__score)
# {'name': 'Jolly', 'age': 18, '_Student__score': 0}
print(student2.__dict__)
