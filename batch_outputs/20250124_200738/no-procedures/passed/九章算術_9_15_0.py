"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 8 bu and a height (leg) of 15 bu.
Question: what is the diameter of the inscribed circle?

Answer: the diameter is *a* bu.
"""

# 句 (base) = 8 bu
句 = 8

# 股 (height) = 15 bu
股 = 15

# Calculate the hypotenuse (弦) using the Pythagorean theorem
弦 = (句**2 + 股**2)**0.5

# The area of the triangle
面積 = (句 * 股) / 2

# The radius of the inscribed circle is given by: 面積 / 半周長
半周長 = (句 + 股 + 弦) / 2
半徑 = 面積 / 半周長

# The diameter of the inscribed circle
a = 2 * 半徑

# Result
a#----- content ends here -----

"""
"""
