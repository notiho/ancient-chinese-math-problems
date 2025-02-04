"""
今有垣高一丈倚木於垣上與垣齊引木卻行一尺其木至地問木幾何
術曰以垣高十尺自乘如卻行尺數而一所得以加卻行尺數而半之即木長數
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A pole is leaned against the wall, reaching the top of the wall.
The pole is then pulled back 1 chi from the wall, and its end touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it.
Add the square of the distance pulled back (in chi).
Take the square root of the sum, which gives the length of the pole.

Answer: the pole is *a* zhang.
"""

from fractions import Fraction
import math

# 垣高一丈 (convert to chi: 1丈 = 10尺)
垣高 = 10  # in chi

# 卻行一尺
卻行 = 1  # in chi

# 以垣高十尺自乘
垣高平方 = 垣高 * 垣高

# 如卻行尺數而一所得
卻行平方 = 卻行 * 卻行

# 以加卻行尺數
和 = 垣高平方 + 卻行平方

# 而半之即木長數 (take the square root)
木長 = math.sqrt(和)

# Convert the result to zhang (1丈 = 10尺)
a = Fraction(木長, 10)  # in zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
