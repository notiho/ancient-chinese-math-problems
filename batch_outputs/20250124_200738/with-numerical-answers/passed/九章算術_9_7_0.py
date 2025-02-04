"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a(=101/20)丈 。
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A pole leans against the wall, with its top level with the top of the wall.
The base of the pole is pulled back 1 chi, and the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it.
Divide by the number of chi the pole is pulled back, and take the result.
Add the number of chi the pole is pulled back, and halve the sum.
This gives the length of the pole.

Answer: *a*(=101/20) zhang.
"""

# 垣高一丈 (convert to chi: 1丈 = 10尺)
垣高 = 10

# 引木卻行一尺
卻行 = 1

# 以垣高十尺自乘
垣高平方 = 垣高 * 垣高

# 如卻行尺數而一，所得
商 = Fraction(垣高平方, 卻行)

# 以加卻行尺數
加卻行 = 商 + 卻行

# 而半之，即木長數
木長 = Fraction(加卻行, 2)

# Convert to zhang (1丈 = 10尺)
a = Fraction(木長, 10)  # 101/20 zhang#----- content ends here -----

"""
"""
