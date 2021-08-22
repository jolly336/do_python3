#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 闭包的误区
# @Time    : 2019/4/21 下午3:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""

* 闭包的意义？

现场，返回不单单是函数，还有函数的变量，不然回受外部变量的影响。
单一函数不能绝对运行结果的，还需要环境变量。


* 使用闭包注意点
一个事例看看闭包

* 闭包的经典误区

"""


# 闭包 = 函数 + 环境变量(函数定义时候)
# 现场

# 1 使用闭包注意点
def f1():
    a = 10

    def f2():
        # a 此时被 Python 认为局部变量
        a = 20
        print(a)  # 10，f2() 内部 a 不会影响外部变量

    print(a)  # 10
    f2()
    print(a)  # 20


# 10 20 10
f1()


# 2 验证下这个是不是闭包？
def f1():
    a = 10

    def f2():
        a = 20
        print(a)

    return f2


f = f1()
# <function f1.<locals>.f2 at 0x102a4d6a8>
print(f)
print(f.__closure__)  # None 为什么？没有闭包属性？？？


# 3 去掉 a 内部赋值，再次验证下闭包？
def f1():
    a = 10

    def f2():
        # a 被 Python 认为是一个局部变量
        # a = 20 # 不要给 a 赋值了。# 由于局部变量 a 的存在，f2 就不会引用外部环境变量的 a，a 此时会被认为局部变量。这时闭包是不存在的
        print(a)  # 误区：注意这里要引用外部的环境变量 a 的

    return f2


f = f1()
# <function f1.<locals>.f2 at 0x102a4d6a8>
print(f)
# (<cell at 0x1005602e8: int object at 0x10028bd40>,)
print(f.__closure__)
