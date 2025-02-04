"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 垣高一丈，轉換為十尺
垣高 = 10  # 尺

# 卻行一尺
卻行 = 1  # 尺

# 以垣高十尺自乘
垣高平方 = 垣高 * 垣高

# 如卻行尺數而一，所得
卻行平方 = 卻行 * 卻行

# 所得，以加卻行尺數
木平方 = 垣高平方 + 卻行平方

# 而半之，即木長數
木長 = Fraction(木平方).sqrt()

# 轉換為丈
a = 木長 / 10  # 尺轉丈
#----- content ends here -----


"""

"""


"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
