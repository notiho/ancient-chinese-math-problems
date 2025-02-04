"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
荅曰： a人 ，雞價 b 。
"""

"""
Suppose a group of people buys chickens. If each person contributes 9 coins, there is a surplus of 11 coins. 
If each person contributes 6 coins, there is a deficit of 16 coins. 
Question: how many people are there, and what is the price of the chickens?

Answer: there are *a* people, and the price of the chickens is *b* coins.
"""

# Let the number of people be x and the price of the chickens be y.
# From the problem, we have the following equations:
# 1. 9x - y = 11  (surplus of 11 coins when each person contributes 9)
# 2. 6x - y = -16 (deficit of 16 coins when each person contributes 6)

from fractions import Fraction

# Solve for x (number of people) and y (price of chickens)
# Subtract the second equation from the first:
# (9x - y) - (6x - y) = 11 - (-16)
# 3x = 27
x = Fraction(27, 3)

# Substitute x into the first equation to solve for y:
# 9x - y = 11
y = 9 * x - 11

# Results
a = x  # Number of people
b = y  # Price of chickens

a, b  # Output the results
"""
"""
