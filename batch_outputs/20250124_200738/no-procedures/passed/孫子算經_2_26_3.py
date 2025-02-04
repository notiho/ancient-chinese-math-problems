"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone stole silk from a storehouse, but the exact amount of silk is unknown. 
It is only known that when the silk is divided among the people in the grass, each person gets 6 bolts of silk with 6 bolts left over. 
If each person is given 7 bolts of silk, there is not enough to give everyone 7 bolts.

Question: How many people (a) and how many bolts of silk (b) are there?

Answer: There are *a* people and *b* bolts of silk.
"""

from fractions import Fraction

# Let the number of people be `a` and the total silk be `b`.
# From the problem:
# b = 6a + 6  (1)
# b = 7a - r, where r > 0 (remainder when dividing by 7) (2)

# Combine the two equations:
# 6a + 6 = 7a - r
# r = 7a - 6a - 6
# r = a - 6

# Since r > 0, we know a > 6.

# Solve for a and b:
for a in range(7, 100):  # Start from 7 (since a > 6) and test values
    b = 6 * a + 6  # From equation (1)
    if b % 7 == 0:  # Check if b satisfies equation (2)
        break

# Final results
a = Fraction(a)  # Number of people
b = Fraction(b)  # Total bolts of silk

a, b  # Output the results#----- content ends here -----

"""
"""
