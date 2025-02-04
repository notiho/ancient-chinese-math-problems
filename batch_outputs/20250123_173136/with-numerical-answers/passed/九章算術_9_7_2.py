"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a(=101/20)丈 。
"""

"""
Suppose there is a wall 1 zhang high. A pole leans against the wall, with its top level with the top of the wall.
The base of the pole is moved 1 chi away from the wall, and the pole touches the ground.
Question: how long is the pole?

The procedure says: Take the height of the wall (10 chi) and square it.
Divide this by the distance moved (in chi), then add the distance moved.
Take half of the result, and this is the length of the pole.

Answer: *a*(=101/20) zhang.
"""

# 垣高一丈
垣高 = 1  # in 丈
垣高尺 = 10 * 垣高  # convert to 尺

# 引木卻行一尺
卻行 = 1  # in 尺

# 以垣高十尺自乘
垣高平方 = 垣高尺 * 垣高尺

# 如卻行尺數而一，所得
除法結果 = Fraction(垣高平方, 卻行)

# 以加卻行尺數
加結果 = 除法結果 + 卻行

# 而半之，即木長數
木長尺 = Fraction(加結果, 2)

# Convert back to 丈
a = Fraction(木長尺, 10)  # 101/20 丈
"""
"""
