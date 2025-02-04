"""
今有丁一千八百六十五人人納絲一斤一十三兩一十七銖問絲幾何
術曰置丁數又以絲一斤二而八之為一十六兩内十三兩三而八之内一十七銖為七百一十三銖以乗丁數得一百三十二萬九千七百四十五銖以二十四銖為法除得五萬五千四百六兩一銖以一十六兩為法除得三千四百六十二斤一十四兩一銖
答曰絲 a斤
"""

"""
Suppose there are 1865 people, each contributing 1 jin, 13 liang, and 17 zhu of silk.
Question: how much silk is there in total?

The procedure says: Place the number of people.
Then take 1 jin as 16 liang, and 13 liang as 13 * 8 zhu (since 1 liang = 8 zhu), and add 17 zhu, resulting in 713 zhu.
Multiply this by the number of people, obtaining 1,329,745 zhu.
Take 24 zhu as the divisor (since 1 liang = 24 zhu), dividing to get 55,406 liang and 1 zhu.
Then take 16 liang as the divisor (since 1 jin = 16 liang), dividing to get 3,462 jin, 14 liang, and 1 zhu.

Answer: *a* jin.
"""

# 丁一千八百六十五人
丁數 = 1865

# 絲一斤一十三兩一十七銖
絲_斤 = 1
絲_兩 = 13
絲_銖 = 17

# 以絲一斤二而八之為一十六兩
一斤_兩 = 16

# 内十三兩三而八之
十三兩_銖 = 13 * 8

# 内一十七銖為七百一十三銖
總銖 = (絲_斤 * 一斤_兩 * 8) + 十三兩_銖 + 絲_銖

# 以乘丁數
總銖 *= 丁數

# 得一百三十二萬九千七百四十五銖
# 以二十四銖為法除
一兩_銖 = 24
總兩 = 總銖 // 一兩_銖
剩餘銖 = 總銖 % 一兩_銖

# 得五萬五千四百六兩一銖
# 以一十六兩為法除
一斤_兩 = 16
總斤 = 總兩 // 一斤_兩
剩餘兩 = 總兩 % 一斤_兩

# 答曰絲 a斤
a = f"{總斤}斤 {剩餘兩}兩 {剩餘銖}銖"
"""
Variable 'a' has wrong value. Expected: 1329745/384, Actual: 1209斤 5兩 9銖"""
