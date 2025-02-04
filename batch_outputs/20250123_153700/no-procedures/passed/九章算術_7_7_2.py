"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
荅曰： a人 ，犬價 b 。
"""

"""
Suppose a group of people wants to buy a dog. If each person contributes 5, the total is 90 less than the required amount. If each person contributes 50, the total is exactly enough.
Question: how many people are there, and what is the price of the dog?

Answer: there are *a* people, and the price of the dog is *b*.
"""

# Let the number of people be x and the price of the dog be y.
# From the problem, we have the following equations:
# 1. 5 * x + 90 = y
# 2. 50 * x = y

# Solve for x and y
from fractions import Fraction

# Equation 1: y = 5 * x + 90
# Equation 2: y = 50 * x
# Set the two equations equal to each other:
# 5 * x + 90 = 50 * x
# Solve for x:
x = Fraction(90, 45)  # x = 2

# Substitute x into one of the equations to find y:
y = 50 * x  # y = 50 * 2 = 100

# Final answers
a = x  # Number of people
b = y  # Price of the dog

a, b  # Output the results
"""
"""
