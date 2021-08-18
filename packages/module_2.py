#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/8/15 6:14 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 引用 module_1.py 模块，使用其变量 a，使用命名空间使用变量 a
# 语法一：import
# import module_1
# print(module_1.a)

# 语法二：import as
# import subpackages.submodule_1 as sub
# print(sub.a)

# 语法三：避免命名空间命名太长的问题
# 不用再写 sub. 了，麻烦~
# from subpackages.submodule_1 import a
# print(a)

# 或者这样，import 后面也可以引入模块，其实和第二种方式没啥区别了
# from subpackages import submodule_1
# print(submodule_1.a)

# 语法四：「不推荐」一次导入，语义不明确
# 一次导入太多，怎么限制 * 导入的范围？可以去 sub_module_1.py 模块加个 __all__
# from subpackages.submodule_1 import *
# print(a)
# print(b)
# print(c) # NameError: name 'c' is not defined

# 语法五：import 加 , 分隔符，导入多个变量
# from subpackages.submodule_1 import a, b
# 多行换行导入，最后加入 \ 换行，或者使用括号，不要使用 \ 斜杠换行！
# from subpackages.submodule_1 import a, \
#     b

# 使用括号特性来换行
from subpackages.submodule_1 import (a,
                                     b)
print(a)
print(b)
