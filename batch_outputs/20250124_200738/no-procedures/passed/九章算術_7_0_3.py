"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. If each person contributes 8 units, there is an excess of 3 units. If each person contributes 7 units, there is a deficit of 4 units.
Question: What are the number of people (*a*) and the price of the item (*b*)?

Answer: *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# Let the number of people be `a` and the price of the item be `b`.
# From the problem, we can derive two equations:
# 1. 8a = b + 3  (when each person contributes 8 units, there is an excess of 3)
# 2. 7a = b - 4  (when each person contributes 7 units, there is a deficit of 4)

# Solve for `b` in terms of `a` from the first equation:
# b = 8a - 3

# Substitute `b` into the second equation:
# 7a = (8a - 3) - 4
# 7a = 8a - 7
# a = 7

# Substitute `a = 7` into the first equation to find `b`:
# b = 8a - 3
# b = 8(7) - 3
# b = 56 - 3
# b = 53

# Final results:
a = 7  # Number of people
b = 53  # Price of the item

# Output:
a, b  # (7 people, 53 units for the price of the item)#----- content ends here -----

"""
"""
