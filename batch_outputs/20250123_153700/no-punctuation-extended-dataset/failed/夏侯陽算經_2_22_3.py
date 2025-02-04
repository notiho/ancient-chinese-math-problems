"""
今有戸五百六十五戸别納絲一斤一十一兩八銖問得絲幾何
術曰置户數下列二十七兩以二十四銖乗之内八銖為六百五十六銖以乗戸數得三十七萬六百四十銖以二十四銖為法除得一萬五千四百四十三兩零八銖以一十六兩為法除得九百六十五斤三兩以三十斤為法除得三十二鈞五斤三兩以四鈞為法除得八石五斤三兩八銖
答曰 a石
"""

"""
Suppose there are 565 households, each contributing 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is collected in total?

The procedure says:
Place the number of households. Below, list 27 liang. Multiply it by 24 zhu. Within, 8 zhu is 656 zhu.
Multiply this by the number of households, obtaining 370,640 zhu.
Use 24 zhu as the divisor, dividing to get 15,443 liang and 8 zhu.
Use 16 liang as the divisor, dividing to get 965 jin and 3 liang.
Use 30 jin as the divisor, dividing to get 32 jun, 5 jin, and 3 liang.
Use 4 jun as the divisor, dividing to get 8 shi, 5 jin, 3 liang, and 8 zhu.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶納絲 1斤11兩8銖
每戶絲_斤 = 1
每戶絲_兩 = 11
每戶絲_銖 = 8

# 置户數，下列二十七兩
每戶絲_總兩 = 16 * 每戶絲_斤 + 每戶絲_兩  # 1斤 = 16兩
每戶絲_總銖 = 24 * 每戶絲_總兩 + 每戶絲_銖  # 1兩 = 24銖

# 以乘戶數，得總銖
總銖 = 每戶絲_總銖 * 戶數

# 以二十四銖為法除，得總兩
總兩 = 總銖 // 24
剩餘銖 = 總銖 % 24

# 以一十六兩為法除，得總斤
總斤 = 總兩 // 16
剩餘兩 = 總兩 % 16

# 以三十斤為法除，得總鈞
總鈞 = 總斤 // 30
剩餘斤 = 總斤 % 30

# 以四鈞為法除，得總石
總石 = 總鈞 // 4
剩餘鈞 = 總鈞 % 4

# 答案
a = 總石  # 石
b = 剩餘鈞  # 鈞
c = 剩餘斤  # 斤
d = 剩餘兩  # 兩
e = 剩餘銖  # 銖
"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
