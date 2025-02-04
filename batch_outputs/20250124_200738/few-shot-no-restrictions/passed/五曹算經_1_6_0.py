"""
今有弧田弦八十步矢五步。問：為田㡬何？
術曰：列弦八十步半之得四十步以矢五步乘之即得。
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an arc-shaped field with a chord (弦) of 80 bu and an arrow (矢, the perpendicular height from the chord to the arc) of 5 bu.
Question: how large is the area of the field?

The procedure says: Take the chord of 80 bu, halve it to get 40 bu. Multiply this by the arrow of 5 bu to obtain the area.

Answer: *a* bu².
"""

from fractions import Fraction

# 弦八十步
弦 = 80

# 矢五步
矢 = 5

# 半之得四十步
半弦 = Fraction(弦, 2)

# 以矢五步乘之即得
面積 = 半弦 * 矢

a = 面積
#----- content ends here -----

"""
"""
