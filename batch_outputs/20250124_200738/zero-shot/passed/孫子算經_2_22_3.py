"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The solution involves calculating the amount of money each group of people receives based on the given proportions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 6930  # Total money in units
total_people = 216  # Total number of people
group1_people = 81  # Number of people in group 1
group2_people = 72  # Number of people in group 2
group3_people = 63  # Number of people in group 3

# Multipliers for each group
group1_multiplier = 2
group2_multiplier = 3
group3_multiplier = 4

# Calculate the total weight (法)
group1_weight = group1_people * group1_multiplier
group2_weight = group2_people * group2_multiplier
group3_weight = group3_people * group3_multiplier
total_weight = group1_weight + group2_weight + group3_weight

# Calculate the total money distributed to each group
group1_total_money = Fraction(total_money * group1_weight, total_weight)
group2_total_money = Fraction(total_money * group2_weight, total_weight)
group3_total_money = Fraction(total_money * group3_weight, total_weight)

# Calculate the money per person in each group
a = Fraction(group1_total_money, group1_people)  # Money per person in group 1
b = Fraction(group2_total_money, group2_people)  # Money per person in group 2
c = Fraction(group3_total_money, group3_people)  # Money per person in group 3

# Results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. **Input Data**: The total money, total people, and the number of people in each group are provided.
2. **Weight Calculation**: Each group's weight is calculated by multiplying the number of people in the group by their respective multiplier.
3. **Total Weight**: The sum of all group weights is calculated.
4. **Money Distribution**: The total money is distributed to each group based on their weight proportion.
5. **Per Person Calculation**: The money for each group is divided by the number of people in that group to find the amount each person receives.

### Output:
The variables `a`, `b`, and `c` represent the money each person in groups 1, 2, and 3 receives, respectively, as fractions.
"""


"""
"""
