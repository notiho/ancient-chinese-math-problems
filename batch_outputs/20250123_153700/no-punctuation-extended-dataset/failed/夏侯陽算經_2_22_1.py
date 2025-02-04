"""
今有戸五百六十五戸别納絲一斤一十一兩八銖問得絲幾何
術曰置户數下列二十七兩以二十四銖乗之内八銖為六百五十六銖以乗戸數得三十七萬六百四十銖以二十四銖為法除得一萬五千四百四十三兩零八銖以一十六兩為法除得九百六十五斤三兩以三十斤為法除得三十二鈞五斤三兩以四鈞為法除得八石五斤三兩八銖
答曰 a石
"""

"""
Suppose there are 565 households, each contributing 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is obtained in total?

The procedure says:
Place the number of households.
Below, list 27 liang, and multiply it by 24 zhu.
Within, 8 zhu is treated as 656 zhu.
Multiply this by the number of households, obtaining 370,640 zhu.
Divide by 24 zhu (the divisor), obtaining 15,443 liang and 8 zhu.
Divide by 16 liang (the divisor), obtaining 965 jin and 3 liang.
Divide by 30 jin (the divisor), obtaining 32 jun, 5 jin, and 3 liang.
Divide by 4 jun (the divisor), obtaining 8 shi, 5 jin, 3 liang, and 8 zhu.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 列 1 斤 11 兩 8 銖
斤 = 1
兩 = 11
銖 = 8

# 轉換成銖：1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (斤 * 16 * 24) + (兩 * 24) + 銖

# 乘以戶數
總銖 *= 戶數

# 以 24 銖為法除，得總兩和餘銖
總兩 = 總銖 // 24
餘銖 = 總銖 % 24

# 以 16 兩為法除，得總斤和餘兩
總斤 = 總兩 // 16
餘兩 = 總兩 % 16

# 以 30 斤為法除，得總鈞和餘斤
總鈞 = 總斤 // 30
餘斤 = 總斤 % 30

# 以 4 鈞為法除，得總石和餘鈞
總石 = 總鈞 // 4
餘鈞 = 總鈞 % 4

# 最終答案
a = 總石
"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
