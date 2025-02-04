"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a(=49)斛 粟主 b(=651)斛 。
"""

"""
Suppose there are 700 hu of millet, and it is desired to hire carts to transport it. 
For every 1 hu, the cost of hiring is 7 sheng of millet.
Question: how much millet does the cart owner receive, and how much does the millet owner retain?

The procedure says: Place the 700 hu of millet, and multiply it by the hiring cost of 7 sheng.
Convert the result into hu, obtaining 49 hu as the cart owner's millet.
Subtract this from the original 700 hu, and the remainder is the millet owner's share.

Answer: the cart owner receives *a*(=49) hu, and the millet owner retains *b*(=651) hu.
"""

# 粟七百斛
粟 = 700

# 每一斛雇七升
雇每斛 = Fraction(7, 10)  # 7升 = 7/10斛

# 以雇粟七升乘之
車粟 = 粟 * 雇每斛

# 得四十九斛為車粟
a = 車粟  # 49

# 以減本粟七百斛餘為主粟
b = 粟 - 車粟  # 651
"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
