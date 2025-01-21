"""
今有戸五百六十五戸别納絲一斤一十一兩八銖問得絲幾何
術曰置户數下列二十七兩以二十四銖乗之内八銖為六百五十六銖以乗戸數得三十七萬六百四十銖以二十四銖為法除得一萬五千四百四十三兩零八銖以一十六兩為法除得九百六十五斤三兩以三十斤為法除得三十二鈞五斤三兩以四鈞為法除得八石五斤三兩八銖
答曰 a石
"""

"""
Suppose there are 565 households, each contributing 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is obtained in total?

The procedure says:
Place the number of households. Below, place 27 liang.
Multiply by 24 zhu. Include 8 zhu, making 656 zhu.
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

# 每戶納絲 1斤 11兩 8銖
絲_斤 = 1
絲_兩 = 11
絲_銖 = 8

# 置户數，下列二十七兩
兩 = 16  # 1斤 = 16兩
銖 = 24  # 1兩 = 24銖
總銖 = (絲_斤 * 兩 + 絲_兩) * 銖 + 絲_銖  # 將 1斤11兩8銖轉換為銖
總銖 *= 戶數  # 乘以戶數

# 以二十四銖為法除，得總兩
總兩 = Fraction(總銖, 銖)

# 以一十六兩為法除，得總斤
總斤 = Fraction(總兩, 兩)

# 以三十斤為法除，得總鈞
總鈞 = Fraction(總斤, 30)

# 以四鈞為法除，得總石
總石 = Fraction(總鈞, 4)

# 答案
a = int(總石)  # 取整數部分作為石數

"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
