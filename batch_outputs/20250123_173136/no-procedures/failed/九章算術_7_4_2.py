"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
荅曰： a人 。金價 b 。
"""

"""
Suppose a group of people jointly buys gold. If each person contributes 400, there is a surplus of 3400. If each person contributes 300, there is a surplus of 100.
Question: how many people are there, and what is the price of the gold?

Answer: there are *a* people, and the price of the gold is *b*.
"""

# Let:
# x = number of people
# y = price of the gold

# Equation 1: 400x - y = 3400
# Equation 2: 300x - y = 100

# Solve for x and y
from fractions import Fraction

# Subtract the second equation from the first
# (400x - y) - (300x - y) = 3400 - 100
100 * x = 3300
x = Fraction(3300, 100)

# Substitute x into the first equation to solve for y
y = 400 * x - 3400

# Final results
a = x  # number of people
b = y  # price of the gold

a, b
"""
Code error: cannot assign to expression here. Maybe you meant '==' instead of '='? (<string>, line 21)"""
