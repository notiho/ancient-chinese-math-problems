"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that the area of a circle is given as 300 steps, and we need to compute the circumference of the circle using the provided formula.

The formula is:
1. Multiply the area by 12.
2. Take the square root of the result.
3. The result is the circumference.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
area = Fraction(300)  # Area in steps

# Step 1: Multiply the area by 12
step1 = area * 12

# Step 2: Take the square root of the result
a = Fraction(math.sqrt(step1))

# The circumference is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the circumference of the circle in steps.
"""


"""
"""
