"""
又有弧田弦七十八步二分步之一矢十三步九分步之七問為田幾何
術曰以弦乘矢矢又自乘并之二而一
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a circular segment-shaped field. The chord is 78 bu and 1/2 bu, and the arrow is 13 bu and 7/9 bu.
Question: how large is the field?

The procedure says: Multiply the chord by the arrow. Then, multiply the arrow by itself. Add these together, and divide by 2.

The answer says: *a* mu.
"""

from fractions import Fraction

# 弦七十八步二分步之一
弦 = 78 + Fraction(1, 2)

# 矢十三步九分步之七
矢 = 13 + Fraction(7, 9)

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
a = Fraction(積步, 畝法)#----- content ends here -----

"""
"""
