"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100 coins, there is a surplus of 100 coins. If each person contributes 90 coins, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

Answer: there are *a* people, and the price of the pig is *b* coins.
"""

# Let the number of people be x and the price of the pig be y
# From the problem, we have the following equations:
# 1. 100x = y + 100  (when each person contributes 100 coins, there is a surplus of 100 coins)
# 2. 90x = y         (when each person contributes 90 coins, the amount is exactly sufficient)

# Solving the equations:
# From equation 2, y = 90x
# Substitute y = 90x into equation 1:
# 100x = 90x + 100
# 10x = 100
# x = 10 (number of people)

# Substitute x = 10 into equation 2:
# y = 90x
# y = 90 * 10
# y = 900 (price of the pig)

# Final answers:
a = 10  # Number of people
b = 900  # Price of the pig#----- content ends here -----

"""
"""
