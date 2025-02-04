"""
今有弧田弦八十步矢五步。問：為田㡬何？
答曰： a步 。
"""

"""
Suppose there is an arc-shaped field where the chord (straight line across the arc) is 80 bu and the arrow (perpendicular distance from the chord to the arc) is 5 bu.
Question: how large is the area of the field?

Answer: it is *a* bu².
"""

# 弦 (chord) = 80步
弦 = 80

# 矢 (arrow) = 5步
矢 = 5

# Formula for the area of an arc-shaped field:
# Area = (弦 × 矢) ÷ 2
a = Fraction(弦 * 矢, 2)

# The area of the field is `a` bu².
"""
"""
