#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/12/10 5:21 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import os
import multiprocessing
from multiprocessing import Manager

local_root_directory = '/root/auto_arrange_env/'


def get_local_app_directory(app_module, git_directory):
    """获取本地应用所在路径"""
    if (app_module == '') or (git_directory == ''):
        return local_root_directory
    else:
        return local_root_directory + app_module + git_directory


def check_git_pull_result_failed(result):
    # 默认git下载都是正常的False，当发现下载出现错误时，需要返回异常True
    line_list = result.readlines()
    for i in range(0, len(line_list)):
        if line_list[i].find('error') >= 0:
            # 当发现错误error信息时，返回异常
            return True
    return False


def git_clone_app(app_module, git_url, local_branch_tag=''):
    """从git上克隆指定应用到本地路径"""
    if (app_module == '') or (git_url == ''):
        return
    local_app_directory = local_root_directory + app_module + '/'
    os.system('rm -rf ' + local_app_directory)  # 删除本地仓库
    if (local_branch_tag == '') or (local_branch_tag == 'master'):
        # 如果分支为空或者是master，直接clone代码
        os.system('git clone ' + git_url + ' ' + local_app_directory)
    else:
        # 如果有分支信息，直接clone分支代码信息 克隆指定的分支：git clone -b 分支名 仓库地址 本地指定目录
        os.system('git clone -b ' + local_branch_tag + ' ' + git_url + ' ' + local_app_directory)


def pull_git_latest_info(app_module, app_git_url):
    """拉取git上最新代码"""
    local_app_directory = get_local_app_directory(app_module, '/')
    if os.path.exists(local_app_directory):
        # 更新最新代码，包括分支信息和tag，保证分支和tag信息完整
        result = os.popen('cd ' + local_app_directory + '\n' + 'git pull --force')  # 打开本地git代码目录,强制覆盖本地的分支
        # python调用Shell脚本，有两种方法：os.system()和os.popen(),前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容
        if check_git_pull_result_failed(result):
            # git更新失败时，需要删除git目录后重新clone代码
            git_clone_app(app_module, app_git_url)
        result.close()
    else:
        git_clone_app(app_module, app_git_url)


def get_git_url_branch_list(app_module):
    """获取git分支列表"""
    local_app_directory = get_local_app_directory(app_module, '/')
    # 首先同步一下远端所有的分支信息，保证和git上最新的分支信息一致
    os.system('cd ' + local_app_directory + '\n git remote update origin --prune')
    f = os.popen('cd ' + local_app_directory + '\n git branch -r')
    branch_list = f.readlines()
    default_branch_index = None
    for i in range(0, len(branch_list)):
        if branch_list[i].find('origin/HEAD') >= 0:
            default_branch_index = i
        else:
            branch_list[i] = branch_list[i].replace('\n', '').replace(' ', '')
    if default_branch_index is not None:
        # 去除重复的默认分支:origin/HEAD -> origin/master
        branch_list.pop(default_branch_index)
    f.close()
    return branch_list


def get_git_url_tag_list(app_module):
    """获取git上的tag列表"""
    local_app_directory = get_local_app_directory(app_module, '/')
    f = os.popen('cd ' + local_app_directory + '\n git tag')
    tag_list = f.readlines()
    for i in range(0, len(tag_list)):
        tag_list[i] = 'tag/' + tag_list[i].replace('\n', '')
    f.close()
    return tag_list


def worker(app_module_dict, return_dict):
    '''消费函数'''
    app_module = app_module_dict['app_module']
    app_git_url = app_module_dict['app_git_url']
    pull_git_latest_info(app_module, app_git_url)  # pull最新代码
    branch_list = get_git_url_branch_list(app_module)  # 获取git分支列表
    tag_list = get_git_url_tag_list(app_module)  # 获取git的标签；列表
    for i in range(0, len(tag_list)):
        branch_list.append(tag_list[i])
    if len(branch_list) == 0:
        # 如果没有分支信息，默认增加master分支
        branch_list.append('origin/master')
    return_dict[app_module] = branch_list


if __name__ == '__main__':
    app_module_list = [
        {"app_module": "AAA", "app_git_url": "git@192.168.1.1:dev/AAA.git"},
        {"app_module": "BBB", "app_git_url": "git@192.168.1.1:dev/BBB.git"},
        {"app_module": "CCC", "app_git_url": "git@192.168.1.1:dev/CCC.git"},
        {"app_module": "DDD", "app_git_url": "git@192.168.1.1:dev/DDD.git"},
        {"app_module": "EEE", "app_git_url": "git@192.168.1.1:dev/EEE.git"},
    ]
    manager = Manager()
    # return_list = manager.list() 也可以使用列表list
    return_dict = manager.dict()
    jobs = []
    for app_module in app_module_list:
        p = multiprocessing.Process(target=worker, args=(app_module, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    result_dict = dict(return_dict)
    print(result_dict)
