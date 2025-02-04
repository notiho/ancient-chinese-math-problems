"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at its center and extends 1 chi above the water surface.
When the reed is pulled to the edge of the pond, it just touches the edge of the pond.
Question: how deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it. Subtract the square of the height of the reed above the water. Take the remainder, double the height of the reed, and divide by it. This gives the water depth.
Add the height of the reed above the water to the water depth to get the reed's total length.

Answer: The water depth is *a* zhang, and the reed's length is *b* zhang.
"""

from fractions import Fraction
import math

# 池方一丈
池邊長 = 1  # 丈

# 葭出水一尺
葭出水 = Fraction(1, 10)  # 1 尺 = 1/10 丈

# 半池方自乘
半池邊長 = 池邊長 / 2
半池邊平方 = 半池邊長 ** 2

# 出水一尺自乘
葭出水平方 = 葭出水 ** 2

# 減之，餘
餘 = 半池邊平方 - 葭出水平方

# 倍出水除之，即得水深
水深 = 餘 / (2 * 葭出水)

# 加出水數，得葭長
葭長 = 水深 + 葭出水

# 答案
a = 水深
b = 葭長

# Convert to decimal for clarity
a_decimal = float(a)
b_decimal = float(b)

a, b, a_decimal, b_decimal#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 1.2
Variable 'b' has wrong value. Expected: 13/10, Actual: 1.3"""
