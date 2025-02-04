"""
今有官銀三千四百六十二斤一十四兩一銖充賞賜兵一千八百六十五人問人得幾何
術曰置銀斤以二而八之内一十四兩又三而八之内一銖得一百三十二萬九千七百四十五銖以兵數除之得七百一十三銖以二十四銖為法除之得二十九兩一十七銖以一十六兩為法除之得一斤一十三兩
答曰人得 a斤
"""

#----- content starts here -----
"""
Suppose there are 3462 jin, 14 liang, and 1 zhu of official silver to be distributed as rewards to 1865 soldiers.
Question: how much does each soldier receive?

The procedure says: Place the silver in jin. Multiply by 2 and then by 8 to convert to liang. Add 14 liang.
Then multiply by 3 and then by 8 to convert to zhu. Add 1 zhu.
This gives 1,329,745 zhu. Divide by the number of soldiers, obtaining 713 zhu.
Take 24 zhu as the divisor and divide, obtaining 29 liang and 17 zhu.
Take 16 liang as the divisor and divide, obtaining 1 jin and 13 liang.

Answer: each soldier receives *a* jin.
"""

# 官銀三千四百六十二斤一十四兩一銖
銀斤 = 3462
銀兩 = 14
銀銖 = 1

# 置銀斤，以二而八之，內一十四兩
銀兩 += 銀斤 * 2 * 8

# 又三而八之，內一銖
銀銖 += 銀兩 * 3 * 8

# 得一百三十二萬九千七百四十五銖
總銖 = 銀銖

# 以兵數除之
兵數 = 1865
每人銖 = Fraction(總銖, 兵數)

# 得七百一十三銖
每人銖整數 = 每人銖.numerator // 每人銖.denominator

# 以二十四銖為法除之，得二十九兩一十七銖
每人兩 = 每人銖整數 // 24
剩餘銖 = 每人銖整數 % 24

# 以一十六兩為法除之，得一斤一十三兩
每人斤 = 每人兩 // 16
剩餘兩 = 每人兩 % 16

# 答案
a = Fraction(每人斤) + Fraction(剩餘兩, 16) + Fraction(剩餘銖, 16 * 24)#----- content ends here -----

"""
"""
