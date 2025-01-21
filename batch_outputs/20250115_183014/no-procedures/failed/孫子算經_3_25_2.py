"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
答曰： a 獸 b 禽。
"""

"""
Suppose there are beasts (each with 6 heads and 4 legs) and birds (each with 2 heads and 2 legs).
In total, there are 76 heads and 46 legs.
Question: how many beasts and birds are there?

Answer: *a* beasts and *b* birds.
"""

# Let the number of beasts be x and the number of birds be y
# Each beast has 6 heads and 4 legs
# Each bird has 2 heads and 2 legs

# Total heads equation: 6x + 2y = 76
# Total legs equation: 4x + 2y = 46

# Solve the system of equations
from fractions import Fraction

# Step 1: Eliminate y by subtracting the second equation from the first
# (6x + 2y) - (4x + 2y) = 76 - 46
# 2x = 30
x = Fraction(30, 2)  # Number of beasts

# Step 2: Substitute x into one of the equations to solve for y
# Using the second equation: 4x + 2y = 46
y = Fraction(46 - 4 * x, 2)  # Number of birds

# Final result
a = x  # Number of beasts
b = y  # Number of birds

a, b  # Output the result
"""
Variable 'a' has wrong value. Expected: 8, Actual: 15
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
