"""
今有官銀三千四百六十二斤一十四兩一銖充賞賜兵一千八百六十五人問人得幾何
術曰置銀斤以二而八之内一十四兩又三而八之内一銖得一百三十二萬九千七百四十五銖以兵數除之得七百一十三銖以二十四銖為法除之得二十九兩一十七銖以一十六兩為法除之得一斤一十三兩
答曰人得 a斤
"""

"""
Suppose there are 3462 jin, 14 liang, and 1 zhu of official silver to be distributed as rewards to 1865 soldiers.
Question: how much does each soldier receive?

The procedure says: Place the silver in jin. Multiply by 2 and then by 8, converting to liang. Add 14 liang.
Then multiply by 3 and then by 8, converting to zhu. Add 1 zhu.
This gives 1,329,745 zhu. Divide by the number of soldiers, obtaining 713 zhu.
Using 24 zhu as the divisor, divide to obtain 29 liang and 17 zhu.
Using 16 liang as the divisor, divide to obtain 1 jin and 13 liang.

Answer: each soldier receives *a* jin.
"""

from fractions import Fraction

# 官銀三千四百六十二斤一十四兩一銖
銀_斤 = 3462
銀_兩 = 14
銀_銖 = 1

# 置銀斤，以二而八之，內一十四兩
銀_兩 = 銀_兩 + 銀_斤 * 2 * 8

# 又三而八之，內一銖
銀_銖 = 銖 = 銖 + 銀_兩 * 3
"""
Code error: name '銖' is not defined"""
