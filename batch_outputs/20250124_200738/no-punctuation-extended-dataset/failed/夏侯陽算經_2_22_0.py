"""
今有戸五百六十五戸别納絲一斤一十一兩八銖問得絲幾何
術曰置户數下列二十七兩以二十四銖乗之内八銖為六百五十六銖以乗戸數得三十七萬六百四十銖以二十四銖為法除得一萬五千四百四十三兩零八銖以一十六兩為法除得九百六十五斤三兩以三十斤為法除得三十二鈞五斤三兩以四鈞為法除得八石五斤三兩八銖
答曰 a石
"""

#----- content starts here -----
"""
Suppose there are 565 households, each contributing 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is obtained in total?

The procedure says:
1. Place the number of households.
2. Below, list 27 liang, and multiply it by 24 zhu.
3. Add 8 zhu, resulting in 656 zhu.
4. Multiply this by the number of households, obtaining 370,640 zhu.
5. Divide by 24 zhu (as the divisor), obtaining 15,443 liang and 8 zhu.
6. Divide by 16 liang (as the divisor), obtaining 965 jin and 3 liang.
7. Divide by 30 jin (as the divisor), obtaining 32 jun, 5 jin, and 3 liang.
8. Divide by 4 jun (as the divisor), obtaining 8 shi, 5 jin, 3 liang, and 8 zhu.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶納絲 1斤 11兩 8銖
每戶絲_斤 = 1
每戶絲_兩 = 11
每戶絲_銖 = 8

# 1斤 = 16兩, 1兩 = 24銖
每戶絲_總銖 = (每戶絲_斤 * 16 * 24) + (每戶絲_兩 * 24) + 每戶絲_銖

# 總銖數
總銖 = 每戶絲_總銖 * 戶數

# 以24銖為法除，得總兩數
總兩 = 總銖 // 24
剩餘銖 = 總銖 % 24

# 以16兩為法除，得總斤數
總斤 = 總兩 // 16
剩餘兩 = 總兩 % 16

# 以30斤為法除，得總鈞數
總鈞 = 總斤 // 30
剩餘斤 = 總斤 % 30

# 以4鈞為法除，得總石數
總石 = 總鈞 // 4
剩餘鈞 = 總鈞 % 4

# 答案
a = 總石
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
