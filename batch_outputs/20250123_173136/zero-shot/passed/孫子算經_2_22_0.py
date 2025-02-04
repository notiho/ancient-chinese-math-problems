"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
total_money = 6930  # Total money
people_2 = 81       # People getting 2 parts
people_3 = 72       # People getting 3 parts
people_4 = 63       # People getting 4 parts

# Calculating the weights for each group
weight_2 = people_2 * 2  # 81 * 2
weight_3 = people_3 * 3  # 72 * 3
weight_4 = people_4 * 4  # 63 * 4

# Total weight
total_weight = weight_2 + weight_3 + weight_4  # 162 + 216 + 252

# Calculating the total money distributed to each group
money_2 = Fraction(weight_2 * total_money, total_weight)  # (162 * 6930) / 630
money_3 = Fraction(weight_3 * total_money, total_weight)  # (216 * 6930) / 630
money_4 = Fraction(weight_4 * total_money, total_weight)  # (252 * 6930) / 630

# Calculating the money per person in each group
a = Fraction(money_2, people_2)  # Money per person in group 2 parts
b = Fraction(money_3, people_3)  # Money per person in group 3 parts
c = Fraction(money_4, people_4)  # Money per person in group 4 parts

# Results
a, b, c


"""


### Explanation:
1. **Weights Calculation**:
   - Each group contributes a weight based on the number of people and the parts they receive (e.g., `weight_2 = 81 * 2`).

2. **Total Weight**:
   - The sum of all weights is calculated (`total_weight = weight_2 + weight_3 + weight_4`).

3. **Money Distribution**:
   - The total money is distributed proportionally to the weights (`money_2`, `money_3`, `money_4`).

4. **Money Per Person**:
   - The money for each group is divided by the number of people in that group to find the money per person (`a`, `b`, `c`).

### Final Values:
- `a`: Money per person for the group receiving 2 parts.
- `b`: Money per person for the group receiving 3 parts.
- `c`: Money per person for the group receiving 4 parts.
"""


"""
"""
