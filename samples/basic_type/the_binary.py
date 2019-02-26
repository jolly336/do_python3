#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 进制转换：10进制、2进制、8进制、16进制
# @Time    : 2019-02-26 00:02
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


# 二进制
print(0b10)
print(0b11)

# 八进制
print(0o10)
print(0o11)

# 十六进制
print(0x10)
print(0x1F)

# 进制转换

# 十进制 -> 二进制
print(bin(10))

# 八进制 -> 二进制
print(bin(0o7))

# 十六进制 -> 二进制
print(bin(0xE))


# 二进制 -> 十进制
print(int(0b111))

# 八进制 -> 十进制
print(int(0o77))

# 十进制 -> 十六进制
print(hex(888))

# 八进制 -> 十六进制
print(hex(0o7777))


# 二进制 -> 八进制
print(oct(0b111))

# 十六进制 -> 八进制
print(oct(0x777))