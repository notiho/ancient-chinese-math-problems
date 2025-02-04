"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
答曰：車主 a斛 粟主 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 700 hu of millet, and it is desired to hire carts to transport it. For every hu transported, the cart owner charges 7 sheng of millet as payment.
Question: how much millet does the cart owner receive, and how much does the millet owner retain?

Answer: the cart owner receives *a* hu, and the millet owner retains *b* hu.
"""

from fractions import Fraction

# Total millet in hu
total_millet = 700

# Payment per hu transported (in sheng)
payment_per_hu = 7

# Convert payment per hu to hu (since 1 hu = 10 dou = 100 sheng)
payment_per_hu_in_hu = Fraction(payment_per_hu, 100)

# Total millet paid to the cart owner
a = total_millet * payment_per_hu_in_hu

# Millet retained by the millet owner
b = total_millet - a

# Results
a, b#----- content ends here -----

"""
"""
