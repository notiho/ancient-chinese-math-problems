"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at its center and extends 1 chi above the water.
When the reed is pulled to the edge of the pond, it just reaches the edge of the pond.
Question: how deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it, and subtract the square of the height of the reed above the water.
Take the remainder, double the height of the reed above the water, and divide by it to obtain the water depth.
Add the height of the reed above the water to the water depth to obtain the length of the reed.

Answer: the water depth is *a* zhang; the reed length is *b* zhang.
"""

from fractions import Fraction
from math import sqrt

# 池方一丈
池邊長 = 1  # zhang

# 葭生其中央，出水一尺
出水 = Fraction(1, 10)  # 1 chi = 1/10 zhang

# 半池方自乘
半池邊 = Fraction(池邊長, 2)
半池邊平方 = 半池邊 ** 2

# 以出水一尺自乘
出水平方 = 出水 ** 2

# 減之，餘
餘 = 半池邊平方 - 出水平方

# 倍出水除之，即得水深
水深 = 餘 / (2 * 出水)

# 加出水數，得葭長
葭長 = 水深 + 出水

a = 水深
b = 葭長

# Output results
a, b#----- content ends here -----

"""
"""
