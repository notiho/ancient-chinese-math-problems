"""
今有程傳委輸空車日行七十里重車日行五十里今載太倉粟輸上林五日三返問太倉去上林幾何
術曰并空重里數以三返乘之為法令空重相乘又以五日乘之為實實如法得一里
荅曰 a里 
"""

"""
Suppose there is a transport system where an empty cart travels 70 li per day, and a loaded cart travels 50 li per day.
Now, grain is being transported from Taicang to Shanglin, taking 5 days for 3 round trips.
Question: how far is Taicang from Shanglin?

The procedure says: Add the distances traveled by the empty and loaded carts, and multiply this sum by the number of round trips (3), obtaining the divisor.
Multiply the distances of the empty and loaded carts, and also multiply by the number of days (5), obtaining the dividend.
Divide the dividend by the divisor to obtain the distance of one li.

The answer says: *a* li.
"""

# 空車日行七十里
空車里數 = 70

# 重車日行五十里
重車里數 = 50

# 三返
返數 = 3

# 五日
日數 = 5

# 并空重里數，以三返乘之，為法
法 = (空車里數 + 重車里數) * 返數

# 令空重相乘，又以五日乘之，為實
實 = (空車里數 * 重車里數) * 日數

# 實如法得一里
a = Fraction(實, 法)
"""
"""
