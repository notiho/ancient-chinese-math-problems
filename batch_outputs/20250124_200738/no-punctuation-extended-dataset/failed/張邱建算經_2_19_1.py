"""
今有田方一百二十一步欲以為圓問周幾何
術曰方自相乗又以十二乗之為實開方除之即得
答曰 a步
"""

#----- content starts here -----
"""
Suppose there is a square field with a side length of 121 bu. It is desired to transform it into a circular field.
Question: what is the circumference of the circular field?

The procedure says: Square the side length of the square field, then multiply it by 12. This gives the dividend.
Extract the square root of the dividend, then divide it by the divisor (π ≈ 3.14). The result is the circumference.

Answer: *a* bu.
"""

# 方一百二十一步
方 = 121

# 方自相乘
積 = 方 * 方

# 又以十二乘之，為實
實 = 12 * 積

# 開方 (square root)
開方 = Fraction(實).sqrt()

# 除之 (π ≈ 3.14)
圓周率 = Fraction(157, 50)  # Approximation of π
a = 開方 / 圓周率#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
