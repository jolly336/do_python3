#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/11/25 11:31 上午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
Python 调用 shell 命令常用方法（4种）

https://cloud.tencent.com/developer/article/1737545

https://www.cnblogs.com/zhming26/p/6283361.html

subprocess.getstatusoutput() 仅适用于 Python 3.x

对于 Python 2.x，请使用 commands module

顺便提一下，请注意 getstatusoutput()相当于check_output(..., universal_newlines=True, stderr=STDOUT)（Python 2.x和3.x都有）。
'''

import os
import commands
import subprocess
import shlex

'''
法一：

使用os模块的system方法：os.system（cmd），其返回值是shell指令运行后返回的状态码，int类型，0表示shell指令成功执行，256表示未找到，
该方法适用于shell命令不需要输出内容的场景。
'''
val = os.system('ls -al')
print("os.system() return: {}".format(val))  # 0 表示 shell 执行成功，256 表示未找到

'''
法二：
使用 os.popen()，该方法以文件的形式返回 shell 指令运行后的结果，需要获取内容时可使用 read() 或 readlines() 方法，举例如下：
'''
val = os.popen('ls -al')
for temp in val.readlines():
    print("os.popen: {}".format(temp))

'''
方法三：

使用commands模块，有三个方法可以使用：

（1）commands.getstatusoutput(cmd)，其以字符串的形式返回的是输出结果和状态码，即（status,output）。

（2）commands.getoutput(cmd)，返回cmd的输出结果。

（3）commands.getstatus(file)，返回ls -l file的执行结果字符串，调用了getoutput，不建议使用此方法
'''

print("commands output start --> ")
# 注意：Python 3.x 上删除了 getstatusoutput ！！！
# AttributeError: module 'commands' has no attribute 'getstatusoutput'
(status, output) = commands.getstatusoutput("ls -l")
print("status: {}, output: {}".format(status, output))

output = commands.getoutput("ls -l")
print("output: {}".format(output))

status = commands.getstatus("bash --version")
print("status: {}".format(status))
print("<--- commands output end")

'''
方法四：
subprocess 模块，允许创建很多子进程，创建的时候能指定子进程和子进程的输入、输出、错误输出管道，执行后能获取输出结果和执行状态。

（1）subprocess.run()：python3.5中新增的函数， 执行指定的命令， 等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。

（2）subprocess.call()：执行指定的命令， 返回命令执行状态， 功能类似os.system（cmd）。

（3）subprocess.check_call()：python2.5中新增的函数, 执行指定的命令, 如果执行成功则返回状态码， 否则抛出异常。

说明：subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, universal_newlines=False)

　　 subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

　　 subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

　　 args：表示shell指令，若以字符串形式给出shell指令，如”ls -l “则需要使shell = Ture。否则默认已数组形式表示shell变量，如”ls”,”-l”。

　　 当使用比较复杂的shell语句时，可以先使用shlex模块的shlex.split()方法来帮助格式化命令，然后在传递给run()方法或Popen。
'''

print("subprocess output start --> ")
command = "ls -l"
args = shlex.split(command)
subprocess.Popen(args)

subprocess.call("ls -l", shell=True)

# 注意：Python 2.x 上没有 subprocess.getstatusoutput ！！！
# AttributeError: 'module' object has no attribute 'getstatusoutput'
(status, output) = subprocess.getstatusoutput("ls -l")
print("status: {}, output: {}".format(status, output))

print("subprocess output end --> ")
