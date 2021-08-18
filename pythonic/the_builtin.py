#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : __len__与__bool__内置方法（自定义对象）
# @Time    : 2019/4/21 下午11:43
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


class Test():
    # 1
    # pass

    # 2 内置2个方法
    def __bool__(self):
        print('bool called')
        return False

    def __len__(self):
        # return 0
        # return '8'
        print('len called')
        return True

    # python2 方法，绝对对象bool取值
    # python3 使用__bool__和__len__方法取值
    def __nonzero__(self):
        pass


# 1. bool 不出现时，由len方法决定
# False
print(bool(Test()))

# 2. 我们调用bool()方法，其实内部是调用了内部len方法
# 3. len()方法也会触发调用内部len方法

print(len(Test()))

# 4. bool方法存在时，由bool方法决定返回值



