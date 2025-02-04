"""
今有丁一千八百六十五人人納絲一斤一十三兩一十七銖問絲幾何
術曰置丁數又以絲一斤二而八之為一十六兩内十三兩三而八之内一十七銖為七百一十三銖以乗丁數得一百三十二萬九千七百四十五銖以二十四銖為法除得五萬五千四百六兩一銖以一十六兩為法除得三千四百六十二斤一十四兩一銖
答曰絲 a斤
"""

#----- content starts here -----
"""
Suppose there are 1865 people, and each person contributes 1 jin, 13 liang, and 17 zhu of silk.
Question: how much silk is there in total?

The procedure says: Place the number of people.
Then take 1 jin as 16 liang, and 13 liang as 13 liang.
Take 1 liang as 24 zhu, and 17 zhu as 713 zhu.
Multiply by the number of people, obtaining 1,329,745 zhu.
Take 24 zhu as the divisor, dividing to get 55,406 liang and 1 zhu.
Take 16 liang as the divisor, dividing to get 3,462 jin, 14 liang, and 1 zhu.

Answer: the total silk is *a* jin.
"""

from fractions import Fraction

# 丁一千八百六十五人
丁數 = 1865

# 絲一斤二而八之為一十六兩
一斤 = 16  # 1 jin = 16 liang

# 内十三兩
十三兩 = 13

# 三而八之内一十七銖為七百一十三銖
一兩 = 24  # 1 liang = 24 zhu
一十七銖 = 17

# Convert 1 jin, 13 liang, and 17 zhu into zhu
絲每人總銖 = (一斤 * 一兩) + (十三兩 * 一兩) + 一十七銖

# 以乘丁數得總銖
總銖 = 丝每人總銖 * 丁數

# 以二十四銖為法除，得總兩
每兩銖 = 24
總兩 = 總銖 // 每兩銖
剩餘銖 = 總銖 % 每兩銖

# 以一十六兩為法除，得總斤
每斤兩 = 16
總斤 = 總兩 // 每斤兩
剩餘兩 = 總兩 % 每斤兩

# 結果
a = f"{總斤}斤 {剩餘兩}兩 {剩餘銖}銖"#----- content ends here -----

"""
Code error: name '丝每人總銖' is not defined"""
