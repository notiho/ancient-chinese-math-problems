"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buy a pig. If each person contributes 100, there is an excess of 100. If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

Answer: there are *a* people, and the price of the pig is *b*.
"""

# Let the number of people be x and the price of the pig be y.
# From the problem, we have the following two equations:
# 1. 100x = y + 100  (when each person contributes 100, there is an excess of 100)
# 2. 90x = y         (when each person contributes 90, the amount is exactly sufficient)

# Solve for x (number of people) and y (price of the pig):
from fractions import Fraction

# Equation 1: y = 100x - 100
# Equation 2: y = 90x
# Set the two equations for y equal to each other:
# 100x - 100 = 90x
# Solve for x:
a = 10  # Number of people

# Substitute x = 10 into y = 90x to find the price of the pig:
b = 90 * a  # Price of the pig

# Results:
a, b  # a = number of people, b = price of the pig#----- content ends here -----

"""
"""
