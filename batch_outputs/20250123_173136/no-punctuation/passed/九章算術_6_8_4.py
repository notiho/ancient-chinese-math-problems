"""
今有程傳委輸空車日行七十里重車日行五十里今載太倉粟輸上林五日三返問太倉去上林幾何
術曰并空重里數以三返乘之為法令空重相乘又以五日乘之為實實如法得一里
荅曰 a里 
"""

"""
Suppose there is a transport system where an empty cart travels 70 li per day, and a loaded cart travels 50 li per day.
Now, grain is transported from Taicang to Shanglin, taking 5 days for 3 round trips.
Question: how far is it from Taicang to Shanglin?

The procedure says: Add the distances for the empty and loaded carts, and multiply by 3 round trips to obtain the divisor.
Let the empty and loaded distances be multiplied, and also multiply by 5 days to obtain the dividend.
Divide the dividend by the divisor to obtain the distance of one li.

Answer: *a* li.
"""

# 空車日行七十里
空車里數 = 70

# 重車日行五十里
重車里數 = 50

# 三返
返次數 = 3

# 五日
日數 = 5

# 并空重里數
空重里數和 = 空車里數 + 重車里數

# 以三返乘之，為法
法 = 空重里數和 * 返次數

# 令空重相乘
空重相乘 = 空車里數 * 重車里數

# 又以五日乘之，為實
實 = 空重相乘 * 日數

# 實如法得一里
a = Fraction(實, 法)
"""
"""
