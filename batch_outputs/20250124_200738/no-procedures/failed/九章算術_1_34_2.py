"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular segment-shaped field (弧田). The chord (弦) is 30 bu, and the arrow (矢, the perpendicular distance from the midpoint of the chord to the arc) is 15 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

# 弦 (chord) = 30 bu
弦 = 30

# 矢 (arrow) = 15 bu
矢 = 15

# The formula for the area of a circular segment is:
# Area = (弦 × 矢) ÷ 3
area_in_bu = (弦 * 矢) / 3

# Convert the area from bu² to mu (1 mu = 240 bu²)
a = Fraction(area_in_bu, 240)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
