#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 类
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
内容：
* 类的定义
* 浅谈函数与方法的区别
* 构造函数
* 区别模块变量与类中的变量
"""

class Student():
    """
    1. 类的函数必须加 self 关键字，要使用类定义的变量，需要使用 self.xx 来引用
    2. 类的定义放在一个模块，类的使用放到另外一个模块

    方法和函数的区别？
    * C、C++ 函数
    * Java、C# 方法
    * 方法：设计层面，更多是面向对象层面，面向对象更关心的是设计，代码的设计封装；
    * 函数：程序运行、过程式的一种称谓，更多的是面向过程
    行为（方法）+ 特征

    构造函数：
    * 当实例化对象时，Python会自动调用 init 构造函数，不需要显示手动调用。
    * init 构造函数是可以手动调用的，但是不要自己调用，实例化会自动走的。
    * 手动调用 init 构造函数，返回来这个： <class 'NoneType'>

    初始化对象的属性
    类变量 vs 实例变量
    * 实例变量：self.name = name
    """

    # 类变量，不是实例变量，区别其他语言 Java
    name = ''  # 全局变量
    age = 0 # 数据变量，Python 把类的变量叫数据变量，模块里的叫变量

    # 构造函数
    def __init__(self , name, age): # def __init__(this , name, age): self 其实不是关键字，名字也可以换成 this 也行。推荐用 self
        print('student')
        # 构造函数不能返回字符串
        # return 'student'
        # return None 默认返回来这个，不能手动返回其他类型。有别于其他函数

        # 初始化对象的属性
        name = name
        age = age

    # 行为 与 特征：方法
    # 类的函数和在模块中写的普通函数是有区别的，必须强制加上 self 关键字
    # 思考：把 print_file 方法放到 Student 类合适吗？其实是不合适的，不属于 Student 类，应该单独键一个类 Printer 来打印
    def print_file(self):
        print('name: ' + self.name)  # 使用 self 关键字引用实例变量
        print('age: ' + str(self.age))

    def do_homework(self):
        print('homework')

    # 类只负责定义，不负责执行，调用要放到外部！
    # TypeError: print_file() missing 1 required positional argument: 'self'
    # print_file()


# 调用放到外部
# student = Student()
# student.print_file()

# 显示调用构造函数，默认返回 None
student = Student('Nelson', 18)
print(student.name)


# a = student.__init__()
# print(a)
# 手动调用 init 构造函数，返回来这个： <class 'NoneType'>
# print(type(a))


# 思考：把 print_file 方法放到 Student 类合适吗？其实是不合适的，不属于 Student 类，应该单独键一个类 Printer 来打印
# Printer 类只是为了演示把 print_file 从 Student 拿出来，打印行为主体不应该属于学生，是属于打印机的。
# （行为需要找对主体！！！）
class Printer():
    # 打印应该不属于Student，而应属于打印机
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))
