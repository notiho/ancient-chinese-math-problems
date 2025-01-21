"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
荅曰： a人 ，雞價 b 。
"""

"""
Suppose a group of people jointly buys chickens. If each person contributes 9 coins, there is an excess of 11 coins. If each person contributes 6 coins, there is a shortage of 16 coins.
Question: how many people are there, and what is the price of the chickens?

Answer: there are *a* people, and the price of the chickens is *b* coins.
"""

# Let the number of people be x and the price of the chickens be y.
# From the problem, we have the following two equations:
# 1. 9x = y + 11  (when each person contributes 9 coins, there is an excess of 11 coins)
# 2. 6x = y - 16  (when each person contributes 6 coins, there is a shortage of 16 coins)

# Solve for x (number of people) and y (price of chickens):
from fractions import Fraction

# Subtract the second equation from the first:
# (9x - 6x) = (y + 11) - (y - 16)
# 3x = 27
x = Fraction(27, 3)

# Substitute x back into the first equation to find y:
# 9x = y + 11
y = 9 * x - 11

# Final results:
a = x  # Number of people
b = y  # Price of chickens

a, b  # Output the results
"""
"""
