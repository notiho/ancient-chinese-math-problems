"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone has stolen silk from a storehouse, but the exact amount of silk stolen is unknown. 
It is only known that when the silk is divided among the thieves such that each person gets 6 bolts of silk, there are 6 bolts left over. 
However, if each person gets 7 bolts of silk, there are not enough bolts to go around.

Question: How many thieves (people) and how many bolts of silk were stolen?

Answer: There are *a* thieves and *b* bolts of silk.
"""

# Let the number of thieves be `a` and the total number of bolts of silk be `b`.
# From the problem, we know:
# 1. b = 6a + 6 (when each person gets 6 bolts, 6 are left over)
# 2. b = 7a - r, where r > 0 (when each person gets 7 bolts, there is a shortage)

# We need to find integers `a` and `b` that satisfy both conditions.

from fractions import Fraction

# Solve the problem
for a in range(1, 100):  # Assume a reasonable range for the number of thieves
    b = 6 * a + 6  # From the first condition
    if b % 7 == 0:  # Check if b satisfies the second condition (b must be divisible by 7)
        break

# Output the results
a = a  # Number of thieves
b = b  # Total bolts of silk

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13, Actual: 6
Variable 'b' has wrong value. Expected: 84, Actual: 42"""
