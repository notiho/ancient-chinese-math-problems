"""
今有弧田，弦三十步，矢十五步。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a(=45/32)畝 。
"""

"""
Suppose there is an arc-shaped field with a chord (base) of 30 bu and an arrow (height) of 15 bu.
Question: how large is the field?

The procedure says: Multiply the chord by the arrow, then multiply the arrow by itself, and add these together. Divide the result by 2.

The answer says: *a*(=45/32) mu.
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
田積步 = Fraction(和, 2)

# 畝法二百四十步
畝法 = 240

# 田積步轉為畝
a = Fraction(田積步, 畝法) # 45/32

"""
"""
