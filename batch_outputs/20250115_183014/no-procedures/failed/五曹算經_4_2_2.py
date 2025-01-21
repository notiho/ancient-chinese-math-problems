"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
答曰：車主 a斛 粟主 b斛 。
"""

"""
Suppose there are 700 hu of millet, and it is desired to hire carts to transport it. For every hu, the cost of transport is 7 sheng of millet.
Question: how much millet does the cart owner receive, and how much does the millet owner retain?

Answer: the cart owner receives *a* hu, and the millet owner retains *b* hu.
"""

from fractions import Fraction

# 粟七百斛
total_millet = 700

# 每一斛雇七升
cost_per_hu = Fraction(7, 10)  # 7 sheng = 7/10 hu

# Calculate the total millet given to the cart owner
a = total_millet * cost_per_hu

# Calculate the remaining millet for the millet owner
b = total_millet - a

# Output the results
a, b
"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
