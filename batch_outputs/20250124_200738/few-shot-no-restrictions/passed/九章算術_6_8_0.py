"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a transport system where an empty cart travels 70 li per day, and a loaded cart travels 50 li per day.
Now, grain is being transported from Taicang to Shanglin. In 5 days, the cart completes 3 round trips.
Question: How far is Taicang from Shanglin?

The procedure says: Add the distances for empty and loaded carts, and multiply by the number of round trips (3), to get the divisor.
Multiply the distances for empty and loaded carts, and then multiply by the number of days (5), to get the dividend.
Divide the dividend by the divisor to get the distance of 1 li.

The answer says: *a* li.
"""

from fractions import Fraction

# 空車日行七十里
空車里數 = 70

# 重車日行五十里
重車里數 = 50

# 五日三返
日數 = 5
往返次數 = 3

# 并空、重里數，以三返乘之，為法
法 = (空車里數 + 重車里數) * 往返次數

# 令空、重相乘，又以五日乘之，為實
實 = (空車里數 * 重車里數) * 日數

# 實如法得一里
a = Fraction(實, 法)

a  # Distance from Taicang to Shanglin in li#----- content ends here -----

"""
"""
