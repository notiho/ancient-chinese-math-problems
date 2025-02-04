"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

"""
Suppose there is a wall 1 zhang (10 chi) high. A pole is leaned against the wall, with its top level with the top of the wall.
The base of the pole is moved 1 chi away from the wall, and the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it. 
Divide this by the number of chi the base of the pole is moved away from the wall. 
Add the number of chi the base is moved away, and halve the result. This gives the length of the pole.

Answer: the pole is *a* zhang.
"""

# 垣高一丈 (10 尺)
垣高 = 10

# 卻行一尺
卻行 = 1

# 以垣高十尺自乘
垣高平方 = 垣高 * 垣高

# 如卻行尺數而一，所得
商 = Fraction(垣高平方, 卻行)

# 以加卻行尺數
加和 = 商 + 卻行

# 而半之，即木長數
木長 = Fraction(加和, 2)

# Convert to 丈 (1 丈 = 10 尺)
a = Fraction(木長, 10)  # 木長 in 丈
"""
"""
