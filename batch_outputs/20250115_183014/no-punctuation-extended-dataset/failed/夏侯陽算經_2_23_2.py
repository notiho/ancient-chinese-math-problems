"""
今有丁一千八百六十五人人納絲一斤一十三兩一十七銖問絲幾何
術曰置丁數又以絲一斤二而八之為一十六兩内十三兩三而八之内一十七銖為七百一十三銖以乗丁數得一百三十二萬九千七百四十五銖以二十四銖為法除得五萬五千四百六兩一銖以一十六兩為法除得三千四百六十二斤一十四兩一銖
答曰絲 a斤
"""

"""
Suppose there are 1865 people, each contributing 1 jin, 13 liang, and 17 zhu of silk.
Question: how much silk is there in total?

The procedure says: Place the number of people.
Then take 1 jin of silk, multiply it by 2 and add 8, making 16 liang.
Within the 13 liang, multiply by 3 and add 8.
Within the 17 zhu, multiply by 713.
Multiply this by the number of people, obtaining 1,329,745 zhu.
Using 24 zhu as the divisor, divide to get 55,406 liang and 1 zhu.
Using 16 liang as the divisor, divide to get 3,462 jin, 14 liang, and 1 zhu.

Answer: the silk is *a* jin.
"""

from fractions import Fraction

# 丁一千八百六十五人
丁數 = 1865

# 絲一斤二而八之為一十六兩
一斤 = 16  # 1 jin = 16 liang

# 内十三兩三而八之
十三兩 = 13

# 内一十七銖為七百一十三銖
一銖 = Fraction(1, 713)  # 1 zhu = 1/713 of a jin

# 計算每人絲的總量 (以銖為單位)
每人絲 = (1 * 一斤) + 十三兩 + (17 * 一銖)

# 以乘丁數
總絲銖 = 每人絲 * 丁數

# 以二十四銖為法除，得總量 (以兩為單位)
一兩 = 24 * 一銖  # 1 liang = 24 zhu
總絲兩 = 總絲銖 / 一兩

# 以一十六兩為法除，得總量 (以斤為單位)
一斤 = 16  # 1 jin = 16 liang
總絲斤 = 總絲兩 / 一斤

# 分解為斤、兩、銖
a = int(總絲斤)  # 取整數部分為斤
剩餘兩 = (總絲斤 - a) * 一斤
b = int(剩餘兩)  # 取整數部分為兩
剩餘銖 = (剩餘兩 - b) * 一兩
c = round(剩餘銖)  # 取整數部分為銖

# 答案
a斤 = a
b兩 = b
c銖 = c
"""
Variable 'a' has wrong value. Expected: 1329745/384, Actual: 100506"""
