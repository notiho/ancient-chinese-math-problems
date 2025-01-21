"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
答曰： a斛 。
"""

"""
Suppose there is millet, 2374 hu, and each hu has an additional 3 sheng added.
Question: how much millet is there in total?

Answer: *a* hu.
"""

# 粟二千三百七十四斛
粟 = 2374

# 每斛加三升
每斛加升 = 3

# 1 hu = 10 dou = 100 sheng
每斛升數 = 100

# Total millet in hu
a = 粟 + Fraction(粟 * 每斛加升, 每斛升數)
"""
"""
