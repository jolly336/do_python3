#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/11/25 11:23 上午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
Python 调用 shell 脚本

python do_shell.py jolly nelson
'''

import os
import sys

if (len(sys.argv) < 3):
    print("please input two arguments")
    sys.exit(1)

arg0 = sys.argv[1]  # argv[0] is .py file
arg1 = sys.argv[2]

os.system('./hello.sh ' + arg0 + ' ' + arg1)
