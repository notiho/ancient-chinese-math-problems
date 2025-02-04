"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular segment-shaped field (弧田). The chord (弦) is 30 bu, and the arrow (矢, the perpendicular distance from the chord to the arc) is 15 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# 弦 (chord) = 30步
弦 = 30

# 矢 (arrow) = 15步
矢 = 15

# The formula for the area of a circular segment is approximately:
# Area = (弦 × 矢) ÷ 3
田積 = Fraction(弦 * 矢, 3)

# Convert the area from square bu to mu (1 畝 = 240 square bu)
a = Fraction(田積, 240)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 45/32, Actual: 5/8"""
