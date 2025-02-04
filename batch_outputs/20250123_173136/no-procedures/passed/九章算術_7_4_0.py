"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
荅曰： a人 。金價 b 。
"""

"""
Suppose a group of people jointly buy gold. If each person contributes 400, there is a surplus of 3400. If each person contributes 300, there is a surplus of 100.
Question: How many people are there, and what is the price of the gold?

Answer: There are *a* people, and the price of the gold is *b*.
"""

# Let:
# x = number of people (a)
# y = price of the gold (b)

# Equation 1: 400x - y = 3400
# Equation 2: 300x - y = 100

from fractions import Fraction

# Solve for x (number of people)
x = Fraction(3400 - 100, 400 - 300)

# Solve for y (price of the gold)
y = 400 * x - 3400

# Results
a = x
b = y

a, b
"""
"""
