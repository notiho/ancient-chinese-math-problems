"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the circumference of a circle given its area (積, "area") is 300 square steps (步). The formula provided in the problem is:

1. Multiply the area by 12.
2. Take the square root of the result.
3. The result is the circumference (周).

Here is the Python code to compute the circumference:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given area
area = 300  # in square steps

# Step 1: Multiply the area by 12
step1 = area * 12

# Step 2: Take the square root of the result
a = math.sqrt(step1)  # circumference in steps

# The result is stored in variable 'a'
#----- content ends here -----


"""


The circumference `a` is computed in steps (步).
"""


"""
"""
