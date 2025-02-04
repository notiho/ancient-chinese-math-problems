"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a wall 1 zhang high. A wooden pole leans against the wall, with its top level with the top of the wall.
If the base of the pole is pulled 1 chi away from the wall, the pole touches the ground.
Question: how long is the pole?

Answer: the pole is *a* zhang.
"""

# 垣高一丈 (wall height)
垣高 = 1  # in zhang

# 引木卻行一尺 (distance from the wall)
距離 = Fraction(1, 10)  # 1 chi = 1/10 zhang

# Use the Pythagorean theorem to calculate the length of the pole
# 木長^2 = 垣高^2 + 距離^2
木長平方 = 垣高**2 + 距離**2

# 木長 = sqrt(木長平方)
木長 = 木長平方**Fraction(1, 2)

# Answer
a = 木長  # in zhang

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 101/20, Actual: 1.004987562112089"""
