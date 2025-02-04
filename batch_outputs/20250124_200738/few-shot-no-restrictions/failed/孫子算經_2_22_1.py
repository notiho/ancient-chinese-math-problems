"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

#----- content starts here -----
"""
Suppose there are 6930 coins to be distributed among 216 people, divided into three groups:
- 81 people, each receiving 2 parts.
- 72 people, each receiving 3 parts.
- 63 people, each receiving 4 parts.

Question: How much does each group receive in total?

The procedure says:
1. Place the 81 people in the first position, 72 people in the second position, and 63 people in the third position.
2. Multiply the first position by 2, obtaining 162.
3. Multiply the second position by 3, obtaining 216.
4. Multiply the third position by 4, obtaining 252.
5. Add these three results together, obtaining 630 as the divisor (法).
6. Place the total coins (6930) as the dividend (實).
7. Multiply 6930 by 162 for the first position, by 216 for the second position, and by 252 for the third position.
8. Divide each result by 630 to obtain the total coins for each group.
9. Finally, divide the total coins for each group by the number of people in that group to determine how much each person in the group receives.

Answer: The group receiving 2 parts gets *a* coins, the group receiving 3 parts gets *b* coins, and the group receiving 4 parts gets *c* coins.
"""

from fractions import Fraction

# Total coins and people
total_coins = 6930
group1_people = 81
group2_people = 72
group3_people = 63

# Multipliers for each group
group1_multiplier = 2
group2_multiplier = 3
group3_multiplier = 4

# Step 1: Calculate the divisor (法)
group1_contribution = group1_people * group1_multiplier
group2_contribution = group2_people * group2_multiplier
group3_contribution = group3_people * group3_multiplier
divisor = group1_contribution + group2_contribution + group3_contribution

# Step 2: Calculate the total coins for each group
group1_total = Fraction(total_coins * group1_contribution, divisor)
group2_total = Fraction(total_coins * group2_contribution, divisor)
group3_total = Fraction(total_coins * group3_contribution, divisor)

# Step 3: Calculate the coins per person for each group
group1_per_person = group1_total / group1_people
group2_per_person = group2_total / group2_people
group3_per_person = group3_total / group3_people

# Results
a = group1_total
b = group2_total
c = group3_total

# Print the results
print(f"Group 1 (2 parts per person) gets a total of {a} coins.")
print(f"Group 2 (3 parts per person) gets a total of {b} coins.")
print(f"Group 3 (4 parts per person) gets a total of {c} coins.")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 22, Actual: 1782
Variable 'b' has wrong value. Expected: 33, Actual: 2376
Variable 'c' has wrong value. Expected: 44, Actual: 2772"""
