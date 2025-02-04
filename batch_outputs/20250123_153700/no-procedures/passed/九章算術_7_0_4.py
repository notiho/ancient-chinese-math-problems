"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
荅曰： a人 ，物價 b 。
"""

"""
Suppose a group of people jointly buys an item. If each person contributes 8 units of money, there is a surplus of 3 units. If each person contributes 7 units of money, there is a deficit of 4 units.
Question: how many people are there, and what is the price of the item?

Answer: there are *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# Let the number of people be x and the price of the item be y.
# From the problem, we have the following equations:
# 1. 8x - y = 3  (when each person contributes 8, there is a surplus of 3)
# 2. 7x - y = -4 (when each person contributes 7, there is a deficit of 4)

# Subtract the second equation from the first to eliminate y:
# (8x - y) - (7x - y) = 3 - (-4)
# x = 7

# Substitute x = 7 into the first equation to solve for y:
# 8x - y = 3
# 8(7) - y = 3
# 56 - y = 3
# y = 56 - 3
# y = 53

# Final results
a = 7  # number of people
b = 53  # price of the item

a, b  # Output the results
"""
"""
