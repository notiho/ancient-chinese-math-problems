"""
今有田方一百二十一步欲以為圓問周幾何
術曰方自相乗又以十二乗之為實開方除之即得
答曰 a步
"""

#----- content starts here -----
"""
Suppose there is a square field with a side length of 121 bu. It is desired to make it into a circular field.
Question: what is the circumference of the circle?

The procedure says: Square the side length of the square field. Multiply it by 12, obtaining the dividend.
Take the square root of the dividend and divide it by the divisor (π approximated as 3.14). The result is the circumference.

Answer: *a* bu.
"""

# 田方一百二十一步
方 = 121

# 方自相乘
方積 = 方 * 方

# 又以十二乘之，為實
實 = 12 * 方積

# 開方 (square root)
開方 = Fraction(實).sqrt()

# 除之 (π approximated as 3.14)
π = Fraction(157, 50)  # Approximation of π as 3.14
a = 開方 / π#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
