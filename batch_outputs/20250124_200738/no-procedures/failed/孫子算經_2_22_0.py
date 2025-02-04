"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

#----- content starts here -----
"""
Suppose there are 6930 coins to be distributed among 216 people, divided into three groups:
- 81 people, each receiving 2 parts.
- 72 people, each receiving 3 parts.
- 63 people, each receiving 4 parts.

Question: How much money does each group collectively receive?

Answer: The group receiving 2 parts gets *a* coins, the group receiving 3 parts gets *b* coins, and the group receiving 4 parts gets *c* coins.
"""

# Total coins
total_coins = 6930

# Number of people in each group
group_2_parts = 81
group_3_parts = 72
group_4_parts = 63

# Parts per person in each group
parts_2 = 2
parts_3 = 3
parts_4 = 4

# Total parts for each group
total_parts_2 = group_2_parts * parts_2
total_parts_3 = group_3_parts * parts_3
total_parts_4 = group_4_parts * parts_4

# Total parts
total_parts = total_parts_2 + total_parts_3 + total_parts_4

# Coins per part
coins_per_part = Fraction(total_coins, total_parts)

# Coins for each group
a = total_parts_2 * coins_per_part
b = total_parts_3 * coins_per_part
c = total_parts_4 * coins_per_part

# Results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 22, Actual: 1782
Variable 'b' has wrong value. Expected: 33, Actual: 2376
Variable 'c' has wrong value. Expected: 44, Actual: 2772"""
