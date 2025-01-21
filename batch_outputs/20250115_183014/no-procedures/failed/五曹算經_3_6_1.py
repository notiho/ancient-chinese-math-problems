"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
答曰： a枚 奇 b文 。
"""

"""
Suppose there are 27 guan and 833 wen in total. Every 5 wen can buy 3 pears.
Question: how many pears can be bought, and how much money is left?

Answer: *a* pears and *b* wen remaining.
"""

# Total money in wen
total_wen = 27 * 1000 + 833

# Cost of 3 pears is 5 wen
cost_per_3_pears = 5

# Calculate total pears that can be bought
total_pears = (total_wen // cost_per_3_pears) * 3

# Calculate remaining money
remaining_wen = total_wen % cost_per_3_pears

# Calculate the number of pears
a = total_pears
b = remaining_wen

a, b
"""
Variable 'a' has wrong value. Expected: 16699, Actual: 16698
Variable 'b' has wrong value. Expected: 4, Actual: 3"""
