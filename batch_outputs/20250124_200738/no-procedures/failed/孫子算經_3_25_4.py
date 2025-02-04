"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
答曰： a 獸 b 禽。
"""

#----- content starts here -----
"""
Suppose there are beasts (each with 6 heads and 4 legs) and birds (each with 2 heads and 2 legs). 
The total number of heads is 76, and the total number of legs is 46.
Question: how many beasts and birds are there?

Answer: *a* beasts and *b* birds.
"""

# Let x represent the number of beasts and y represent the number of birds.
# We have the following system of equations:
# 6x + 2y = 76  (total heads)
# 4x + 2y = 46  (total legs)

# Solve for x and y
from fractions import Fraction

# Subtract the second equation from the first to eliminate y:
# (6x + 2y) - (4x + 2y) = 76 - 46
# 2x = 30
x = Fraction(30, 2)  # x = 15 (number of beasts)

# Substitute x into the first equation to solve for y:
# 6(15) + 2y = 76
# 90 + 2y = 76
# 2y = 76 - 90
# 2y = -14
y = Fraction(-14, 2)  # y = -7 (number of birds)

a = x
b = y#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: 15
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
