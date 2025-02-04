"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a(=875/18)里 。
"""

#----- content starts here -----
"""
Suppose there is a transportation task involving carrying grain. An empty cart travels 70 li per day, and a loaded cart travels 50 li per day.
Now, grain is transported from Taicang to Shanglin, completing three round trips in five days.
Question: how far is Taicang from Shanglin?

The procedure says: Add the distances for empty and loaded carts, and multiply by the three round trips to obtain the divisor.
Multiply the distances for empty and loaded carts, and then multiply by the five days to obtain the dividend.
Divide the dividend by the divisor to obtain the distance of one li.

Answer: *a*(=875/18) li.
"""

# 空車日行七十里
空車里數 = 70

# 重車日行五十里
重車里數 = 50

# 五日三返
日數 = 5
返數 = 3

# 并空、重里數
空重和 = 空車里數 + 重車里數

# 以三返乘之，為法
法 = 空重和 * 返數

# 令空、重相乘
空重積 = 空車里數 * 重車里數

# 又以五日乘之，為實
實 = 空重積 * 日數

# 實如法得一里
a = Fraction(實, 法) # 875/18
#----- content ends here -----

"""
"""
