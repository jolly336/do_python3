#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : for 循环，比for循环更好的是「切片」！
# @Time    : 2019/4/13 下午7:11
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 主要是用来遍历/循环 序列或集合、字典
# 1. for
a = ['apple', 'orange', 'banana', 'grape']
for x in a:
    print(x)

# 2. for-else
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y, end='')
else:
    # 当for遍历结束完执行 else 语句块
    print('fruit is gone')

# 3. break-continue
a = [1, 2, 3]
for x in a:
    if x == 2:
        # break
        continue
    print(x)
else:
    # break 时，不会执行else，非正常迭代完成
    print('EOF')

# 4. for(i=0; i<10; i++)
# range 生成0-9序列 [0,10)，第三个参数为步长
for x in range(0, 10, 2):
    print(x, end=' | ')

# 递减等差数列
for x in range(10, 0, -2):
    print(x, end=' | ')

# 5. 打印出相间隔数字
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(a), 2):
    print(a[i], end=' | ')

# 比for循环更好的，切片!!!
b = a[0:len(a):2]
print(b)
