"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
荅曰： a丈 。
"""

"""
Suppose there is a wall 1 zhang tall. A wooden pole is leaned against the wall, with its top level with the top of the wall. 
The base of the pole is moved 1 chi away from the wall, and the pole touches the ground.
Question: how long is the pole?

Answer: the pole is *a* zhang.
"""

# 垣高一丈 (wall height)
垣高 = 1  # in zhang

# 引木卻行一尺 (distance moved away from the wall)
移動距離 = Fraction(1, 10)  # 1 chi = 1/10 zhang

# Using the Pythagorean theorem to calculate the length of the pole
# 木長 = sqrt(垣高^2 + 移動距離^2)
a = (垣高**2 + 移動距離**2)**0.5  # length of the pole in zhang

# Convert to Fraction for exact representation
a = Fraction(a).limit_denominator()  # Final answer in zhang
"""
Variable 'a' has wrong value. Expected: 101/20, Actual: 162005/161201"""
