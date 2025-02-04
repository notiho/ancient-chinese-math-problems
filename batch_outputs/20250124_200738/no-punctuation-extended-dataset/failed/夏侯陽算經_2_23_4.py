"""
今有丁一千八百六十五人人納絲一斤一十三兩一十七銖問絲幾何
術曰置丁數又以絲一斤二而八之為一十六兩内十三兩三而八之内一十七銖為七百一十三銖以乗丁數得一百三十二萬九千七百四十五銖以二十四銖為法除得五萬五千四百六兩一銖以一十六兩為法除得三千四百六十二斤一十四兩一銖
答曰絲 a斤
"""

#----- content starts here -----
"""
Suppose there are 1865 people, each contributing 1 jin, 13 liang, and 17 zhu of silk.
Question: how much silk is there in total?

The procedure says: Place the number of people.
Then take 1 jin of silk, multiply it by 2 and add 8, making 16 liang.
Within that, take 13 liang, multiply it by 3 and add 8.
Within that, take 17 zhu, making 713 zhu.
Multiply this by the number of people, obtaining 1,329,745 zhu.
Using 24 zhu as the divisor, divide to obtain 55,406 liang and 1 zhu.
Using 16 liang as the divisor, divide to obtain 3,462 jin, 14 liang, and 1 zhu.

Answer: *a* jin.
"""

from fractions import Fraction

# 丁一千八百六十五人
丁數 = 1865

# 絲一斤
絲_斤 = 1

# 一斤二而八之為一十六兩
絲_兩 = 16

# 內十三兩
絲_內_兩 = 13

# 三而八之
絲_內_兩_銖 = 3 * 絲_內_兩 + 8

# 內一十七銖
絲_內_銖 = 17

# 為七百一十三銖
絲_銖 = 713

# 以乘丁數
總銖 = 絲_銖 * 丁數

# 得一百三十二萬九千七百四十五銖
assert 總銖 == 1329745

# 以二十四銖為法除
銖法 = 24
總兩 = 總銖 // 銖法
剩餘銖 = 總銖 % 銖法

# 得五萬五千四百六兩一銖
assert 總兩 == 55406
assert 剩餘銖 == 1

# 以一十六兩為法除
兩法 = 16
總斤 = 總兩 // 兩法
剩餘兩 = 總兩 % 兩法

# 得三千四百六十二斤一十四兩一銖
assert 総斤 == 3462
assert 剩餘兩 == 14

# 答
a = (總斤, 剩餘兩, 剩餘銖)#----- content ends here -----

"""
Code error: name '総斤' is not defined"""
