"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
荅曰： a人 ，豕價 b 。
"""

"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is an excess of 100. If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

Answer: there are *a* people, and the price of the pig is *b*.
"""

# Let x represent the number of people (人數)
# Let y represent the price of the pig (豕價)

# Equation 1: 100x - y = 100 (excess of 100 when each contributes 100)
# Equation 2: 90x = y (exactly sufficient when each contributes 90)

# Solve for x and y
from fractions import Fraction

# From Equation 2, y = 90x
# Substitute y = 90x into Equation 1:
# 100x - 90x = 100
# 10x = 100
x = 10  # 人數

# Substitute x = 10 into Equation 2 to find y:
y = 90 * x  # 豕價
y = 900

# Final answer
a = x  # 人數
b = y  # 豕價

a, b  # Output the results
"""
"""
