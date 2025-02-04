"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing a total amount of money among three groups of people based on specific ratios. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 6930  # Total money in units
group1_people = 81  # People in the first group
group2_people = 72  # People in the second group
group3_people = 63  # People in the third group

# Ratios for each group
group1_ratio = 2
group2_ratio = 3
group3_ratio = 4

# Step 1: Calculate the weighted sums for each group
group1_weight = group1_people * group1_ratio  # 81 * 2
group2_weight = group2_people * group2_ratio  # 72 * 3
group3_weight = group3_people * group3_ratio  # 63 * 4

# Total weight
total_weight = group1_weight + group2_weight + group3_weight

# Step 2: Calculate the total weighted money for each group
group1_total_money = total_money * group1_weight
group2_total_money = total_money * group2_weight
group3_total_money = total_money * group3_weight

# Step 3: Divide the total weighted money by the total weight to get the money per group
group1_money = Fraction(group1_total_money, total_weight)
group2_money = Fraction(group2_total_money, total_weight)
group3_money = Fraction(group3_total_money, total_weight)

# Step 4: Divide the money for each group by the number of people in that group
a = group1_money / group1_people  # Money per person in group 1
b = group2_money / group2_people  # Money per person in group 2
c = group3_money / group3_people  # Money per person in group 3

# Results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. **Input Values**: The total money, number of people in each group, and the ratios are provided.
2. **Weighted Sums**: Calculate the weighted sums for each group based on the number of people and their respective ratios.
3. **Total Weight**: Sum up the weights for all groups.
4. **Weighted Money**: Multiply the total money by the weight of each group.
5. **Money per Group**: Divide the weighted money by the total weight to find the money allocated to each group.
6. **Money per Person**: Divide the money for each group by the number of people in that group to find the money each person receives.

The variables `a`, `b`, and `c` represent the money each person in the respective groups receives.
"""


"""
"""
