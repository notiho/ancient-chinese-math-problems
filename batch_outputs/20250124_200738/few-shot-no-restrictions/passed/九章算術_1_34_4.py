"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is an arc-shaped field. The chord (base) is 30 bu, and the arrow (height) is 15 bu.
Question: how large is the field?

The procedure says: Multiply the chord by the arrow, then multiply the arrow by itself, add these together, and divide by 2.

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
和 = 弦乘矢 + 矢自乘

# 二而一
積步 = Fraction(和, 2)

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即畝數
a = Fraction(積步, 畝法)

a#----- content ends here -----

"""
"""
