"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a斛 粟主 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 700 hu of millet, and it is desired to hire carts to transport it. 
For every 1 hu, the cost of transport is 7 sheng of millet.
Question: how much millet does the cart owner receive, and how much does the millet owner retain?

The procedure says: Place the 700 hu of millet, and multiply it by 7 sheng (the transport cost per hu), obtaining 49 hu as the millet for the cart owner.
Subtract this from the original 700 hu to find the millet retained by the millet owner.

Answer: the cart owner receives *a* hu, and the millet owner retains *b* hu.
"""

from fractions import Fraction

# 粟七百斛
粟 = 700

# 每一斛雇七升
每斛雇 = Fraction(7, 10)  # 7升 = 7/10斛

# 車主粟
車主粟 = 粟 * 每斛雇

# 粟主粟
粟主粟 = 粟 - 車主粟

# 答案
a = 車主粟
b = 粟主粟

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
