#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/9/10 4:06 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import subprocess

# import commands


# def git(*args):
#     return subprocess.check_call(['git'] + list(args))
#
# print("结果---")
# # print(git("status"))

def git(*args):
    return subprocess.getoutput('git ' + str(args))
    # return commands.getstatusoutput(['git'] + list(args))

print("结果---")
branch = subprocess.getoutput('git rev-parse --abbrev-ref HEAD')
print("branch: " + branch)
if branch:
    origin_commitId = subprocess.getoutput('git rev-parse origin/%s' % branch)
    print("origin commitId: " + origin_commitId)
