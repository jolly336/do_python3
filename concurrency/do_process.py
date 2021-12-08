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
* [multiprocessing.Pool: When to use apply, apply_async or map?](https://newbedev.com/multiprocessing-pool-when-to-use-apply-apply-async-or-map)
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
    # 模拟在这里抛出异常，pool.apply_async() 不获取 get() 拿不到异常信息！
    # raise IOError("error occur")
    return True


def make_log_result(results):
    """
    使用 callback 来监听进程执行结果，可以做进度监听或者结果判断！
    :param results:
    :return:
    """

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
    futures = []
    for i in range(10):
        # apply_sync的结果就是异步获取func的返回值
        result = pool.apply_async(func=myfun, args=(i,), callback=make_log_result(results))
        # result.get() # 方式一：这句话能获取到函数里抛出错误，阻塞的？
        futures.append(result)  # 方式二：列表存起来 future，待会遍历获取结果

    pool.close()
    pool.join()

    # close 和 join 之后获取结果
    # 参考：https://www.cnblogs.com/konglinqingfeng/p/9699947.html
    for future in futures:
        print(future.get())  # 获取结果，如果有异常，会返回来异常

    print("results: {}".format(results))

    # 方式三：通过 callback 收集结果，最后打印
    if all(results):
        print("all success!")
    else:
        print("failed, result: {}".format(results))

    print("--> cost time: {}".format(time.time() - t))

    # 使用 map
    # TODO: https://newbedev.com/multiprocessing-pool-when-to-use-apply-apply-async-or-map


if __name__ == '__main__':
    main()
