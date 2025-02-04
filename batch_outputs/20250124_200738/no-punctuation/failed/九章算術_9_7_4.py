"""
今有垣高一丈倚木於垣上與垣齊引木卻行一尺其木至地問木幾何
術曰以垣高十尺自乘如卻行尺數而一所得以加卻行尺數而半之即木長數
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A pole is leaned against the wall, reaching the top of the wall.
When the bottom of the pole is pulled 1 chi away from the wall, the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it.
Add the square of the number of chi the pole is pulled away.
Take the sum, and then take its square root. This gives the length of the pole.

Answer: the pole is *a* zhang.
"""

from fractions import Fraction
import math

# 垣高一丈 (convert to chi: 1丈 = 10尺)
垣高 = 10

# 卻行一尺
卻行 = 1

# 以垣高十尺自乘
垣高平方 = 垣高 ** 2

# 如卻行尺數而一所得
卻行平方 = 卻行 ** 2

# 以加卻行尺數
總和 = 垣高平方 + 卻行平方

# 而半之即木長數 (take square root)
木長 = math.sqrt(總和)

# Convert back to zhang (1丈 = 10尺)
a = Fraction(木長, 10)  # 木長 in 丈#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
