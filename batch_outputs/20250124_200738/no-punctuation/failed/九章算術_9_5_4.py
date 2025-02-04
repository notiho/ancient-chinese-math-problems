"""
今有池方一丈葭生其中央出水一尺引葭赴岸適與岸齊問水深葭長各幾何
術曰半池方自乘以出水一尺自乘減之餘倍出水除之即得水深加出水數得葭長
荅曰水深 a丈 葭長 b丈 
"""

#----- content starts here -----
"""
Suppose there is a square pond with each side measuring 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water. When the reed is pulled toward the edge of the pond, it just reaches the edge of the pond.
Question: how deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it, and subtract the square of the reed's height above the water. Multiply the remainder by 2 and divide by the reed's height above the water. This gives the water depth. Add the reed's height above the water to the water depth to get the reed's total length.

Answer: the water depth is *a* zhang, and the reed's length is *b* zhang.
"""

from fractions import Fraction

# 池方一丈 (side length of the pond)
池邊長 = 1  # in 丈

# 葭生其中央出水一尺 (reed extends 1 chi above the water)
出水 = Fraction(1, 10)  # 1 chi = 1/10 zhang

# 半池方 (half the side length of the pond)
半池邊 = Fraction(池邊長, 2)

# 半池方自乘 (square of half the side length)
半池邊平方 = 半池邊 ** 2

# 出水一尺自乘 (square of the reed's height above the water)
出水平方 = 出水 ** 2

# 半池方自乘以出水一尺自乘減之 (subtract the square of the reed's height from the square of half the side length)
差 = 半池邊平方 - 出水平方

# 餘倍出水 (multiply the remainder by 2)
餘倍出水 = 2 * 差

# 除之即得水深 (divide by the reed's height above the water to get the water depth)
水深 = 餘倍出水 / 出水

# 加出水數得葭長 (add the reed's height above the water to the water depth to get the reed's total length)
葭長 = 水深 + 出水

a = 水深
b = 葭長#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 24/5
Variable 'b' has wrong value. Expected: 13/10, Actual: 49/10"""
