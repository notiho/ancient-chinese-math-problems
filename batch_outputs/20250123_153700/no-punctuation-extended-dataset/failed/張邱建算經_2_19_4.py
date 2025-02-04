"""
今有田方一百二十一步欲以為圓問周幾何
術曰方自相乗又以十二乗之為實開方除之即得
答曰 a步
"""

"""
Suppose there is a square field with a side length of 121 bu. It is desired to make it into a circular field.
Question: what is the circumference of the circular field?

The procedure says: Square the side length of the square field, then multiply it by 12, obtaining the dividend.
Take the square root of the dividend and divide it by the divisor (π approximated as 3), obtaining the circumference.

Answer: *a* bu.
"""

# 田方一百二十一步
方 = 121

# 方自相乘
方積 = 方 * 方

# 又以十二乘之，為實
實 = 12 * 方積

# 開方
開方 = Fraction(實).sqrt()

# 除之 (π approximated as 3)
a = Fraction(開方, 3)
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
