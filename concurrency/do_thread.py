#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/12/7 6:24 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


"""

多线程-并发，Python 同一时刻只有一个任务在执行，区别于其它语言， Java

* [21 | Python并发编程之Futures](https://time.geekbang.org/column/article/102562)
* [python多线程基础](https://zhuanlan.zhihu.com/p/34004179)
* [多线程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017629247922688)
"""

import time
import threading
import multiprocessing


# # 1. 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 2. Lock-多线程操作一个数据会造成 race condition，分别演示下不加锁和加锁

# # 2.1 不加锁
# # 假定这是你的银行存款:
# balance = 0
#
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(2000000):
#         change_it(n)
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# # 2.2 加锁，性能会受影响，甚至可能会产生死锁
#
# # 假定这是你的银行存款:
# balance = 0
#
# lock = threading.Lock()
#
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 3. 多核 CPU-跑起来查看 CPU 只占用了 101%？
# Python 的多线程不能利用多核，有 GIL 存在，所以同一时刻只能有一个线程在执行任务
# GIL锁：Global Interpreter Lock

def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
