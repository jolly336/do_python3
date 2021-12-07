#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2021/12/7 3:25 下午
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
揭秘协程 20讲：https://time.geekbang.org/column/article/101855
"""

import time
import functools
import asyncio
import random


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print("函数 {} 运行耗时 {} 秒".format(func.__name__, end - start))
        return res

    return wrapper


if __name__ == '__main__':
    # 爬虫的例子
    print("---> 第一个示例：常规阻塞爬虫")


    def crawl_page(url):
        print("正在爬虫 {}".format(url))
        sleep_time = int(url.split('_')[-1])
        time.sleep(sleep_time)
        print("OK {}".format(url))


    @log_execution_time
    def main(urls):
        for url in urls:
            crawl_page(url)


    main(["url_1", "url_2", "url_3", "url_4"])

    print("---> 第二个示例：并发版爬虫，效果与上面一致")


    async def crawl_page2(url):
        print("正在爬虫 {}".format(url))
        sleep_time = int(url.split('_')[-1])
        await asyncio.sleep(sleep_time)
        print("OK {}".format(url))


    async def main2(urls):
        for url in urls:
            await crawl_page2(url)


    start = time.perf_counter()
    asyncio.run(main2(["url_1", "url_2", "url_3", "url_4"]))
    end = time.perf_counter()
    print("2 运行耗时 {} 秒".format(end - start))

    print("---> 第三个示例：真正的并发版爬虫")


    async def crawl_page3(url):
        print("正在爬虫 {}".format(url))
        sleep_time = int(url.split('_')[-1])
        await asyncio.sleep(sleep_time)
        print("OK {}".format(url))


    async def main3(urls):
        tasks = [asyncio.create_task(crawl_page3(url)) for url in urls]
        for task in tasks:
            await task


    start = time.perf_counter()
    asyncio.run(main3(["url_1", "url_2", "url_3", "url_4"]))
    end = time.perf_counter()
    print("3 运行耗时 {} 秒".format(end - start))

    print("---> 第四个示例：真正的并发版爬虫，task 的另一种做法 asyncio.gather(*tasks)")


    async def main4(urls):
        tasks = [asyncio.create_task(crawl_page3(url)) for url in urls]
        await asyncio.gather(*tasks)


    start = time.perf_counter()
    asyncio.run(main4(["url_1", "url_2", "url_3", "url_4"]))
    end = time.perf_counter()
    print("4 运行耗时 {} 秒".format(end - start))

    print("---> 第五个示例：协程运行底层")


    async def worker_1():
        print("work1 开始")
        await asyncio.sleep(1)
        print("work1 结束")


    async def worker_2():
        print("work2 开始")
        await asyncio.sleep(2)
        print("work2 结束")


    async def main5():
        print("await 之前")
        await worker_1()
        print("await worker_1 之后")
        await worker_2()
        print("await worker_2 之后")


    start = time.perf_counter()
    asyncio.run(main5())
    end = time.perf_counter()
    print("5 运行耗时 {} 秒".format(end - start))

    print("---> 第六个示例：协程运行底层")


    async def main6():
        task1 = asyncio.create_task(worker_1())
        task2 = asyncio.create_task(worker_2())
        print("await 之前")
        await task1
        print("await worker_1 之后")
        await task2
        print("await worker_2 之后")


    start = time.perf_counter()
    asyncio.run(main6())
    end = time.perf_counter()
    print("6 运行耗时 {} 秒".format(end - start))

    print("---> 第七个示例：限定时间，超出就取消，协程出现错误")


    async def worker1():
        await asyncio.sleep(1)
        return 1


    async def worker2():
        await asyncio.sleep(2)
        return 2 / 0


    async def worker3():
        await asyncio.sleep(3)
        return 3


    async def main7():
        task1 = asyncio.create_task(worker1())
        task2 = asyncio.create_task(worker2())
        task3 = asyncio.create_task(worker3())
        await asyncio.sleep(2)
        task3.cancel()
        res = await asyncio.gather(task1, task2, task3, return_exceptions=True)
        print(res)


    start = time.perf_counter()
    asyncio.run(main7())
    end = time.perf_counter()
    print("7 运行耗时 {} 秒".format(end - start))


    # 生产者消费者模型

    async def consumer(queue, id):
        while True:
            val = await queue.get()
            print("{} get a val: {}".format(id, val))
            await asyncio.sleep(1)


    async def producer(queue, id):
        for i in range(5):
            val = random.randint(1, 10)
            await queue.put(val)
            print("{} set a val: {}".format(id, val))
            await asyncio.sleep(1)


    async def main8():
        queue = asyncio.Queue()
        consumer1 = asyncio.create_task(consumer(queue, "consumer 1"))
        consumer2 = asyncio.create_task(consumer(queue, "consumer 2"))
        producer1 = asyncio.create_task(producer(queue, "producer 1"))
        producer2 = asyncio.create_task(producer(queue, "producer 2"))

        await asyncio.sleep(10)
        consumer1.cancel()
        consumer2.cancel()
        await asyncio.gather(consumer1, consumer2, producer1, producer2, return_exceptions=True)


    start = time.perf_counter()
    asyncio.run(main8())
    end = time.perf_counter()
    print("8 运行耗时 {} 秒".format(end - start))
