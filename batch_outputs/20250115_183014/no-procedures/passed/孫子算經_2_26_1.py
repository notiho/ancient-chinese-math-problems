"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
答曰：賊 a人 ，絹 b匹 。
"""

"""
Suppose someone has stolen silk from a storehouse, but the exact amount of silk is unknown. 
It is only known that when the silk is divided among the people in the grass, each person gets 6 bolts of silk with 6 bolts left over. 
If each person gets 7 bolts of silk, there are not enough bolts for everyone.

Question: How many people (a) and how many bolts of silk (b) are there?

Answer: There are *a* people and *b* bolts of silk.
"""

from fractions import Fraction

# Let the number of people be a and the number of bolts of silk be b.
# From the problem:
# b = 6a + 6  (1)
# b = 7a - r, where r > 0 (remainder when divided by 7) (2)

# Solve for a and b such that both conditions are satisfied.
# From (1), substitute b into (2):
# 6a + 6 = 7a - r
# r = 7a - 6a - 6
# r = a - 6

# r must be a positive remainder, so a > 6.
# Additionally, b must be divisible by 6 (from (1)) and leave a remainder of 0 when divided by 7 (from (2)).

# Start testing values of a > 6 to find the smallest solution.
for a in range(7, 100):  # Start from 7 (a > 6)
    b = 6 * a + 6  # From equation (1)
    if b % 7 == 0:  # Check if b satisfies equation (2)
        break

# Output the results
a, b  # a is the number of people, b is the number of bolts of silk
"""
"""
