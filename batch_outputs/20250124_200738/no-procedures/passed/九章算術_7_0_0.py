"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. If each person contributes 8 units of money, there is an excess of 3 units. If each person contributes 7 units of money, there is a shortage of 4 units.
Question: how many people are there, and what is the price of the item?

Answer: there are *a* people, and the price of the item is *b*.
"""

# Let the number of people be x and the price of the item be y.
# From the problem, we have the following equations:
# 8x = y + 3  (Equation 1: when each person contributes 8, there is an excess of 3)
# 7x = y - 4  (Equation 2: when each person contributes 7, there is a shortage of 4)

# Solve for x and y using the equations.

from fractions import Fraction

# Equation 1: y = 8x - 3
# Equation 2: y = 7x + 4

# Set the two equations for y equal to each other:
# 8x - 3 = 7x + 4
# Solve for x:
x = 7  # Number of people

# Substitute x back into one of the equations to solve for y:
y = 8 * x - 3  # Price of the item

# Final answers:
a = x  # Number of people
b = y  # Price of the item

a, b  # Output the results#----- content ends here -----

"""
"""
