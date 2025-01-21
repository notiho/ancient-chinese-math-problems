"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""
To solve the problem, we will follow the given method:

1. Multiply the given area (積) by 12.
2. Take the square root of the result.
3. The result is the circumference (圓周).

Here is the Python code:


"""


from fractions import Fraction
from math import sqrt

# Given data
area = Fraction(1518) + Fraction(3, 4)  # 1518步 and 3/4步

# Step 1: Multiply the area by 12
area_times_12 = area * 12

# Step 2: Take the square root
a = sqrt(area_times_12)

# The circumference (圓周) is stored in variable 'a'


"""


The variable `a` now contains the circumference in steps (步).
"""


"""
"""
