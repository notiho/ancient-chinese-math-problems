"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys an item. If each person contributes 8 units of money, there is an excess of 3 units. If each person contributes 7 units of money, there is a shortage of 4 units.
Question: how many people are there, and what is the price of the item?

Answer: there are *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# Let the number of people be x and the price of the item be y.
# Equation 1: 8x = y + 3  (when each person contributes 8, there is an excess of 3)
# Equation 2: 7x = y - 4  (when each person contributes 7, there is a shortage of 4)

# Solve for y in terms of x using Equation 1
# y = 8x - 3

# Substitute y into Equation 2
# 7x = (8x - 3) - 4
# 7x = 8x - 7
# x = 7 (number of people)

# Substitute x back into Equation 1 to find y
# y = 8x - 3
# y = 8(7) - 3
# y = 56 - 3
# y = 53 (price of the item)

# Final answers
a = 7  # number of people
b = 53  # price of the item

# Output the results
a, b#----- content ends here -----

"""
"""
