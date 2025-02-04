"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a circular segment-shaped field (弧田) with a chord (弦) of 30 bu and a height (矢) of 15 bu.
Question: how large is the field?

Answer: *a* mu.
"""

# 弦 (chord) = 30 bu
弦 = 30

# 矢 (height) = 15 bu
矢 = 15

# Formula for the area of a circular segment-shaped field:
# Area = (弦 × 矢) ÷ 3
area_in_bu = (弦 * 矢) / 3

# Convert the area from bu to mu (1 mu = 240 bu)
a = Fraction(area_in_bu, 240)
"""
Code error: both arguments should be Rational instances"""
