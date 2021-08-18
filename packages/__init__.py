#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 包下要有 __init__.py文件，否则就认为普通文件夹
# @Time    : 2019/4/13 下午9:39
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# __init__.py的模块名为当前的包名

# 导入公共模块，方便其他模块导入时，重复导入

'''
问题：__init__.py 什么时候执行？
当一个包被导入时，__init__.py 将被首先执行。Python 会自动执行的

问题：__init__.py 具体的应用场景？
* 第一个作用：里面设置 __all__ 属性，限制导包，具体看 module_2.py 和 module_3.py 示例
* 第二个作用：
'''
