"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water surface. 
When the reed is pulled to the edge of the pond, it just touches the edge of the pond.

Question: What are the depth of the water and the length of the reed?

The procedure says: Take half the side length of the pond, square it, and subtract the square of the reed's height above the water. 
Take the remainder, double the reed's height, and divide by it to obtain the water depth. 
Add the reed's height to the water depth to get the total length of the reed.

Answer: The water depth is *a* zhang; the reed length is *b* zhang.
"""

from fractions import Fraction
from math import sqrt

# 池方一丈 (side length of the square pond)
池邊長 = 1  # in zhang

# 葭出水一尺 (reed extends 1 chi above the water)
出水 = Fraction(1, 10)  # 1 chi = 1/10 zhang

# 半池方 (half the side length of the pond)
半池邊長 = Fraction(池邊長, 2)

# 半池方自乘 (square of half the side length)
半池邊長平方 = 半池邊長 ** 2

# 出水一尺自乘 (square of the reed's height above the water)
出水平方 = 出水 ** 2

# 減之，餘 (subtract the square of the reed's height from the square of half the side length)
餘 = 半池邊長平方 - 出水平方

# 倍出水 (double the reed's height)
倍出水 = 2 * 出水

# 餘倍出水除之，即得水深 (divide the remainder by double the reed's height to get the water depth)
水深 = Fraction(餘, 倍出水)

# 加出水數，得葭長 (add the reed's height to the water depth to get the reed's total length)
葭長 = 水深 + 出水

# Final results
a = 水深  # water depth in zhang
b = 葭長  # reed length in zhang

# Output
a, b#----- content ends here -----

"""
"""
