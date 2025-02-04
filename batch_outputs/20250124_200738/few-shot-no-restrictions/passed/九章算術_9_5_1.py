"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water surface. 
When the reed is pulled to the edge of the pond, it just reaches the edge of the pond.

Question: How deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it, and subtract the square of the height the reed extends above the water. 
Take the remainder, double the height the reed extends above the water, and divide by it to obtain the water depth. 
Add the height the reed extends above the water to the water depth to obtain the reed's length.

Answer: The water depth is *a* zhang; the reed's length is *b* zhang.
"""

from fractions import Fraction
import math

# 池方一丈 (side length of the square pond)
池邊長 = 1  # in 丈

# 葭出水一尺 (reed extends 1 chi above water)
出水 = Fraction(1, 10)  # 1 chi = 1/10 丈

# 半池方 (half the side length of the pond)
半池邊 = Fraction(池邊長, 2)

# 半池方自乘 (square of half the side length)
半池邊平方 = 半池邊 ** 2

# 出水一尺自乘 (square of the height the reed extends above water)
出水平方 = 出水 ** 2

# 餘 = 半池邊平方 - 出水平方
餘 = 半池邊平方 - 出水平方

# 餘倍出水除之 (divide the remainder by twice the height the reed extends above water)
水深 = 餘 / (2 * 出水)

# 葭長 = 水深 + 出水
葭長 = 水深 + 出水

# Final answers
a = 水深  # 水深 in 丈
b = 葭長  # 葭長 in 丈

# Output the results
a, b#----- content ends here -----

"""
"""
