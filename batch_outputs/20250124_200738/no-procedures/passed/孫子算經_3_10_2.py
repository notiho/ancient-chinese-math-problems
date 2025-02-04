"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 2,374 hu of millet, and each hu has an additional 3 sheng.
Question: how much millet is there in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 每斛加三升
每斛加 = 3

# 1 hu = 10 dou = 100 sheng
# Convert the additional sheng into hu
每斛加_in_hu = Fraction(每斛加, 100)

# Total millet in hu
a = 粟 + 粟 * 每斛加_in_hu#----- content ends here -----

"""
"""
