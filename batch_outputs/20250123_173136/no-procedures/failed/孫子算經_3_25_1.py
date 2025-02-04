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

# Let:
# x = number of beasts
# y = number of birds

# Equation 1: 6x + 2y = 76 (total heads)
# Equation 2: 4x + 2y = 46 (total legs)

# Solve the system of equations step by step:

# Step 1: Subtract Equation 2 from Equation 1 to eliminate y
# (6x + 2y) - (4x + 2y) = 76 - 46
# 2x = 30
x = Fraction(30, 2)  # Number of beasts

# Step 2: Substitute x into Equation 2 to solve for y
# 4x + 2y = 46
y = Fraction(46 - 4 * x, 2)  # Number of birds

# Final answer:
a = x  # Number of beasts
b = y  # Number of birds
"""
Variable 'a' has wrong value. Expected: 8, Actual: 15
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
