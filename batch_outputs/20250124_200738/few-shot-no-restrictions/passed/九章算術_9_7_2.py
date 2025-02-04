"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A piece of wood is leaned against the wall, with its top level with the top of the wall.
The base of the wood is moved 1 chi away from the wall, and the wood reaches the ground.
Question: how long is the wood?

The procedure says: Take the height of the wall (10 chi) and square it. Divide it by the number of chi the base of the wood is moved away, then add the number of chi the base is moved away. Take half of the result, and this is the length of the wood.

Answer: the wood is *a* zhang long.
"""

from fractions import Fraction

# 垣高一丈 (1丈 = 10尺)
垣高 = 10  # in chi

# 卻行一尺
卻行 = 1  # in chi

# 以垣高十尺自乘
垣高平方 = 垣高 ** 2

# 如卻行尺數而一，所得
分母 = 卻行
商 = Fraction(垣高平方, 分母)

# 以加卻行尺數
加和 = 商 + 卻行

# 而半之，即木長數
木長 = Fraction(加和, 2)

# Convert to zhang (1丈 = 10尺)
a = Fraction(木長, 10)  # in zhang

a  # The length of the wood in zhang#----- content ends here -----

"""
"""
