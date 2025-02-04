"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
This problem involves distributing 6930 coins among 216 people divided into three groups, with each group receiving a different share of coins. Here's the solution encoded in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total coins
total_coins = 6930

# Number of people in each group
group_1_people = 81  # Two parts
group_2_people = 72  # Three parts
group_3_people = 63  # Four parts

# Multipliers for each group
group_1_multiplier = 2
group_2_multiplier = 3
group_3_multiplier = 4

# Calculate the total divisor (法)
group_1_contribution = group_1_people * group_1_multiplier
group_2_contribution = group_2_people * group_2_multiplier
group_3_contribution = group_3_people * group_3_multiplier
total_divisor = group_1_contribution + group_2_contribution + group_3_contribution

# Calculate the total shares for each group
group_1_total_share = total_coins * group_1_contribution
group_2_total_share = total_coins * group_2_contribution
group_3_total_share = total_coins * group_3_contribution

# Divide each group's total share by the total divisor
group_1_coins = Fraction(group_1_total_share, total_divisor)
group_2_coins = Fraction(group_2_total_share, total_divisor)
group_3_coins = Fraction(group_3_total_share, total_divisor)

# Divide each group's coins by the number of people in that group
group_1_per_person = Fraction(group_1_coins, group_1_people)
group_2_per_person = Fraction(group_2_coins, group_2_people)
group_3_per_person = Fraction(group_3_coins, group_3_people)

# Results
a = group_1_per_person
b = group_2_per_person
c = group_3_per_person

print(f"Two-part group gets {a} coins per person.")
print(f"Three-part group gets {b} coins per person.")
print(f"Four-part group gets {c} coins per person.")
#----- content ends here -----


"""


### Explanation:
1. **Input Data**:
   - Total coins: 6930.
   - Groups: 81 people (2 parts), 72 people (3 parts), 63 people (4 parts).

2. **Procedure**:
   - Multiply the number of people in each group by their respective multipliers (2, 3, 4).
   - Add these contributions to get the total divisor (法).
   - Multiply the total coins by each group's contribution to get the total share for each group.
   - Divide the total share for each group by the total divisor to get the coins allocated to each group.
   - Finally, divide the coins allocated to each group by the number of people in that group to get the coins per person.

3. **Output**:
   - `a`: Coins per person in the two-part group.
   - `b`: Coins per person in the three-part group.
   - `c`: Coins per person in the four-part group.

"""


"""
"""
