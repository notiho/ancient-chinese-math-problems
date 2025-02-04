"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 6930  # Total money
people_2_parts = 81  # People receiving 2 parts
people_3_parts = 72  # People receiving 3 parts
people_4_parts = 63  # People receiving 4 parts

# Calculating the weights for each group
weight_2_parts = 2 * people_2_parts  # 2 * 81
weight_3_parts = 3 * people_3_parts  # 3 * 72
weight_4_parts = 4 * people_4_parts  # 4 * 63

# Total weight
total_weight = weight_2_parts + weight_3_parts + weight_4_parts

# Calculating the total money distributed to each group
money_2_parts = Fraction(weight_2_parts * total_money, total_weight)
money_3_parts = Fraction(weight_3_parts * total_money, total_weight)
money_4_parts = Fraction(weight_4_parts * total_money, total_weight)

# Calculating the money per person in each group
a = Fraction(money_2_parts, people_2_parts)  # Money per person in group 2 parts
b = Fraction(money_3_parts, people_3_parts)  # Money per person in group 3 parts
c = Fraction(money_4_parts, people_4_parts)  # Money per person in group 4 parts

# Results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. **Weights Calculation**:
   - Each group has a weight based on the number of people and the parts they receive (2, 3, or 4 parts).
   - Multiply the number of people in each group by their respective parts to get the weight.

2. **Total Weight**:
   - Add up the weights of all groups to get the total weight.

3. **Money Distribution**:
   - Distribute the total money proportionally to each group based on their weight.

4. **Money Per Person**:
   - Divide the money received by each group by the number of people in that group to get the money per person.

### Output:
The variables `a`, `b`, and `c` will contain the money per person for the groups receiving 2 parts, 3 parts, and 4 parts respectively, represented as fractions.
"""


"""
"""
