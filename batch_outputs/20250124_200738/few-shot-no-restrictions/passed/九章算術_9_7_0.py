"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A pole is leaned against the wall, and its top aligns with the top of the wall.
The base of the pole is pulled back 1 chi, and the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it. Divide it by the number of chi the pole is pulled back, and add the result to the number of chi the pole is pulled back. Then halve the sum to obtain the length of the pole.

Answer: the pole is *a* zhang long.
"""

from fractions import Fraction

# 垣高一丈 (1 zhang = 10 chi)
垣高 = 10  # in chi

# 卻行一尺 (1 chi)
卻行 = 1  # in chi

# 以垣高十尺自乘
垣高平方 = 垣高 ** 2

# 如卻行尺數而一，所得
商 = Fraction(垣高平方, 卻行)

# 以加卻行尺數
和 = 商 + 卻行

# 而半之，即木長數
木長 = 和 / 2

# Convert the result to zhang (1 zhang = 10 chi)
a = 木長 / 10  # in zhang

a  # The length of the pole in zhang#----- content ends here -----

"""
"""
