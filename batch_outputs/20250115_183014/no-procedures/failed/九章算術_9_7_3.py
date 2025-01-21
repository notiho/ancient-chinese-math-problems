"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
荅曰： a丈 。
"""

"""
Suppose there is a wall 1 zhang high. A wooden pole is leaned against the wall, with its top level with the top of the wall.
If the base of the pole is moved 1 chi away from the wall, the pole touches the ground.
Question: how long is the wooden pole?

Answer: the wooden pole is *a* zhang.
"""

# 垣高一丈 (wall height)
垣高 = 1  # in zhang

# 引木卻行一尺 (distance moved away from the wall)
移動距離 = Fraction(1, 10)  # 1 chi = 1/10 zhang

# Using the Pythagorean theorem: 木長^2 = 垣高^2 + 移動距離^2
木長平方 = 垣高**2 + 移動距離**2

# 木長 = sqrt(木長平方)
# Since we cannot use external libraries, we represent the square root as a Fraction:
木長 = Fraction(垣高**2 + 移動距離**2).sqrt()

a = 木長  # 木長 in zhang
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
