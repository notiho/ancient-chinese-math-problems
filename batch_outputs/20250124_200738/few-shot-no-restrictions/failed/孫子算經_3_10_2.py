"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
術曰：置粟二千三百七十四斛，以一斛三升乘之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 2374 hu of millet, with each hu increased by 3 sheng.
Question: what is the total amount of millet?

The procedure says: Place the 2374 hu of millet, and multiply it by 1 hu and 3 sheng. This gives the total.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 每斛加三升
一斛 = 1  # 1 hu
三升 = Fraction(3, 10)  # 3 sheng = 3/10 hu (since 1 hu = 10 sheng)

# 每斛的總量
每斛總量 = 一斛 + 三升

# 總粟數
a = 粟 * 每斛總量

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
