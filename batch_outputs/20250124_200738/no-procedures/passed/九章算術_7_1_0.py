"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
荅曰： a人 ，雞價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people buys chickens together. If each person contributes 9 coins, there is an excess of 11 coins. If each person contributes 6 coins, there is a shortage of 16 coins.
Question: how many people are there, and what is the price of the chickens?

Answer: there are *a* people, and the price of the chickens is *b* coins.
"""

# Let the number of people be `a` and the price of the chickens be `b`.
# From the problem, we have the following equations:
# 1. 9a = b + 11  (when each person contributes 9 coins, there is an excess of 11 coins)
# 2. 6a = b - 16  (when each person contributes 6 coins, there is a shortage of 16 coins)

# Solve for `a` and `b`:
# From the first equation: b = 9a - 11
# Substitute b into the second equation:
# 6a = (9a - 11) - 16
# 6a = 9a - 27
# 3a = 27
# a = 9

# Substitute a = 9 into the first equation to find b:
# b = 9a - 11
# b = 9(9) - 11
# b = 81 - 11
# b = 70

# Final results:
a = 9  # number of people
b = 70  # price of the chickens in coins#----- content ends here -----

"""
"""
