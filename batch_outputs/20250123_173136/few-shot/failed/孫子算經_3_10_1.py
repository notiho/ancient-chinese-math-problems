"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
術曰：置粟二千三百七十四斛，以一斛三升乘之，即得。
答曰： a斛 。
"""

"""
Suppose there are 2374 hu of millet, with each hu increased by 3 sheng.
Question: what is the total amount of millet?

The procedure says: Place the 2374 hu of millet.
Multiply it by 1 hu and 3 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 一斛三升 (1 hu = 10 sheng, so 1 hu 3 sheng = 1 + 3/10 hu)
一斛三升 = 1 + Fraction(3, 10)

# 以一斛三升乘之，即得
a = 粟 * 一斛三升
"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
