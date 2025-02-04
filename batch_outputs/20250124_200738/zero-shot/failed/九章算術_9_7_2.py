"""
今有垣高一丈。倚木於垣，上與垣齊。引木卻行一尺，其木至地。問︰木幾何？
術曰：以垣高十尺自乘，如卻行尺數而一，所得，以加卻行尺數而半之，即木長數。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a wall of height 1丈 (10尺) and a leaning stick that touches the top of the wall and the ground. When the base of the stick is moved 1尺 away from the wall, the stick touches the ground. We are tasked with finding the length of the stick.

The solution involves the following steps:
1. Square the height of the wall (10尺).
2. Add the square of the distance the base of the stick is moved away from the wall (1尺).
3. Take the square root of the sum to find the length of the stick.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
wall_height = Fraction(10)  # 1丈 = 10尺
distance_moved = Fraction(1)  # 1尺

# Compute the length of the stick
a = math.sqrt(float(wall_height**2 + distance_moved**2))

# Convert the result back to Fraction for exact representation
a = Fraction(a).limit_denominator()

# The length of the stick is stored in variable 'a'
#----- content ends here -----


"""


The length of the stick (`a`) is computed in 丈 (10尺 = 1丈).
"""


"""
Variable 'a' has wrong value. Expected: 101/20, Actual: 1620050/161201"""
