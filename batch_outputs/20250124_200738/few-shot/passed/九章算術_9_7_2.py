"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A pole leans against the wall, with its top level with the top of the wall.
If the base of the pole is moved 1 chi away from the wall, the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it. Divide it by the number of chi the base of the pole is moved away, obtaining a result.
Add this result to the number of chi the base of the pole is moved away, and halve the sum. This gives the length of the pole.

Answer: the pole is *a* zhang long.
"""

# 垣高一丈 (1丈 = 10尺)
垣高 = 10  # in 尺

# 引木卻行一尺
卻行 = 1  # in 尺

# 以垣高十尺自乘
垣高平方 = 垣高 * 垣高

# 如卻行尺數而一，所得
所得 = Fraction(垣高平方, 卻行)

# 以加卻行尺數
加和 = 所得 + 卻行

# 而半之，即木長數
木長 = Fraction(加和, 2)

# Convert 木長 to 丈
a = Fraction(木長, 10)  # 1丈 = 10尺#----- content ends here -----

"""
"""
