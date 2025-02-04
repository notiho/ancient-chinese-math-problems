"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular segment field (弧田) with a chord (弦) of 30 bu and a height (矢) of 15 bu.
Question: how large is the field?

The procedure says: Multiply the chord (弦) by the height (矢), then multiply the height (矢) by itself.
Add these two results together, then divide by 2 to obtain the area.

The answer says: *a* mu.
"""

from fractions import Fraction

# 弦三十步
弦 = 30

# 矢十五步
矢 = 15

# 以弦乘矢
弦乘矢 = 弦 * 矢

# 矢又自乘
矢自乘 = 矢 * 矢

# 并之
總積步 = 弦乘矢 + 矢自乘

# 二而一
田積步 = Fraction(總積步, 2)

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即畝數
a = Fraction(田積步, 畝法)

a#----- content ends here -----

"""
"""
