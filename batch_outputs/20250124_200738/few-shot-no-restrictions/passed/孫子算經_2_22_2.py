"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

#----- content starts here -----
"""
Suppose there are 6930 coins to be distributed among 216 people in 3 groups:
- 81 people, each receiving 2 parts,
- 72 people, each receiving 3 parts,
- 63 people, each receiving 4 parts.

Question: how much does each group receive?

The procedure says:
1. Place the 81 people at the top, 72 people in the middle, and 63 people at the bottom.
2. Multiply the top position by 2, obtaining 162.
   Multiply the middle position by 3, obtaining 216.
   Multiply the bottom position by 4, obtaining 252.
3. Add these three results together, obtaining 630 as the divisor.
4. Place the 6930 coins as the total. Multiply it by 162 for the top position, obtaining 1122660.
   Multiply it by 216 for the middle position, obtaining 1496880.
   Multiply it by 252 for the bottom position, obtaining 1746360.
5. Divide each of these results by 630, obtaining the total coins for each group.
6. Divide the total coins for each group by the number of people in that group to find the coins per person.

Answer: The group receiving 2 parts gets *a* coins per person, the group receiving 3 parts gets *b* coins per person, and the group receiving 4 parts gets *c* coins per person.
"""

from fractions import Fraction

# Total coins and group sizes
total_coins = 6930
group_2_people = 81
group_3_people = 72
group_4_people = 63

# Step 1: Calculate the weights for each group
weight_2 = 2 * group_2_people  # 81 * 2
weight_3 = 3 * group_3_people  # 72 * 3
weight_4 = 4 * group_4_people  # 63 * 4

# Step 2: Calculate the total weight (法)
total_weight = weight_2 + weight_3 + weight_4  # 162 + 216 + 252 = 630

# Step 3: Calculate the total coins for each group
coins_2_total = Fraction(total_coins * weight_2, total_weight)
coins_3_total = Fraction(total_coins * weight_3, total_weight)
coins_4_total = Fraction(total_coins * weight_4, total_weight)

# Step 4: Calculate coins per person for each group
a = Fraction(coins_2_total, group_2_people)  # Coins per person in group 2
b = Fraction(coins_3_total, group_3_people)  # Coins per person in group 3
c = Fraction(coins_4_total, group_4_people)  # Coins per person in group 4

# Output results
a, b, c#----- content ends here -----

"""
"""
