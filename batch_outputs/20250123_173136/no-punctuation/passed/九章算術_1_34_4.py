"""
今有弧田弦三十步矢十五步問為田幾何
術曰以弦乘矢矢又自乘并之二而一
荅曰 a畝 
"""

"""
Suppose there is an arc-shaped field with a chord (base) of 30 bu and an arrow (height) of 15 bu.
Question: how large is the field?

The procedure says: Multiply the chord by the arrow, then multiply the arrow by itself, and add these together.
Divide the result by 2 to obtain the area.

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
積步 = 弦乘矢 + 矢自乘

# 二而一
積步 = Fraction(積步, 2)

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即畝數
a = Fraction(積步, 畝法)
"""
"""
