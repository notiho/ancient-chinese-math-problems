"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""
To solve this problem, we will follow the method described in the text. The given area (積) is 1518 and 3/4 steps (步). We will calculate the circumference (圓周) using the formula provided:

1. Multiply the area by 12.
2. Take the square root of the result.
3. The result is the circumference.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
area = Fraction(1518) + Fraction(3, 4)  # Area in steps

# Step 1: Multiply the area by 12
area_times_12 = area * 12

# Step 2: Take the square root of the result
# To compute the square root, we find the numerator and denominator separately
numerator_sqrt = int(area_times_12.numerator**0.5)
denominator_sqrt = int(area_times_12.denominator**0.5)

# Ensure the square root is exact (both numerator and denominator must be perfect squares)
if numerator_sqrt**2 == area_times_12.numerator and denominator_sqrt**2 == area_times_12.denominator:
    a = Fraction(numerator_sqrt, denominator_sqrt)  # Circumference in steps
else:
    a = None  # If the square root is not exact, the problem might need further clarification

# Result
a  # Circumference in steps
#----- content ends here -----


"""


This code calculates the circumference `a` in steps (步). If the square root is not exact, the variable `a` will be set to `None`.
"""


"""
"""
