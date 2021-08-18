#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类-成员可见性
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
成员可见性：公开和私有

* 成员可见性 = 变量 + 方法可见性
* 之前章节的示例都是不安全的，所有成员和方法都可以在外部访问，造成类不安全
* 「编程提倡」：不要直接访问变量的方式直接做修改，对于类下面的方法都应该通过方法来更改，可以保护数据

为啥 Python 可以让双下划线 __init__ 方法外部访问？
-> 注意下，init 后面还有个 __，这不是私有。这是 Python 是想区别于其它，比如Python 内置的变量 __class__
"""


class Student():
    # 学生数量
    sum = 0

    # 构造函数
    # def __init__(self, name, age, score):
    #     self.name = name
    #     self.age = age
    #     # self.score = score  # 不安全，这种外部就可以随意更改
    #     self.__score = 0
    #     self.__class__.sum += 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.score = score  # 公开的 pubic：不安全，这种外部就可以随意更改
        self.__score = 0  # private，python 没有 public、private 关键字，通过加双下划线来表示私有
        self.__class__.sum += 1

    def do_homework(self):
        self.do_english_homework()  # 类内部调用
        print('homework')

    def do_english_homework(self):
        print()

    # def marking(self, score):  # 定义一个方法来打分，在方法里可以做安全判断
    #     if score < 0:
    #         return '不能够打负分'
    #     self.__score = score
    #     print(self.name + '同学考试分数为：' + str(self.__score))

    # 改成 private method，私有方法
    def __marking(self, score):  # 定义一个方法来打分，在方法里可以做安全判断
        if score < 0:
            return '不能够打负分'
        self.__score = score
        print(self.name + '同学考试分数为：' + str(self.__score))


student1 = Student('Nelson', 18)
student1.do_homework()  # 内外部调用
# student1.score = -1 # 外部可随意更改 score，造成类数据不安全
# 避免随意给成员变量赋值
# result = student1.marking(59)
result = student1.marking(-1)  # 改成私有方法报错了！AttributeError: 'Student' object has no attribute 'marking'
print(result)

# 为什么给方法添加双下滑下调用就报错，而实例变量添加调用不报错
student1.__score = -1
