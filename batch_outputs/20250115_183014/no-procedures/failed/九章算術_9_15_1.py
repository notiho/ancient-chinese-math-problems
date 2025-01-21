"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
荅曰： a步 。
"""

"""
Suppose there is a right triangle with one leg (ju) of 8 bu and the other leg (gu) of 15 bu.
Question: What is the diameter of the largest circle that can fit inside the triangle (the inscribed circle)?

Answer: The diameter is *a* bu.
"""

# 句 (one leg)
句 = 8

# 股 (other leg)
股 = 15

# Calculate the hypotenuse (弦) using the Pythagorean theorem
弦 = Fraction((句**2 + 股**2)**0.5)

# Calculate the semi-perimeter of the triangle
半周 = Fraction(句 + 股 + 弦, 2)

# The radius of the inscribed circle is given by the formula:
# r = (Area of the triangle) / (Semi-perimeter)
# Area of the triangle = (1/2) * 句 * 股
r = Fraction((句 * 股) / 2, 半周)

# The diameter of the inscribed circle is twice the radius
a = 2 * r
"""
Code error: both arguments should be Rational instances"""
