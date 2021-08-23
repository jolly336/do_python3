#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 闭包-是一种辅助的编程方式
# @Time    : 2019/4/21 下午3:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""

* 闭包到底有啥用？

让代码精简，让你代码架构更加合理，辅助的编程方式。或者就像 类一样，没有类，没有 oop，你也可以写。

闭包是思维方式的不同，函数式编程

* 出个题，用闭包解决

问题：有个旅行者 x,y，不断计算出旅行者位置，起点 x = 0

思路：

- 我先用非闭包解决一下
- 闭包

* 小谈函数式编程

- 类似 JavaScript，我们直接在模块外部调用函数内部变量肯定是不行的，但是通过闭包来调用内部函数，内部函数使用了内部局部变量，相当于间接调用了函数内局部变量
- 容易造成内存泄漏，服务器还好，但是在 JavaScript 操作浏览器的时候，由于环境变量是常驻内存的，非常消耗内存，容易引起浏览器的卡顿，缓慢！！！

我们都是命令式编程，还是没理解函数式编程。
旅行者这个问题，不使用闭包，使用类变量也可以解决；

* 函数式编程建议

- 如果你习惯使用函数式编程，你用没有问题，Python 和 JavaScript 对闭包都有一定的支持；
- 但你不熟悉这样的思维，千万不要去赶潮流，函数式编程很早就有了，你可以使用面向对象主流思想来完成；

> 注意：不推荐在业务代码里大量使用闭包，如果你要写包、框架、类库的话，你可以使用闭包。

* 误区
闭包 不等于 函数式编程
闭包只是函数式编程的一种应用，一种体现
"""

# 闭包 = 函数 + 环境变量(函数定义时候)
# 现场

# 旅行者 x,y，不断计算出旅行者位置

# x = 0
# 3 result = 3 # 旅行者走了 3步，结果打印 3
# 5 result = 8 # 旅行者再走 5步，结果打印 8，而不是 5
# 6 result = 14 # 14步，8 + 6 = 14

# 关键点：每次调用函数时候需要保存上次函数调用结果状态！

'''
我先用非闭包解决一下
'''

# 1. 一个错误误区
# origin = 0
#
# def go(step):
#     # UnboundLocalError: local variable 'origin' referenced before assignment
#     new_pos = origin + step # origin 局部找不到，就去外部一层层找，模块里找
#     # origin被赋值，认为局部变量
#     origin = new_pos # Python 认为 origin 是局部变量
#     return origin
#
# print(go(2))
# print(go(3))
# print(go(6))

# 2. global 设置全局变量
# 全局变量被函数修改，函数没发保证自封闭性，容易受另外一个函数影响，这个函数的意义就没有了。
origin = 0


def go(step):
    global origin  # 让 origin 不是局部变量，是全局变量
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))
print(go(6))

# 3. 闭包实现

# 闭包可以保存环境变量的状态，记忆上次调用的状态
# 闭包所有的修改都局限在方法的内部，而 global 会修改全局变量，很糟糕
# 闭包的环境变量需要常驻内存，会容易引起内存泄漏

origin = 0


# 可以利用闭包实现工厂模式
def factory(pos):  # pos 当前旅行者处于的位置
    def go(step):
        # 声明不是局部变量
        nonlocal pos  # 闭包环境会记忆上次的状态
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


tourist = factory(origin)
print(tourist(2))
print(origin)
print(tourist.__closure__[0].cell_contents)  # 打印闭包环境变量 pos
print(tourist(3))
print(origin)
print(tourist.__closure__[0].cell_contents)
print(tourist(5))
print(origin)
print(tourist.__closure__[0].cell_contents)
