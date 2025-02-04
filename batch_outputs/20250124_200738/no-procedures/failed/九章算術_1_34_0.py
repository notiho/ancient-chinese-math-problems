"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular segment-shaped field (弧田) with a chord (弦) of 30 bu and a height (矢) of 15 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

# 弦 (chord) = 30步
弦 = 30

# 矢 (height) = 15步
矢 = 15

# Area of the circular segment field = (弦 * 矢) / 2
area_in_bu = (弦 * 矢) / 2

# Convert the area from bu² to mu (1 mu = 240 bu²)
a = Fraction(area_in_bu, 240)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
