"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a(=875/18)里 。
"""

"""
Suppose there is a transportation task involving carrying grain. An empty cart travels 70 li per day, and a loaded cart travels 50 li per day.
Now, grain is transported from Taicang to Shanglin, completing 3 round trips in 5 days.
Question: how far is Taicang from Shanglin?

The procedure says: Add the distances for the empty and loaded cart, and multiply by 3 round trips, obtaining the divisor.
Multiply the distances for the empty and loaded cart, and also multiply by 5 days, obtaining the dividend.
Divide the dividend by the divisor to obtain the distance of 1 li.

Answer: *a*(=875/18) li.
"""

# 空車日行七十里
空車 = 70

# 重車日行五十里
重車 = 50

# 并空、重里數
空重和 = 空車 + 重車

# 以三返乘之，為法
三返 = 3
法 = 空重和 * 三返

# 令空、重相乘
空重積 = 空車 * 重車

# 又以五日乘之，為實
五日 = 5
實 = 空重積 * 五日

# 實如法得一里
a = Fraction(實, 法) # 875/18

"""
"""
