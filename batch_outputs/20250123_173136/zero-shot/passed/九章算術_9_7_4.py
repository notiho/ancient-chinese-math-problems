"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
垣高 = Fraction(1)  # in 丈
垣高_in_尺 = 垣高 * 10  # convert 丈 to 尺
卻行 = Fraction(1)  # in 尺

# Calculation
木長 = (垣高_in_尺 ** 2 + 卻行 ** 2) / (2 * 卻行)

# Answer
a = 木長 / 10  # convert back to 丈


"""


The solution is stored in the variable `a`, which represents the length of the wood in 丈.
"""


"""
"""
