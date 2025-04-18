"""
今有垣高一丈倚木於垣上與垣齊引木卻行一尺其木至地問木幾何
術曰以垣高十尺自乘如卻行尺數而一所得以加卻行尺數而半之即木長數
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A pole is leaned against the wall, with its top flush with the top of the wall.
The base of the pole is pulled 1 chi away from the wall, and the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it.
Add the square of the distance the base of the pole is pulled away (1 chi).
Take the sum and halve it, obtaining the length of the pole.

The answer says: *a* zhang.
"""

from fractions import Fraction

# 垣高一丈 (convert to chi: 1丈 = 10尺)
垣高 = 10  # in chi

# 卻行一尺
卻行 = 1  # in chi

# 以垣高十尺自乘
垣高平方 = 垣高 * 垣高

# 如卻行尺數而一所得
卻行平方 = 卻行 * 卻行

# 以加卻行尺數
總和 = 垣高平方 + 卻行平方

# 而半之，即木長數
木長 = Fraction(總和).sqrt()

# Convert back to zhang (1丈 = 10尺)
a = 木長 / 10#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
