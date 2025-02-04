"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
術曰：置粟二千三百七十四斛，以一斛三升乘之，即得。
答曰： a斛 。
"""

"""
Suppose there is millet, 2374 hu, and each hu has an additional 3 sheng.
Question: how much millet is there in total?

The procedure says: Place the millet as 2374 hu. Multiply it by 1 hu and 3 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 一斛三升 (1 hu = 10 dou = 100 sheng, so 1 hu 3 sheng = 1 + 3/100 hu)
一斛三升 = 1 + Fraction(3, 100)

# 以一斛三升乘之，即得
a = 粟 * 一斛三升
"""
"""
