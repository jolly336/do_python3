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
# 由于__score为私有，所以此时是给student1对象新添加了一个实例变量
student1.__score = -1
print(student1.__score)
# python把私有变量名称修改为 _class__var 而阻止外部访问
print(student1._Student__score)
# {'name': 'Nelson', 'age': 18, '_Student__score': 0, '__score': -1}
print(student1.__dict__)
# AttributeError: 'Student' object has no attribute '__score'
# print(student2.__score)
# {'name': 'Jolly', 'age': 18, '_Student__score': 0}
print(student2.__dict__)
