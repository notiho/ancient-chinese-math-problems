"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100 coins, there is a surplus of 100 coins. If each person contributes 90 coins, the amount is exactly enough.
Question: how many people are there, and what is the price of the pig?

Answer: there are *a* people, and the price of the pig is *b* coins.
"""

# Let the number of people be x and the price of the pig be y.
# From the problem, we have two equations:
# 1. 100x = y + 100  (when each person contributes 100 coins, there is a surplus of 100 coins)
# 2. 90x = y         (when each person contributes 90 coins, the amount is exactly enough)

# Solve for x and y
from fractions import Fraction

# Equation 1: y = 100x - 100
# Equation 2: y = 90x

# Set the two equations for y equal to each other:
# 100x - 100 = 90x
# Simplify:
x = 10  # Number of people

# Substitute x into one of the equations to find y:
y = 90 * x  # Price of the pig
y = 900

# Final answers
a = x  # Number of people
b = y  # Price of the pig

a, b  # Output the results#----- content ends here -----

"""
"""
