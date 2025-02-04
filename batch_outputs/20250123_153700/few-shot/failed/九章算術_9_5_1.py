"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
Suppose there is a square pond with a side length of 1 zhang, and a reed grows at its center, extending 1 chi above the water.
When the reed is pulled to the edge of the pond, it just reaches the edge of the pond.
Question: how deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it. 
Square the length of the reed extending above the water, subtract it from the previous result. 
Take the remainder, double the length of the reed extending above the water, and divide by it. 
This gives the depth of the water. 
Add the length of the reed extending above the water to the depth of the water to get the total length of the reed.

Answer: the water is *a* zhang deep; the reed is *b* zhang long.
"""

from fractions import Fraction

# 池方一丈
池邊長 = 1  # 丈

# 葭生其中央，出水一尺
出水 = Fraction(1, 10)  # 尺 converted to 丈 (1 丈 = 10 尺)

# 半池方自乘
半池邊 = 池邊長 / 2
半池方自乘 = 半池邊 ** 2

# 以出水一尺自乘
出水自乘 = 出水 ** 2

# 減之，餘
餘 = 半池方自乘 - 出水自乘

# 倍出水除之，即得水深
水深 = 餘 / (2 * 出水)

# 加出水數，得葭長
葭長 = 水深 + 出水

a = 水深
b = 葭長
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 1.2
Variable 'b' has wrong value. Expected: 13/10, Actual: 1.3"""
