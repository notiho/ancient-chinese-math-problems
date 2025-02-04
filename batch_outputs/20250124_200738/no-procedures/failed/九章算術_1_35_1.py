"""
又有弧田，弦七十八步、二分步之一，矢十三步、九分步之七。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular segment-shaped field (弧田). 
The chord (弦) is 78 1/2 bu, and the arrow (矢, height of the segment) is 13 7/9 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

from fractions import Fraction

# 弦 (chord) = 78 1/2 bu
弦 = 78 + Fraction(1, 2)

# 矢 (arrow) = 13 7/9 bu
矢 = 13 + Fraction(7, 9)

# Area of a circular segment (弧田) is calculated as:
# Area = (弦 × 矢) ÷ 2
田積 = (弦 * 矢) / 2

# Convert the area from square bu to mu (1 畝 = 240 square bu)
a = 田積 / 240

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 51491/19440, Actual: 4867/2160"""
