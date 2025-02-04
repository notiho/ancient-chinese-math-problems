"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen in total. Each 5 wen can buy 3 pears.
Question: how many pears can be bought, and how much money is left?

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# Total money in wen
total_money = 27 * 1000 + 833  # 1 guan = 1000 wen

# Cost of 3 pears is 5 wen
cost_per_3_pears = 5

# Calculate total pears that can be bought
total_pears = (total_money // cost_per_3_pears) * 3

# Remaining money
remaining_money = total_money % cost_per_3_pears

# Convert total pears into groups of 3
a = total_pears
b = remaining_money

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 16699, Actual: 16698
Variable 'b' has wrong value. Expected: 4, Actual: 3"""
