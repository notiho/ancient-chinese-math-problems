"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there is 27 guan and 833 wen of money. Each 5 wen buys 3 pears.
Question: how many pears can be bought, and how much money is left?

Answer: *a* pears and *b* wen remaining.
"""

# Total money in wen
total_money = 27 * 1000 + 833  # 1 guan = 1000 wen

# Cost of 3 pears is 5 wen
cost_per_3_pears = 5

# Total pears that can be bought
total_pears = total_money // cost_per_3_pears * 3

# Remaining money
remaining_money = total_money % cost_per_3_pears

# Final answer
a = total_pears
b = remaining_money#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 16699, Actual: 16698
Variable 'b' has wrong value. Expected: 4, Actual: 3"""
