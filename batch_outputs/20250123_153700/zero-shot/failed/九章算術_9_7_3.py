"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a wall of height 1丈 (10尺), and a leaning wooden pole. The pole's top is level with the top of the wall, and when the base of the pole is moved 1尺 away from the wall, the pole touches the ground. We need to calculate the length of the pole.

Here is the Python code:


"""


from fractions import Fraction

# Given values
wall_height = Fraction(10)  # 1丈 = 10尺
distance_from_wall = Fraction(1)  # 1尺

# Calculation
a = (wall_height ** 2 + distance_from_wall ** 2) / (2 * distance_from_wall)

# The length of the pole is stored in variable 'a'


"""


The variable `a` represents the length of the pole in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 101/20, Actual: 101/2"""
