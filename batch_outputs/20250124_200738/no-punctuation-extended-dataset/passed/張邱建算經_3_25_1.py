"""
今有客歲作要與粟一百五十斛已與之粟先五十八日歸問折粟與粟各幾何
術曰置歸作日數以與粟乘之各自為實以一歲三百五十四日為法實如法得一
答曰折粟 a斛 與粟 b斛
"""

#----- content starts here -----
"""
Suppose last year, a contract was made to provide 150 hu of millet. 
The millet was already provided 58 days earlier than the agreed-upon date.
Question: how much millet is considered as "discounted millet" (折粟), and how much is the actual millet provided (與粟)?

The procedure says: Place the number of days provided earlier (58 days) and multiply it by the agreed millet amount (150 hu). 
Each becomes its own dividend.
Take one year as 354 days, which becomes the divisor.
Perform the division, and obtain the discounted millet (折粟).
Subtract the discounted millet from the agreed millet to get the actual millet provided (與粟).

Answer: the discounted millet is *a* hu, and the actual millet provided is *b* hu.
"""

# 與粟一百五十斛
與粟 = 150

# 先五十八日歸
提前日數 = 58

# 一歲三百五十四日
一年日數 = 354

# 置歸作日數以與粟乘之，各自為實
折粟實 = 提前日數 * 與粟

# 以一歲三百五十四日為法，實如法得一
a = Fraction(折粟實, 一年日數)

# 與粟 = 與粟 - 折粟
b = 與粟 - a#----- content ends here -----

"""
"""
