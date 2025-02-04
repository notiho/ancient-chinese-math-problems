"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a transport task involving empty and loaded carts. An empty cart travels 70 li per day, while a loaded cart travels 50 li per day.
Now, grain is being transported from Taicang to Shanglin, and the round trip (three trips in five days) is completed.
Question: How far is Taicang from Shanglin?

The procedure says: Add the distances for empty and loaded carts, and multiply by the number of round trips (three trips), giving the divisor.
Multiply the distances for empty and loaded carts, and then multiply by the number of days (five days), giving the dividend.
Divide the dividend by the divisor to obtain the distance of one li.

Answer: *a* li.
"""

from fractions import Fraction

# 空車日行七十里
空車日行 = 70

# 重車日行五十里
重車日行 = 50

# 五日三返
日數 = 5
三返 = 3

# 并空、重里數
空重和 = 空車日行 + 重車日行

# 以三返乘之，為法
法 = 空重和 * 三返

# 令空、重相乘
空重積 = 空車日行 * 重車日行

# 又以五日乘之，為實
實 = 空重積 * 日數

# 實如法得一里
a = Fraction(實, 法)

a#----- content ends here -----

"""
"""
