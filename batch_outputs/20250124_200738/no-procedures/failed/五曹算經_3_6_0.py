"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen in total. Every 5 wen can buy 3 pears.
Question: how many pears can be bought, and how much money is left?

Answer: *a* pears and *b* wen remaining.
"""

# Total money in wen
total_wen = 27 * 1000 + 833

# Cost of 3 pears is 5 wen
cost_per_3_pears = 5

# Calculate the total number of pears that can be bought
total_pears = (total_wen // cost_per_3_pears) * 3

# Calculate the remaining money
remaining_wen = total_wen % cost_per_3_pears

# Final answer
a = total_pears
b = remaining_wen

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 16699, Actual: 16698
Variable 'b' has wrong value. Expected: 4, Actual: 3"""
