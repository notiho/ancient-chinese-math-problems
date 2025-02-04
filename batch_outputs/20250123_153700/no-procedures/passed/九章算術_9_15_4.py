"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
荅曰： a步 。
"""

"""
Suppose there is a right triangle with a base (leg) of 8 bu and a height (leg) of 15 bu.
Question: what is the diameter of the inscribed circle?

Answer: the diameter is *a* bu.
"""

# 句 (base) = 8步
句 = 8

# 股 (height) = 15步
股 = 15

# Calculate the hypotenuse (弦) using the Pythagorean theorem
弦 = Fraction((句**2 + 股**2)**0.5)

# Calculate the area of the triangle
面積 = Fraction(句 * 股, 2)

# Calculate the semi-perimeter of the triangle
半周長 = Fraction(句 + 股 + 弦, 2)

# The radius of the inscribed circle is the area divided by the semi-perimeter
半徑 = Fraction(面積, 半周長)

# The diameter is twice the radius
a = 2 * 半徑
"""
"""
