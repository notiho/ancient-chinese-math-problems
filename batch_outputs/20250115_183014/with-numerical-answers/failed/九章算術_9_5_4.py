"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
術曰：半池方自乘，以出水一尺自乘，減之，餘，倍出水除之，即得水深。加出水數，得葭長。
荅曰：水深 a(=6/5)丈 ；葭長 b(=13/10)丈 。
"""

"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at its center and extends 1 chi above the water.
When the reed is pulled to the edge of the pond, it just reaches the edge.
Question: how deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it. 
Square the height of the reed above the water and subtract it from the previous result. 
Take the remainder, double the height of the reed, and divide by it. This gives the depth of the water.
Add the height of the reed to the depth of the water to obtain the length of the reed.

Answer: The water depth is *a*(=6/5) zhang, and the reed length is *b*(=13/10) zhang.
"""

# 池方一丈
池邊長 = 1  # 丈

# 葭生其中央，出水一尺
出水 = Fraction(1, 10)  # 1 尺 = 1/10 丈

# 半池方自乘
半池邊 = 池邊長 / 2
半池方自乘 = 半池邊 ** 2

# 以出水一尺自乘，減之
出水自乘 = 出水 ** 2
餘 = 半池方自乘 - 出水自乘

# 餘，倍出水除之，即得水深
水深 = Fraction(餘, 2 * 出水)

# 加出水數，得葭長
葭長 = 水深 + 出水

a = 水深  # 6/5 丈
b = 葭長  # 13/10 丈
"""
Code error: both arguments should be Rational instances"""
