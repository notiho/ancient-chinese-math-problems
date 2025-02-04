"""
今有客歲作要與粟一百五十斛已與之粟先五十八日歸問折粟與粟各幾何
術曰置歸作日數以與粟乘之各自為實以一歲三百五十四日為法實如法得一
答曰折粟 a斛 與粟 b斛
"""

#----- content starts here -----
"""
Suppose last year, an agreement was made to give 150 hu of millet. 
The millet was already given 58 days earlier than the agreed time.
Question: how much millet is considered as "discounted millet" (折粟), and how much millet is actually given (與粟)?

The procedure says: Place the number of days given earlier (58 days), and multiply it by the agreed millet (150 hu). 
Each becomes its own dividend. 
Take one year as 354 days as the divisor. 
Divide the dividend by the divisor to obtain the result.

Answer: the discounted millet is *a* hu, and the given millet is *b* hu.
"""

# 與粟一百五十斛
與粟 = 150

# 已與之粟先五十八日
提前日數 = 58

# 一歲三百五十四日
一年日數 = 354

# 置歸作日數以與粟乘之，為實
折粟實 = 提前日數 * 與粟

# 以一歲三百五十四日為法，實如法得一
a = Fraction(折粟實, 一年日數)

# 與粟 = 原粟 - 折粟
b = 與粟 - a#----- content ends here -----

"""
"""
