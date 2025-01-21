"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a wall of height 1丈 (10尺) and a leaning stick. The stick is moved 1尺 away from the wall, and it touches the ground. We need to calculate the length of the stick.

Here is the Python code:


"""


from fractions import Fraction

# Given data
wall_height = Fraction(10)  # 1丈 = 10尺
distance_from_wall = Fraction(1)  # 1尺

# Calculation
# 木長數 = sqrt(垣高^2 + (卻行尺數)^2)
# 木長數 = sqrt(wall_height^2 + distance_from_wall^2)
# 木長數 = wall_height^2 / (distance_from_wall + wall_height)

a = (wall_height**2 + distance_from_wall**2)**0.

"""

"""


"""
Variable 'a' has wrong value. Expected: 101/20, Actual: 1.0"""
