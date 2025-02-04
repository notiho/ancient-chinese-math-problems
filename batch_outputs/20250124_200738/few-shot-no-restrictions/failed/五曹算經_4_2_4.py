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

The procedure says: Place the 700 hu of millet, and multiply it by the transport cost of 7 sheng per hu. 
Convert the result into hu (since 10 sheng = 1 hu), obtaining the amount of millet given to the cart owner.
Subtract this from the original 700 hu to find the amount retained by the millet owner.

Answer: the cart owner receives *a* hu, and the millet owner retains *b* hu.
"""

from fractions import Fraction

# 粟七百斛
粟 = 700

# 每一斛雇七升
每斛雇 = 7  # in 升

# Convert 7升 per 1斛 to 斛 (10升 = 1斛)
每斛雇_斛 = Fraction(每斛雇, 10)

# 車粟 = 粟 * 每斛雇_斛
車粟 = 粟 * 每斛雇_斛

# 主粟 = 粟 - 車粟
主粟 = 粟 - 車粟

# Results
a = 車粟
b = 主粟

# Output
a, b  # a = 車主所得粟 (in hu), b = 粟主所得粟 (in hu)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
