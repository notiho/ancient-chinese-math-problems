"""
今有客歲作要與粟一百五十斛已與之粟先五十八日歸問折粟與粟各幾何
術曰置歸作日數以與粟乘之各自為實以一歲三百五十四日為法實如法得一
答曰折粟 a斛 與粟 b斛
"""

"""
Suppose last year, an agreement was made to give 150 hu of millet. 
The millet was already given 58 days earlier than the agreed return date.
Question: how much millet is considered as "discounted millet" (折粟), and how much is the remaining millet actually given (與粟)?

The procedure says: Place the number of days returned earlier and multiply it by the millet to be given. 
Each becomes its own dividend. 
Take one year as 354 days as the divisor. 
Divide the dividend by the divisor to obtain the result.

Answer: the discounted millet is *a* hu, and the millet actually given is *b* hu.
"""

# 與粟一百五十斛
與粟 = 150

# 已與之粟先五十八日歸
提前日數 = 58

# 一歲三百五十四日
一年日數 = 354

# 置歸作日數，以與粟乘之，為實
折粟實 = 提前日數 * 與粟

# 以一歲三百五十四日為法，實如法得一
a = Fraction(折粟實, 一年日數)

# 與粟 = 原粟 - 折粟
b = 與粟 - a
"""
"""
