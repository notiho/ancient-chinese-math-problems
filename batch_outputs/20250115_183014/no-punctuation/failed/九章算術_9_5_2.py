"""
今有池方一丈葭生其中央出水一尺引葭赴岸適與岸齊問水深葭長各幾何
術曰半池方自乘以出水一尺自乘減之餘倍出水除之即得水深加出水數得葭長
荅曰水深 a丈 葭長 b丈 
"""

"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows from its center and extends 1 chi above the water. When the reed is pulled toward the edge of the pond, it just reaches the edge.
Question: how deep is the water, and how long is the reed?

The procedure says: Take half the side length of the pond, square it, and subtract the square of the height the reed extends above the water. Multiply the remainder by 2 and divide by the height the reed extends above the water. This gives the depth of the water. Add the height the reed extends above the water to the depth to get the length of the reed.

Answer: the water is *a* zhang deep, and the reed is *b* zhang long.
"""

# 池方一丈
池邊長 = 1  # 丈

# 葭生其中央出水一尺
出水 = Fraction(1, 10)  # 尺 to 丈 conversion: 1 尺 = 1/10 丈

# 半池方
半池邊 = 池邊長 / 2

# 半池方自乘
半池方平方 = 半池邊 ** 2

# 出水一尺自乘
出水平方 = 出水 ** 2

# 減之
餘 = 半池方平方 - 出水平方

# 餘倍出水
餘倍出水 = 2 * 餘

# 除之即得水深
水深 = 餘倍出水 / 出水

# 加出水數得葭長
葭長 = 水深 + 出水

a = 水深
b = 葭長
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 4.8
Variable 'b' has wrong value. Expected: 13/10, Actual: 4.8999999999999995"""
