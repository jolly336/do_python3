#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/12/8 3:10 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
并行-多进程执行，在 Python 是真正的并行执行，利用多核 CPU，区别于 Java

* [一篇文章搞定Python多进程(全)](https://zhuanlan.zhihu.com/p/64702600)
* [多进程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064)
* [How to keep track of status with multiprocessing and pool.map?](https://pretagteam.com/question/how-to-keep-track-of-status-with-multiprocessing-and-poolmap)
* [Is there a way for workers in multiprocessing.Pool's apply_async to catch errors and continue?](https://stackoverflow.com/questions/25148359/is-there-a-way-for-workers-in-multiprocessing-pools-apply-async-to-catch-errors)
"""

import multiprocessing
import time

print("core cpu: " + str(multiprocessing.cpu_count()))

a = 0


def myfun(i):
    time.sleep(1)
    global a
    a = 1 + 1
    print("a: {}, i: {}".format(a, i))
    return True


def make_log_result(results):
    def log_result(retVal):
        results.append(retVal)
        print("result: {}, results: {}".format(retVal, results))

    return log_result


def err_result(ret):
    print("error: {}".format(ret))


def main():
    t = time.time()
    pool = multiprocessing.Pool(10)
    results = []
    for i in range(10):
        pool.apply_async(func=myfun, args=(i,), callback=make_log_result(results))

    pool.close()
    pool.join()

    print("results: {}".format(results))

    if all(results):
        print("all success!")
    else:
        print("failed, result: {}".format(results))

    print("--> cost time: {}".format(time.time() - t))


if __name__ == '__main__':
    main()
