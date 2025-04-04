"""
又有弧田，弦七十八步、二分步之一，矢十三步、九分步之七。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is an arc-shaped field. The chord (straight line across the arc) is 78 1/2 bu, and the arrow (perpendicular distance from the chord to the arc) is 13 7/9 bu.
Question: how large is the field?

Answer: it is *a* mu.
"""

from fractions import Fraction

# 弦 (chord) = 78 1/2 步
弦 = Fraction(78, 1) + Fraction(1, 2)

# 矢 (arrow) = 13 7/9 步
矢 = Fraction(13, 1) + Fraction(7, 9)

# Formula for the area of an arc-shaped field: (1/2) * 弦 * 矢
田 = Fraction(1, 2) * 弦 * 矢

# Convert the area from bu^2 to mu (1 mu = 240 bu^2)
a = Fraction(田, 240)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 51491/19440, Actual: 4867/2160"""
