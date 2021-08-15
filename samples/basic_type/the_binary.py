#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 进制转换：10进制、2进制、8进制、16进制
# @Time    : 2019-02-26 00:02
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


# 二进制
print(0b10)  # 2
print(0b11)  # 3

# 八进制
print(0o10)  # 8
print(0o11)  # 9

# 十六进制
print(0x10)  # 16
print(0x1F)  # 31

# 进制转换

# 十进制 -> 二进制
print(bin(10))  # 0b1010

# 八进制 -> 二进制
print(bin(0o7))  # 0b111

# 十六进制 -> 二进制
print(bin(0xE))  # 0b1110

# 二进制 -> 十进制
print(int(0b111))  # 7

# 八进制 -> 十进制
print(int(0o77))  # 63

# 十进制 -> 十六进制
print(hex(888))  # 0x378

# 八进制 -> 十六进制
print(hex(0o7777))  # 0xfff

# 二进制 -> 八进制
print(oct(0b111))  # 0o7

# 十六进制 -> 八进制
print(oct(0x777))  # 0o3567
