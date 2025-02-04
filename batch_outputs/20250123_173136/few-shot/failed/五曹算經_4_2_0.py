"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a斛 粟主 b斛 。
"""

"""
Suppose there are 700 hu of millet, and it is desired to hire carts to transport it.
For every 1 hu, the cost of hiring is 7 sheng of millet.
Question: how much millet does the cart owner receive, and how much does the millet owner retain?

The procedure says: Place the 700 hu of millet and multiply it by the 7 sheng per hu for hiring, obtaining 49 hu as the cart owner's millet.
Subtract this from the original 700 hu to find the millet owner's remaining millet.

Answer: the cart owner receives *a* hu, and the millet owner retains *b* hu.
"""

# 粟七百斛
粟 = 700

# 每一斛雇七升
雇率 = Fraction(7, 10)  # 7升 = 7/10斛

# 以雇粟七升乘之得四十九斛為車粟
車主粟 = 粟 * 雇率

# 以減本粟七百斛餘為主粟
粟主粟 = 粟 - 車主粟

# 答案
a = 車主粟
b = 粟主粟
"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
