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

# Cost of 3 pears in wen
cost_per_3_pears = 5

# Total pears that can be bought
a = (total_wen // cost_per_3_pears) * 3

# Remaining money in wen
b = total_wen % cost_per_3_pears
"""
Variable 'a' has wrong value. Expected: 16699, Actual: 16698
Variable 'b' has wrong value. Expected: 4, Actual: 3"""
