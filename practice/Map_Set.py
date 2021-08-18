#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 字典、集合，你真的了解吗？
# @Time    : 2019/10/14 下午12:58
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import time

d = {'b': 1, 'a': 2, 'c': 10}

d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
print(d_sorted_by_key)

d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
print(d_sorted_by_value)

s = {3, 4, 2, 1}
print(sorted(s))


# 1.比如电商企业的后台，存储了每件产品的 ID、名称和价格。现在需求是，给定某件商品的 ID，找出其价格。

# 「列表」使用列表来存储进行查找，时间复杂度：O(n)，即使使用二分查找，也会需要 O(logn) 时间复杂度，列表的排序还需要 O(nlogn) 的时间。
def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None


products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150)
]

print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))

# 「字典」使用字典存储，时间复杂度：O(1)
products = {
    143121312: 100,
    432314553: 30,
    32421912367: 150
}
print('The price of product 432314553 is {}'.format(products[432314553]))


# 2.需求：找出这些商品有多少种不同的价格
# 「列表」，其中 A 和 B 是两层循环，在最差情况下，需要 O(n^2) 时间复杂度
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products: # A
        if price not in unique_price_list: # B
            unique_price_list.append(price)
    return len(unique_price_list)


products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150)
]

print('number of unique price is: {}'.format(find_unique_price_using_list(products)))


# 「集合」set version，集合是高度优化的哈希表，里面元素不能重复，并且其添加和查找操作只需 O(1) 的复杂度，那么总的时间复杂度就只有 O(n)
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_set(products)))

# 初始化含有 100,000 个元素的产品，并分别计算了使用列表和集合来统计产品价格数量的运行时间
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))
## 输出
# time elapse using list: 41.61519479751587

# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
# 输出
# time elapse using set: 0.008238077163696289

