"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
荅曰： a人 ，犬價 b 。
"""

"""
Suppose a group of people collectively buys a dog. If each person contributes 5, the total is 90 less than the required amount. If each person contributes 50, the total is exactly enough.
Question: how many people are there, and what is the price of the dog?

Answer: there are *a* people, and the price of the dog is *b*.
"""

# Let the number of people be x and the price of the dog be y.
# From the problem, we have the following equations:
# 1. 5x + 90 = y
# 2. 50x = y

# Solve for x and y
from fractions import Fraction

# Equation 1: y = 5x + 90
# Equation 2: y = 50x

# Set the two equations equal to each other:
# 5x + 90 = 50x
# Solve for x:
a = Fraction(90, 45)  # a = 2

# Substitute x = a into one of the equations to find y:
b = 50 * a  # b = 100

# Final result:
a人 = a
b價 = b

a人, b價
"""
"""
