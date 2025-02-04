"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is an excess of 100. If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

Answer: there are *a* people, and the price of the pig is *b*.
"""

# Let the number of people be `a` and the price of the pig be `b`.
# From the problem, we have the following equations:
# 1. 100a - b = 100  (when each person contributes 100, there is an excess of 100)
# 2. 90a = b         (when each person contributes 90, the amount is exactly sufficient)

# Solve the equations:
# From equation (2), substitute b = 90a into equation (1):
# 100a - 90a = 100
# 10a = 100
a = 100 // 10  # Number of people

# Substitute a into equation (2) to find b:
b = 90 * a  # Price of the pig

# Final result:
a, b  # a is the number of people, b is the price of the pig#----- content ends here -----

"""
"""
