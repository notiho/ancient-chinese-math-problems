"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the circumference of a circle given its area (積, "area") in steps (步). The formula provided is:

1. Multiply the area by 12.
2. Take the square root of the result.
3. The result is the circumference (周, "a").

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
area = Fraction(300)  # Area in steps

# Calculation
a = math.sqrt(area * 12)  # Circumference in steps

# Result
a  # This is the circumference in steps
#----- content ends here -----


"""


The variable `a` will store the circumference in steps. Note that we use `math.sqrt` to compute the square root.
"""


"""
"""
