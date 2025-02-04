"""
今有客歲作要與粟一百五十斛已與之粟先五十八日歸問折粟與粟各幾何
術曰置歸作日數以與粟乘之各自為實以一歲三百五十四日為法實如法得一
答曰折粟 a斛 與粟 b斛
"""

#----- content starts here -----
"""
Suppose last year, a contract was made to give 150 hu of millet. 
The millet was already given 58 days earlier than the agreed time.
Question: how much millet is considered as "discounted millet" (折粟), and how much millet is directly given (與粟)?

The procedure says: Place the number of days earlier than the agreed time (58 days).
Multiply it by the amount of millet to be given (150 hu). Each becomes its own dividend.
Take one year as 354 days as the divisor.
Perform the division, obtaining the amount of discounted millet (折粟).
Subtract the discounted millet from the total millet to get the directly given millet (與粟).

Answer: the discounted millet is *a* hu, and the directly given millet is *b* hu.
"""

# 粟一百五十斛
與粟總量 = 150

# 已與之粟先五十八日歸
提前日數 = 58

# 一歲三百五十四日
一年日數 = 354

# 置歸作日數以與粟乘之，各自為實
折粟實 = 提前日數 * 與粟總量

# 實如法得一
a = Fraction(折粟實, 一年日數)

# 與粟 = 總量 - 折粟
b = 與粟總量 - a#----- content ends here -----

"""
"""
