"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone has stolen silk from the storehouse, but the exact amount is unknown. 
It is only known that when the silk is divided among the thieves, if each person gets 6 pi, there are 6 pi left over; 
if each person gets 7 pi, there are not enough for everyone. 

Question: how many thieves and how much silk are there?

Answer: there are *a* thieves, and *b* pi of silk.
"""

# We need to solve for the number of thieves (a) and the amount of silk (b).
# Let `a` be the number of thieves and `b` be the total amount of silk.
# The conditions are:
# 1. b = 6a + 6 (when each person gets 6 pi, 6 pi are left over)
# 2. b = 7a - r (when each person gets 7 pi, there is a shortage, so r > 0)

# We solve this using modular arithmetic:
# From condition 1: b ≡ 6 (mod 6)
# From condition 2: b ≡ 0 (mod 7)

# Find the smallest b that satisfies both conditions:
from fractions import Fraction

# Initialize variables
a = 0  # Number of thieves
b = 0  # Amount of silk

# Solve using brute force
while True:
    b += 7  # b must be a multiple of 7
    if b % 6 == 6:  # b must leave a remainder of 6 when divided by 6
        a = (b - 6) // 6  # Calculate the number of thieves
        break

# Output the results
a, b  # a is the number of thieves, b is the amount of silk#----- content ends here -----

"""
Timed out"""
