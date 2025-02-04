"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
荅曰： a人 ，雞價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people buys chickens together. If each person contributes 9 coins, there is an excess of 11 coins. If each person contributes 6 coins, there is a shortage of 16 coins.
Question: how many people are there, and what is the price of the chicken?

Answer: *a* people, and the price of the chicken is *b* coins.
"""

# Let the number of people be x and the price of the chicken be y.
# From the problem, we have the following equations:
# 1. 9x = y + 11  (when each person contributes 9 coins, there is an excess of 11 coins)
# 2. 6x = y - 16  (when each person contributes 6 coins, there is a shortage of 16 coins)

# Solve the equations step by step:

# From the first equation: y = 9x - 11
# Substitute y into the second equation: 6x = (9x - 11) - 16
# Simplify: 6x = 9x - 27
# Rearrange: 3x = 27
# Solve for x: x = 9

# Substitute x = 9 into the first equation to find y:
# y = 9x - 11
# y = 9(9) - 11
# y = 81 - 11
# y = 70

# Final answer:
a = 9  # number of people
b = 70  # price of the chicken in coins#----- content ends here -----

"""
"""
