"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
Suppose there are 6930 coins to be distributed among 216 people in 3 groups, divided into 9 parts:
- 81 people, each receiving 2 parts
- 72 people, each receiving 3 parts
- 63 people, each receiving 4 parts

Question: how much money does each group receive?

Answer: the group receiving 2 parts gets *a* coins, the group receiving 3 parts gets *b* coins, and the group receiving 4 parts gets *c* coins.
"""

# Total coins
total_coins = 6930

# Total parts = (81 people * 2 parts) + (72 people * 3 parts) + (63 people * 4 parts)
total_parts = (81 * 2) + (72 * 3) + (63 * 4)

# Value of one part
value_per_part = Fraction(total_coins, total_parts)

# Coins for each group
a = 81 * 2 * value_per_part  # Coins for the group receiving 2 parts
b = 72 * 3 * value_per_part  # Coins for the group receiving 3 parts
c = 63 * 4 * value_per_part  # Coins for the group receiving 4 parts

# Results
a, b, c
"""
Variable 'a' has wrong value. Expected: 22, Actual: 1782
Variable 'b' has wrong value. Expected: 33, Actual: 2376
Variable 'c' has wrong value. Expected: 44, Actual: 2772"""
