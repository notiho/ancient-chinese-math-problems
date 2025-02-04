"""
今有官銀三千四百六十二斤一十四兩一銖充賞賜兵一千八百六十五人問人得幾何
術曰置銀斤以二而八之内一十四兩又三而八之内一銖得一百三十二萬九千七百四十五銖以兵數除之得七百一十三銖以二十四銖為法除之得二十九兩一十七銖以一十六兩為法除之得一斤一十三兩
答曰人得 a斤
"""

"""
Suppose there are 3462 jin, 14 liang, and 1 zhu of official silver to be distributed as rewards to 1865 soldiers.
Question: how much does each soldier receive?

The procedure says: Take the silver in jin, multiply it by 2 and then by 8, and convert it into liang.
Add 14 liang, then multiply it by 3 and then by 8, and convert it into zhu.
Add 1 zhu, obtaining 1,329,745 zhu.
Divide this by the number of soldiers, obtaining 713 zhu.
Take 24 zhu as the divisor, divide it, obtaining 29 liang and 17 zhu.
Take 16 liang as the divisor, divide it, obtaining 1 jin and 13 liang.

The answer says: each soldier receives *a* jin.
"""

from fractions import Fraction

# 官銀三千四百六十二斤一十四兩一銖
銀斤 = 3462
銀兩 = 14
銀銖 = 1

# 置銀斤，以二而八之，内一十四兩
銀總銖 = 銀斤 * 2 * 8 * 24  # Convert jin to zhu
銀總銖 += 銀兩 * 24  # Add liang converted to zhu

# 又三而八之，内一銖
銀總銖 += 銀銖  # Add zhu

# 得一百三十二萬九千七百四十五銖
assert 銀總銖 == 1329745  # Verify total zhu

# 以兵數除之
兵數 = 1865
每人銖 = Fraction(銀總銖, 兵數)

# 得七百一十三銖
assert 每人銖 == 713  # Verify zhu per soldier

# 以二十四銖為法除之
每人兩 = 每人銖 // 24  # Convert zhu to liang
剩餘銖 = 每人銖 % 24

# 得二十九兩一十七銖
assert 每人兩 == 29 and 剩餘銖 == 17  # Verify liang and remaining zhu

# 以一十六兩為法除之
每人斤 = 每人兩 // 16  # Convert liang to jin
剩餘兩 = 每人兩 % 16

# 得一斤一十三兩
assert 每人斤 == 1 and 剩餘兩 == 13  # Verify jin and remaining liang

# 答曰人得 a斤
a = Fraction(每人斤) + Fraction(剩餘兩, 16) + Fraction(剩餘銖, 16 * 24)  # Final result in jin

"""
"""
